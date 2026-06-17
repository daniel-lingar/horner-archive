/* Leaflet map for Horner archive PPAN / GPS sites */
window.HornerSiteMap = (function () {
  function popupHtml(m) {
    var parts = ["<strong>" + m.name + "</strong>"];
    if (m.ppan) {
      parts.push("<code>" + m.ppan + "</code>");
    }
    if (m.owner) {
      parts.push(m.owner + (m.acres ? " · " + m.acres + " ac" : ""));
    }
    if (m.legal) {
      parts.push("<span style='font-size:0.85em'>" + m.legal + "</span>");
    }
    if (m.note) {
      parts.push("<em style='font-size:0.85em'>" + m.note + "</em>");
    }
    parts.push(
      "<span style='font-size:0.8em;color:#666'>" +
        m.lat.toFixed(5) + "°N, " + Math.abs(m.lng).toFixed(5) + "°W</span>"
    );
    return parts.join("<br>");
  }

  function addLegend(map, data, position) {
    var legend = L.control({ position: position || "bottomright" });
    legend.onAdd = function () {
      var div = L.DomUtil.create("div", "horner-map-legend");
      div.innerHTML = "<strong>Legend</strong>";
      data.legend.forEach(function (item) {
        var row = document.createElement("div");
        row.className = "horner-legend-row";
        var swatch = document.createElement("span");
        swatch.className = "horner-legend-swatch";
        if (item.shape === "line" || item.shape === "dashed") {
          swatch.style.background = "transparent";
          swatch.style.borderTop = "3px solid " + item.color;
          if (item.shape === "dashed") {
            swatch.style.borderTopStyle = "dashed";
          }
          swatch.style.height = "0";
          swatch.style.marginTop = "8px";
        } else {
          swatch.style.background = item.color;
        }
        row.appendChild(swatch);
        row.appendChild(document.createTextNode(item.label));
        div.appendChild(row);
      });
      div.innerHTML += "<div class='horner-legend-source'>" + data.source + "</div>";
      return div;
    };
    legend.addTo(map);
  }

  function init(containerId, options) {
    options = options || {};
    var data = window.HORNER_MAP_DATA;
    var el = document.getElementById(containerId);
    if (!el || !data) {
      return null;
    }

    var map = L.map(containerId, {
      zoomControl: true,
      scrollWheelZoom: true
    });

    var osm = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    });

    var satellite = L.tileLayer(
      "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
      {
        maxZoom: 19,
        attribution: "Tiles &copy; Esri"
      }
    );

    var labels = L.tileLayer(
      "https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}",
      { maxZoom: 19, pane: "overlayPane", opacity: 0.7 }
    );

    satellite.addTo(map);
    labels.addTo(map);

    var baseLayers = {
      Satellite: satellite,
      "Street map": osm
    };

    var groups = {
      sites: L.layerGroup(),
      access: L.layerGroup(),
      reference: L.layerGroup()
    };

    data.markers.forEach(function (m) {
      var marker = L.circleMarker([m.lat, m.lng], {
        radius: m.radius || 7,
        color: "#fff",
        weight: 2,
        fillColor: m.color,
        fillOpacity: 0.92
      }).bindPopup(popupHtml(m));
      var layer = groups[m.group] || groups.sites;
      marker.addTo(layer);
    });

    data.corridors.forEach(function (c) {
      var line = L.polyline(c.coords, {
        color: c.color,
        weight: c.weight || 3,
        opacity: c.opacity || 0.8,
        dashArray: c.dash || null
      }).bindPopup("<strong>" + c.name + "</strong>");
      var layer = groups[c.group] || groups.access;
      line.addTo(layer);
    });

    groups.sites.addTo(map);
    groups.access.addTo(map);
    if (options.showReference !== false) {
      groups.reference.addTo(map);
    }

    L.control.layers(baseLayers, {
      "Historic sites": groups.sites,
      "Access corridors": groups.access,
      "Reference / approach": groups.reference
    }, { collapsed: false }).addTo(map);

    addLegend(map, data, options.legendPosition || "bottomright");

    var studyMarkers = data.markers.filter(function (m) {
      return m.group !== "reference";
    });
    var bounds = L.latLngBounds(studyMarkers.map(function (m) {
      return [m.lat, m.lng];
    }));
    map.fitBounds(bounds.pad(options.padding || 0.12));

    if (options.defaultZoom) {
      map.setZoom(options.defaultZoom);
    }

    return map;
  }

  return { init: init };
})();
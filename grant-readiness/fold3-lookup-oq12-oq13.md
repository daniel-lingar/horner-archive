# Fold3 Lookup Sheet — OQ-12 / OQ-13

**Use when:** Logged into Fold3 (or ordering NARA M317 copies)  
**Bundle with:** [NARA request OQ-15](nara-request-oq15.md) if mailing a combined order

---

## OQ-12 — William Gordon Acord (priority: card images only)

| Field | Value |
|-------|-------|
| Status | **Unit closed v20.6** — Co. H, 10th Arkansas Militia |
| NARA M317 card | **44903963** |
| Goal | Download card images for `sources/cmsr/` publication |

**Search strings**

1. `Acord, William G.` + Arkansas + Confederate
2. Direct card lookup: M317 card **44903963**
3. Unit browse: 10th Arkansas Militia → Company H

**Save as:** `sources/cmsr/william-gordon-acord-m317-44903963.pdf` (or JPG set)

---

## OQ-13 — Henry Stewart (priority: unit confirmation)

| Field | Value |
|-------|-------|
| Status | **Identity closed** — Joseph Henry Stewart, 1840–1930, Yale Cemetery |
| Open question | CSA unit designation |
| Goal | Match M317 card to Johnson County Henry Stewart |

**Search strings**

1. `Stewart, Henry` + Arkansas + Confederate
2. `Stewart, Joseph H.` + Arkansas
3. Browse: 10th Arkansas Militia → Company I (dossier v2 roster lead)
4. Browse: 7th Arkansas Cavalry (Johnson County companies)

**Disambiguation checks before accepting a card**

- Residence or enlistment place in **Johnson / Pope / Newton** county corridor
- Age consistent with b. Dec 1840 (enlistment 1861–1864)
- Not the Missouri Union deserter or unrelated Gordon's Cavalry entries without county proof

**Save as:** `sources/cmsr/henry-stewart-m317-[card#].pdf`

---

## After retrieval

- [ ] Update §13 OQ-13 to closed (or split identity/unit notes)
- [ ] Add §14 doc-entry with card images
- [ ] Update §16 evidentiary table
- [ ] Regenerate `dossier.pdf`
- [ ] Commit as v20.7 (or next patch)
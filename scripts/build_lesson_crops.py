"""Reproduce exact source details from their versioned crop manifest.

This does not authenticate sources or provide the pending human review.
"""
from pathlib import Path
import hashlib,json
from PIL import Image
R=Path(__file__).resolve().parents[1]
for item in json.loads((R/'sources/reviewed/lesson-derivatives.json').read_text()):
    source=R/item['source']
    if hashlib.sha256(source.read_bytes()).hexdigest()!=item['source_sha256']:
        raise SystemExit('Source changed: review before cropping '+str(source))
    Image.open(source).crop(item['box']).save(R/item['path'])
    print(item['path']+'; exact crop only; human review remains pending')

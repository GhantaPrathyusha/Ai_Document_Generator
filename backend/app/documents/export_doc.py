import os
from docx import Document
from datetime import datetime
from app.config import settings

def export_to_docx(text: str) -> str:
    export_dir = settings.EXPORT_DIR
    os.makedirs(export_dir, exist_ok=True)

    filename = f"output_{int(datetime.utcnow().timestamp())}.docx"
    filepath = os.path.join(export_dir, filename)

    doc = Document()
    # simple splitting into paragraphs
    for p in text.split("\n\n"):
        doc.add_paragraph(p)
    doc.save(filepath)
    return filepath

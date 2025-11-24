from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from app.services.llm_service import generate_document_content
from app.deps import get_current_user
from app.schemas import GenerateRequest
from app.documents.export_doc import export_to_docx
from app.documents.export_ppt import export_to_pptx
import os

router = APIRouter(tags=["documents"])

@router.post("/generate")
def generate_doc(payload: GenerateRequest, user = Depends(get_current_user)):
    try:
        content = generate_document_content(payload.prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if payload.format.lower() == "docx":
        file_path = export_to_docx(content)
        media_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

    elif payload.format.lower() == "pptx":
        file_path = export_to_pptx(content)
        media_type = "application/vnd.openxmlformats-officedocument.presentationml.presentation"

    else:
        raise HTTPException(status_code=400, detail="Invalid format. Use 'docx' or 'pptx'.")

    filename = os.path.basename(file_path)

    return FileResponse(
        path=file_path,
        filename=filename,
        media_type=media_type
    )

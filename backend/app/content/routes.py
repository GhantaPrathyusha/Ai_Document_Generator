from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.schemas import GenerateRequest, HistoryOut
from app.database import get_db
from app.models import ContentHistory
from app.content.generator import generate_text_from_prompt
from app.deps import get_current_user
from app.documents.export_doc import export_to_docx
from app.documents.export_ppt import export_to_pptx

router = APIRouter(tags=["content"])  # ❗ Removed prefix="/content"

@router.post("/generate", response_model=HistoryOut)
def generate(payload: GenerateRequest, 
             db: Session = Depends(get_db), 
             current_user = Depends(get_current_user)):
    
    try:
        output_text = generate_text_from_prompt(payload.prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {e}")

    hist = ContentHistory(user_id=current_user.id, 
                          prompt=payload.prompt, 
                          output=output_text)
    db.add(hist)
    db.commit()
    db.refresh(hist)

    # Create export file
    if payload.format and payload.format.lower() == "pptx":
        _ = export_to_pptx(output_text)
    else:
        _ = export_to_docx(output_text)

    return hist

@router.get("/history", response_model=list[HistoryOut])
def history(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    rows = db.query(ContentHistory)\
        .filter(ContentHistory.user_id == current_user.id)\
        .order_by(ContentHistory.created_at.desc())\
        .all()
    return rows

@router.get("/download/docx/{history_id}")
def download_docx(history_id: int, 
                  db: Session = Depends(get_db), 
                  current_user = Depends(get_current_user)):

    record = db.query(ContentHistory)\
                .filter(ContentHistory.id == history_id, 
                        ContentHistory.user_id == current_user.id)\
                .first()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    path = export_to_docx(record.output)
    return FileResponse(path)

@router.get("/download/pptx/{history_id}")
def download_pptx(history_id: int, 
                  db: Session = Depends(get_db), 
                  current_user = Depends(get_current_user)):

    record = db.query(ContentHistory)\
                .filter(ContentHistory.id == history_id, 
                        ContentHistory.user_id == current_user.id)\
                .first()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    path = export_to_pptx(record.output)
    return FileResponse(path)

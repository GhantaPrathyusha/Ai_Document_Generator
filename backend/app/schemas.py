from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RegisterRequest(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class GenerateRequest(BaseModel):
    prompt: str
    format: Optional[str] = "docx"

class HistoryOut(BaseModel):
    id: int
    prompt: str
    output: str
    created_at: datetime

    model_config = {"from_attributes": True}

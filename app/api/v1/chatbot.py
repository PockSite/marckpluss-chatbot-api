from dns import message
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.dependencies import get_openai_service
from app.schemas.chatbot import ChatRequest

from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

router = APIRouter()

@router.post("/chat", status_code=status.HTTP_200_OK)
def chat(
    request: ChatRequest,
    token: str = Depends(oauth2_scheme),
    service = Depends(get_openai_service)):
    response = service.chat(request.message)

    return {"response": response}
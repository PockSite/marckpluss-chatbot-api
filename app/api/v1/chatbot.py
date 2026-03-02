from fastapi import APIRouter, Depends, HTTPException, status
from app.core.dependencies import get_openai_service
from app.schemas.chatbot import ChatRequest

router = APIRouter()

@router.post("/chat", status_code=status.HTTP_200_OK)
def chat(
    request: ChatRequest,
    service = Depends(get_openai_service)):
    response = service.chat(request.message)
    return {"response": response}
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.dependencies import get_openai_service
from app.schemas.chatbot import ChatRequest
from app.core.limiter import limiter

router = APIRouter()

@limiter.limit("5/minute")
@router.post("/chat", status_code=status.HTTP_200_OK)
def chat(
    request: ChatRequest,
    service = Depends(get_openai_service)):
    response = service.chat(request.message)
    return {"response": response}
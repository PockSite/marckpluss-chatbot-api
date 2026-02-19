from fastapi import APIRouter
from app.api.v1 import chatbot

router = APIRouter()

router.include_router(chatbot.router, prefix="/chatbot", tags=["Chatbot"])
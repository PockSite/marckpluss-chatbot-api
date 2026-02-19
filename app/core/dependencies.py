
from fastapi import Depends
from app.service.openai_service import OpenAIService
from app.client.openai_client import OpenAIClient

def get_openai_service(client: OpenAIClient = Depends()):
    return OpenAIService(client)

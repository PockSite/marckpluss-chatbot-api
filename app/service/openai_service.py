from app.client.openai_client import OpenAIClient   

class OpenAIService:
    def __init__(self, client: OpenAIClient):
        self.client = client

    def chat(self, message: str) -> str:
        if not message:
            raise ValueError("Message is required")

        return self.client.send_message(message)

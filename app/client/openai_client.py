from openai import OpenAI
from app.core.config import OPENAI_API_KEY
class OpenAIClient():

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def send_message(self, message: str) -> str:
        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=message
        )

        return response.output_text

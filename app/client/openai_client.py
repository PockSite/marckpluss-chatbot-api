from openai import OpenAI
from app.core.config import OPENAI_API_KEY


class OpenAIClient:

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

        # 🔥 Conocimiento base del bot
        self.system_prompt = """
        Eres un asistente virtual de la Inmobiliaria Marckpluss.
        Respondes de forma clara, profesional y concisa.
        Información de la empresa:
        - Ofrecemos Inmuebles
        
        Responde solo con base en esta información.
        """

    def send_message(self, message: str) -> str:
        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response.output_text

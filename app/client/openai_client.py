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
        
        En Marckpluss nos dedicamos a la intermediación de ventas y arriendos por corretaje a nivel nacional, con un enfoque estratégico en Bogotá. Nuestro propósito es acompañar a cada cliente de manera cercana, familiar, profesional y transparente durante todo el proceso de compra y venta de su propiedad.
        Creemos que cada cliente que llega a traves de nosostros con la ilucion de vender o adquirir su propiedad, representa una historia familiar, una meta o un nuevo comienzo. Por eso trabajamos con un modelo híbrido presencial y virtual que nos permite brindar atención personalizada, eficiente y adaptada a las necesidades  de cada familia.
        Nos diferenciamos por ofrecer más que un servicio inmobiliario un acompañamiento humano, con un proceso claro que genera tranquilidad y confianza en cada paso.

        DATOS DE LA EMPRESA 
        Trayectoria desde el 2010 

        REDES SOCIALES 

        Instagram : @marckpluss

        TikTok : @inmueblesmarckpluss

        Facebook : Marckpluss Inmobiliaria 

        Whatsapp: 3204795284
        
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

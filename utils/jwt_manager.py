from jwt import encode, decode
from dotenv import load_dotenv
import os

# cargamos las variables de entorno desde el archivo ".env"
load_dotenv()

def create_token(data: dict) -> str:
    token: str = encode(payload=data, key=os.getenv('API_KEY'), algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key=os.getenv('API_KEY'), algorithms=['HS256'])
    return data
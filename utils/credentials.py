import os
from dotenv import load_dotenv

load_dotenv()

def get_credentials(prefix):
    user = os.getenv(f"{prefix}_USER")
    password = os.getenv(f"{prefix}_PASS")
    if not user or not password:
        raise Exception(f"Credenciais não encontradas para {prefix}")
    return user, password
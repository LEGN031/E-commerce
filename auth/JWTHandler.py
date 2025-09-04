import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv('./config/.env')

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

def create_acces_token(data: dict, expiresDelta:timedelta| None=None):
    toEncode=data.copy()
    expires=datetime.utcnow() + (expiresDelta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    toEncode.update({"exp": expires})
    encodeJWT = jwt.encode(toEncode, SECRET_KEY, algorithm=ALGORITHM)
    return encodeJWT

def verifyAccesToken(token:str):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception('Token has expired')
    except jwt.InvalidTokenError:
        raise Exception('Invalid Token')

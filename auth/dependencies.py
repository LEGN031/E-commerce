from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .JWTHandler import verifyAccesToken

oAuth2 = OAuth2PasswordBearer(tokenUrl="Login")

def get_current_user(token: str = Depends(oAuth2)):
    try:
        payload = verifyAccesToken(token)
        user = payload.get("sub")
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Not Found')
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    

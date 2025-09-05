from fastapi import APIRouter, HTTPException, Depends
from auth.JWTHandler import create_access_token, verifyAccesToken, ACCESS_TOKEN_EXPIRE_MINUTES
from models.models import Users, Sellers, UsersAccounts, SellersAccounts
from datetime import timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from db.dbConection import dbConection
from db.schemas import usersSchema
import hashlib

router = APIRouter(prefix="/auth", tags=["auth"])
oauth2 = OAuth2PasswordBearer(tokenUrl="login")
sellers_collection = dbConection["e-commerce"]["sellers"]
users_collection = dbConection["e-commerce"]["users"]


def get_user():
    user = users_collection.find()
    if not user:
        raise HTTPException(status_code=404, detail='Not Found')
    user = list(map(usersSchema.userAccounts_schema, user))
    return user


def get_user(mail: str):
    user = users_collection.find_one({"email": mail})
    if not user:
        raise HTTPException(status_code=404, detail='Not Found')
    user = usersSchema.userAccounts_schema(user)
    return UsersAccounts(**user)

@router.post("/login/user")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user_db = users_collection.find_one({"email": form_data.username})
    if not user_db:
        raise HTTPException(status_code=404, detail='Not Found')
    user = get_user(form_data.username)

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email},  # "sub" = subject
        expiresDelta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


def get_password_hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

@router.post("/register/user")
async def register_user(user: UsersAccounts):
    user_dict = user.model_dump()
    del user_dict['idUser']
    user_dict["password"] = get_password_hash(user_dict["password"])
    if users_collection.find_one({"email": user_dict["email"]}):
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = users_collection.insert_one(user_dict)
    created_user = users_collection.find_one({"_id": new_user.inserted_id})
    return usersSchema.userAccounts_schema(created_user)

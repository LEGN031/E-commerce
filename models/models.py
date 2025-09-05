from pydantic import BaseModel
from typing import Optional

class Products(BaseModel):
    idProduct:      Optional[str] = None
    name:           str
    price:          float
    productCode:    str

class Sellers(BaseModel):
    idSeller:       Optional[str] = None
    fullName:       str
    documentID:     str
    sellsQuantity:  int

class SellersAccounts(Sellers):
    email:          str
    password:       str

class Users(BaseModel):
    idUser:        Optional[str] = None
    fullName:       str
    documentID:     str
    aticlesBought:  list

class UsersAccounts(Users):
    email:          str
    password:       str

class Purchases(BaseModel):
    idPurchases:        Optional[str] = None
    productID:          str
    userID:             str

class Inventory(BaseModel):
    idPurchases:        Optional[str] = None
    productID:          str
    sellerID:           Optional[str] = None
    quantity:           int

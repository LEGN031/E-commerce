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

class Users(BaseModel):
    idUsers:        Optional[str] = None
    fullName:       str
    documentID:     str
    aticlesBought:  list

class Purchases(BaseModel):
    idPurchases:        Optional[str] = None
    productID:          str
    userID:             str

class Inventory(BaseModel):
    idPurchases:        Optional[str] = None
    productID:          str
    sellerID:           Optional[str] = None
    quantity:           int

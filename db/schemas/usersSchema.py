def user_schema(user) -> dict:
    return {
        "idUser": str(user["_id"]),
        "fullName": user["fullName"],
        "documentID": user["documentID"],
        "aticlesBought": user["aticlesBought"]
    }

def userAccounts_schema(useraccount) -> dict:
    return {
        "idUser": str(useraccount["_id"]),
        "fullName": useraccount["fullName"],
        "documentID": useraccount["documentID"],
        "aticlesBought": useraccount["aticlesBought"],
        "email": useraccount["email"],
        "password": useraccount["password"]
    }
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv("./config/.env")


DB_PASSWORD = os.getenv("DB_PASSWORD")


#local
#db_client = MongoClient("mongodb://localhost:27017/")

#remote
dbConection = MongoClient(f"mongodb+srv://medinae663_db_user:{DB_PASSWORD}@bde-commerce.vmwieff.mongodb.net/")


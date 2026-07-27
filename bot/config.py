import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("API_ID","24861505"))
    API_HASH = os.getenv("API_HASH","fad28c88a18f4f2d9c67c2c08c19696f")
    BOT_TOKEN = os.getenv("BOT_TOKEN","8715105949:AAH8MREniTQXOYV7ebLalpPtLakM2rEUNMg")
    MONGO_URI = os.getenv("MONGO_URI","mongodb+srv://hulowugiviz3_db_user:y2ZZ0peg4wqE4OdV@cluster0.x417wvo.mongodb.net/?appName=Cluster0")
    DB_NAME = os.getenv("DB_NAME", "quiz_bot")
    OWNER_ID = int(os.getenv("OWNER_ID","8583075184"))

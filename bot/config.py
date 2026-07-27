import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("API_ID","24861505"))
    API_HASH = os.getenv("API_HASH","fad28c88a18f4f2d9c67c2c08c19696f")
    BOT_TOKEN = os.getenv("BOT_TOKEN","8715105949:AAH8MREniTQXOYV7ebLalpPtLakM2rEUNMg")
    

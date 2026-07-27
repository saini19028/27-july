from motor.motor_asyncio import AsyncIOMotorClient
from bot.config import Config
import ssl

class Database:
    def __init__(self):
        self.client = None
        self.db = None
        self.users = None
        self.quizzes = None
        self.admins = None

    async def initialize(self):
        # SSL handshake error को ठीक करने के लिए सभी TLS विकल्प स्पष्ट रूप से सेट करें
        # URI में पहले से tlsAllowInvalidCertificates=true है, फिर भी Motor उसे नहीं मान रहा
        # इसलिए हम क्लाइंट कंस्ट्रक्टर में ही विकल्प दे रहे हैं
        self.client = AsyncIOMotorClient(
            Config.MONGO_URI,
            tls=True,
            tlsAllowInvalidCertificates=True,   # सर्टिफिकेट वेरिफिकेशन बंद
            tlsAllowInvalidHostnames=True,      # होस्टनेम वेरिफिकेशन बंद
            serverSelectionTimeoutMS=5000       # 5 सेकंड टाइमआउट
        )

        # डेटाबेस और कलेक्शन सेट करें
        self.db = self.client[Config.DB_NAME]
        self.users = self.db.users
        self.quizzes = self.db.quizzes
        self.admins = self.db.admins

        # सुनिश्चित करें कि कनेक्शन वास्तव में काम कर रहा है
        try:
            await self.client.admin.command('ismaster')
            print("✅ MongoDB कनेक्शन सफल!")
        except Exception as e:
            print(f"❌ MongoDB कनेक्शन विफल: {e}")
            raise

        # इंडेक्स बनाएँ
        await self.users.create_index("user_id", unique=True)
        await self.quizzes.create_index("quiz_id", unique=True)
        await self.admins.create_index("user_id", unique=True)

        # अगर कोई एडमिन नहीं है तो OWNER को एडमिन बनाएँ
        if not await self.admins.find_one({"user_id": Config.OWNER_ID}):
            await self.admins.insert_one({"user_id": Config.OWNER_ID})

    # ---------- User Methods ----------
    async def get_user(self, user_id):
        return await self.users.find_one({"user_id": user_id})

    async def save_user(self, user_data):
        await self.users.update_one(
            {"user_id": user_data["user_id"]},
            {"$set": user_data},
            upsert=True
        )

    async def get_all_users(self):
        return await self.users.find().to_list(length=None)

    # ---------- Quiz Methods ----------
    async def create_quiz(self, quiz_data):
        await self.quizzes.insert_one(quiz_data)
        return quiz_data["quiz_id"]

    async def get_quiz(self, quiz_id):
        return await self.quizzes.find_one({"quiz_id": quiz_id})

    async def update_quiz(self, quiz_id, update_data):
        await self.quizzes.update_one({"quiz_id": quiz_id}, {"$set": update_data})

    async def delete_quiz(self, quiz_id):
        await self.quizzes.delete_one({"quiz_id": quiz_id})

    async def get_all_quizzes(self, published_only=False):
        filter_criteria = {"is_published": True} if published_only else {}
        return await self.quizzes.find(filter_criteria).to_list(length=None)

    # ---------- Admin Methods ----------
    async def is_admin(self, user_id):
        return await self.admins.find_one({"user_id": user_id}) is not None

    async def add_admin(self, user_id):
        await self.admins.insert_one({"user_id": user_id})

    async def remove_admin(self, user_id):
        await self.admins.delete_one({"user_id": user_id})

    async def get_all_admins(self):
        return await self.admins.find().to_list(length=None)

db = Database()

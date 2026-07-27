import asyncio
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from bot.config import Config
from bot.database.mongo import db
from bot.handlers.start import start_cmd

class QuizBot:
    def __init__(self):
        self.app = Client(
            "quiz_bot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN
        )
        self.add_handlers()

    def add_handlers(self):
        self.app.add_handler(MessageHandler(start_cmd, filters.command("start") & filters.private))

    async def start(self):
        await db.initialize()
        print("✅ बॉट स्टार्ट हो गया है!")
        await self.app.start()
        await asyncio.Event().wait()

    async def stop(self):
        await self.app.stop()
        print("🛑 बॉट बंद हो गया।")

if __name__ == "__main__":
    bot = QuizBot()
    try:
        asyncio.run(bot.start())
    except KeyboardInterrupt:
        asyncio.run(bot.stop())

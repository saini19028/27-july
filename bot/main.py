import asyncio
from pyrogram import Client, filters
from bot.config import Config
from bot.database.mongo import db

app = Client(
    "quiz_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    user = message.from_user
    await db.save_user({
        "user_id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name
    })
    await message.reply("✅ **आप डेटाबेस में सेव हो गए!**\nअब आप क्विज़ खेल सकते हैं।")

async def main():
    await db.initialize()
    print("✅ बॉट स्टार्ट हो गया है!")
    await app.start()
    # बॉट को चालू रखने के लिए infinite wait
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())

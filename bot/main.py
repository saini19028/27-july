from pyrogram import Client, filters
from bot.config import Config

# बॉट क्लाइंट बनाएँ
app = Client(
    "quiz_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# /start कमांड हैंडलर
@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    await message.reply("✅ **बॉट काम कर रहा है!**\n\nबधाई हो, अब हम सही रास्ते पर हैं।")

if __name__ == "__main__":
    print("✅ बॉट स्टार्ट हो गया है!")
    app.run()  # यह बॉट को चालू रखेगा

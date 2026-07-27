from pyrogram.types import Message
from bot.database.mongo import db
import time

async def start_cmd(client, message: Message):
    user = message.from_user
    await db.save_user({
        "user_id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "joined_at": time.time()
    })
    await message.reply(f"**🎉 नमस्ते {user.first_name}!**\n\nबॉट सफलतापूर्वक काम कर रहा है! ✅")

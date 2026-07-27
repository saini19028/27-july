import uuid
from bot.database.mongo import db

def generate_quiz_id():
    return str(uuid.uuid4())[:8]

async def is_admin(user_id):
    return await db.is_admin(user_id)

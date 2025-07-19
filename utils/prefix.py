from pyrogram import filters
from database.prefixes import PrefixDB

prefix_db = PrefixDB()

def command(cmd: str):
    async def func(flt, client, message):
        user_id = message.from_user.id if message.from_user else None
        if not user_id:
            return False

        prefix = await prefix_db.get_prefix(user_id)
        text = message.text or ""
        return text.startswith(f"{prefix}{cmd}")
    
    return filters.create(func)
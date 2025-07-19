from pyrogram import filters
from database.prefixes import PrefixDB

prefix_db = PrefixDB()

def command(cmd: str):
    async def func(flt, client, message):
        if not message.from_user:
            return False

        user_id = message.from_user.id
        text = message.text or ""

        prefix = await prefix_db.get_prefix(user_id)
        if not prefix:
            prefix = "."

        match = text.startswith(f"{prefix}{cmd}")
        
        # Debug log (aktifkan saat perlu)
        # print(f"[DEBUG] UserID: {user_id} | Prefix: {prefix} | CMD: {cmd} | Match: {match} | Text: {text}")

        return match

    return filters.create(func)
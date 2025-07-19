from pyrogram import Client, idle
from config import API_ID, API_HASH, STRING_SESSION
import time

# Import plugin secara manual
from plugins import ping
from plugins import alive
from plugins import broadcast
from plugins import help
from plugins import gruplogs
from plugins import prefixes
from plugins import blacklist

start_time = time.time()

app = Client(
    name="arika_userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
    parse_mode="html"
)

if __name__ == "__main__":
    app.start()
    me = app.get_me()
    print(f"✅ Arika Userbot aktif sebagai: {me.first_name} [ID: {me.id}]")
    idle()
    print("🔴 Arika Userbot dimatikan.")
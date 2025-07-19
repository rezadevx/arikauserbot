from pyrogram import Client, idle
from config import API_ID, API_HASH, STRING_SESSION
import importlib
import os
import time

start_time = time.time()

app = Client(
    name="arika_userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
    parse_mode="html"
)

def load_plugins():
    for file in os.listdir("plugins"):
        if file.endswith(".py"):
            try:
                print(f"🔹 Memuat plugin: {file}")
                importlib.import_module(f"plugins.{file[:-3]}")
            except Exception as e:
                print(f"❌ Gagal memuat plugin {file}: {e}")

if __name__ == "__main__":
    app.start()
    me = app.get_me()
    print(f"✅ Arika Userbot aktif sebagai: {me.first_name} [ID: {me.id}]")
    load_plugins()
    idle()
    print("🔴 Arika Userbot dimatikan.")
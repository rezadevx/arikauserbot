from navygram import Client, idle
from config import API_ID, API_HASH, STRING_SESSION
import importlib, os, time

start_time = time.time()

app = Client(
    name="arika_userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
    parse_mode="html"
)

def load_plugins():
    for file in os.listdir("./plugins"):
        if file.endswith(".py"):
            importlib.import_module(f"plugins.{file[:-3]}")

if __name__ == "__main__":
    load_plugins()
    print("🔵 Arika Userbot aktif!")
    app.start()
    idle()
    print("🔴 Arika Userbot dimatikan.")
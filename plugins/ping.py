from pyrogram import Client
from utils.prefix import command
from core.time import start_time
import time

def get_uptime():
    uptime = time.time() - start_time
    h, m, s = int(uptime // 3600), int((uptime % 3600) // 60), int(uptime % 60)
    return f"{h} jam {m} menit {s} detik"

@Client.on_message(command("ping"))
async def ping(client, message):
    start = time.time()
    reply = await message.reply("🏓")
    end = time.time()

    latency = (end - start) * 1000
    uptime = get_uptime()
    user = await client.get_me()

    await reply.edit_text(
        f"🏓 <b>Pong!</b>\n"
        f"👤 <b>Userbot:</b> {user.first_name}\n"
        f"📶 <b>Latency:</b> {latency:.2f} ms\n"
        f"⏱ <b>Uptime:</b> {uptime}"
    )
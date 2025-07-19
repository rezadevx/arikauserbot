from pyrogram import Client, filters
from main import start_time
import time

def get_uptime():
    uptime = time.time() - start_time
    h, m, s = int(uptime // 3600), int((uptime // 60) % 60), int(uptime % 60)
    return f"{h} jam {m} menit {s} detik"

@Client.on_message(filters.command("ping", prefixes=".") & filters.me)
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
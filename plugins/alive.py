from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.prefix import command
from core.time import start_time
import time

def get_uptime():
    uptime = time.time() - start_time
    h, m, s = int(uptime // 3600), int((uptime % 3600) // 60), int(uptime % 60)
    return f"{h} jam {m} menit {s} detik"

@Client.on_message(command("alive"))
async def alive(client, message):
    user = await client.get_me()
    uptime = get_uptime()

    text = (
        "ᴬʳⁱᵏᵃ ᵁˢᵉʳᵇᵒᵗ\n\n"
        f"ᴰⁱ ᵇᵘᵃᵗ ᵒˡᵉʰ: ʳᵉᶻᵃᵈᵉᵛˣ\n"
        f"ᴵᴰ ᴾᵉⁿᵍᵍᵘⁿᵃ: <code>{user.id}</code>\n"
        f"⏱ ᵁᵖᵗⁱᵐᵉ: {uptime}\n"
        f"✅ ˢᵗᵃᵗᵘˢ: ᴬᵏᵗⁱᶠ"
    )

    # Coba inline button, fallback ke teks jika tidak didukung
    try:
        await message.reply(
            text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✖️ ᴛᴜᴛᴜᴘ", callback_data="close_alive")]
            ])
        )
    except Exception:
        await message.reply(text)

@Client.on_callback_query(filters.regex("close_alive"))
async def close_alive(_, query):
    await query.message.delete()
    await query.answer("Dihapus ✅", show_alert=False)
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from main import start_time
import time

def get_uptime():
    uptime = time.time() - start_time
    h, m, s = int(uptime // 3600), int((uptime // 60) % 60), int(uptime % 60)
    return f"{h} jam {m} menit {s} detik"

ALIVE_TEXT = (
    "ᴀʀɪᴋᴀ ᴜsᴇʀʙᴏᴛ\n\n"
    "ᴅɪ ʙᴜᴀᴛ ᴏʟᴇʜ : ʀᴇᴢᴀᴅᴇᴠx\n"
    "ɪᴅ ᴘᴇɴɢɢᴜɴᴀ : <code>{id}</code>\n"
    "Uᴘᴛɪᴍᴇ : {uptime}\n"
    "sᴛᴀᴛᴜs : ᴏɴʟɪɴᴇ ✅"
)

@Client.on_message(filters.command("alive", prefixes=".") & filters.me)
async def alive(client, message):
    user = await client.get_me()
    uptime = get_uptime()
    text = ALIVE_TEXT.format(id=user.id, uptime=uptime)

    try:
        await message.reply(
            text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❌ ᴄʟᴏsᴇ", callback_data="close_alive")]
            ])
        )
    except Exception:
        await message.reply(text)

@Client.on_callback_query(filters.regex("close_alive"))
async def close_alive(client, callback_query: CallbackQuery):
    try:
        await callback_query.message.delete()
    except Exception:
        await callback_query.answer("❌ Tidak bisa menghapus pesan ini.", show_alert=True)
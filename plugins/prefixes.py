from pyrogram import Client, filters
from database.prefixes import PrefixDB

prefix_db = PrefixDB()

@Client.on_message(filters.command("setprefix", prefixes=".") & filters.me)
async def set_prefix(client, message):
    if len(message.command) < 2:
        return await message.reply(
            "❌ Format salah.\nContoh: <code>.setprefix !</code>"
        )

    new_prefix = message.command[1]

    if len(new_prefix) > 2:
        return await message.reply("❌ Prefix terlalu panjang. Maksimal 2 karakter.")

    await prefix_db.set_prefix(message.from_user.id, new_prefix)
    await message.reply(f"✅ Prefix kamu berhasil diubah ke: <code>{new_prefix}</code>")
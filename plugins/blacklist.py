from pyrogram import Client, filters
from database.blacklist import BlacklistDB

db = BlacklistDB()

@Client.on_message(filters.command("addbl", prefixes=".") & filters.me)
async def add_blacklist(client, message):
    chat_id = message.chat.id
    await db.add(chat_id)
    await message.reply("✅ Grup atau pengguna ini telah dimasukkan ke blacklist broadcast.")

@Client.on_message(filters.command("unbl", prefixes=".") & filters.me)
async def remove_blacklist(client, message):
    chat_id = message.chat.id
    await db.remove(chat_id)
    await message.reply("✅ Grup atau pengguna ini telah dihapus dari blacklist broadcast.")
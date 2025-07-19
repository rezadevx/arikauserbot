from pyrogram import Client, filters
from database.blacklist import BlacklistDB

db = BlacklistDB()

@Client.on_message(filters.command("gcast", prefixes=".") & filters.me)
async def gcast(client, message):
    if not message.reply_to_message:
        return await message.reply("❌ Balas pesan yang ingin dibroadcast ke grup.")
    
    done = 0
    failed = 0
    blacklist = await db.get_all()
    
    async for dialog in client.get_dialogs():
        if dialog.chat.type in ("group", "supergroup") and dialog.chat.id not in blacklist:
            try:
                await message.reply_to_message.copy(dialog.chat.id)
                done += 1
            except:
                failed += 1
    
    await message.reply(f"✅ Broadcast ke grup selesai.\nBerhasil: {done}, Gagal: {failed}")

@Client.on_message(filters.command("ucast", prefixes=".") & filters.me)
async def ucast(client, message):
    if not message.reply_to_message:
        return await message.reply("❌ Balas pesan yang ingin dibroadcast ke pesan pribadi.")
    
    done = 0
    failed = 0
    blacklist = await db.get_all()
    
    async for dialog in client.get_dialogs():
        if dialog.chat.type == "private" and dialog.chat.id not in blacklist:
            try:
                await message.reply_to_message.copy(dialog.chat.id)
                done += 1
            except:
                failed += 1
    
    await message.reply(f"✅ Broadcast ke pesan pribadi selesai.\nBerhasil: {done}, Gagal: {failed}")
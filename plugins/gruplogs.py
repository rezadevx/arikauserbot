from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from database.logs import LogDB
from datetime import datetime
import asyncio

logs = LogDB()

@Client.on_message(filters.command("gruplogs", prefixes=".") & filters.me)
async def enable_gruplogs(client, message):
    user_id = message.from_user.id
    current = await logs.get_log_group(user_id)
    if current:
        return await message.reply("✅ Gruplogs sudah aktif.")

    try:
        group = await client.create_supergroup("Arika Log " + str(user_id), "Grup log pribadi milik Anda.")
        await logs.set_log_group(user_id, group.id)
        await client.promote_chat_member(group.id, user_id, can_manage_chat=True)
        await client.set_chat_permissions(group.id, ChatPermissions(can_send_messages=True))
        await client.send_message(group.id, "✅ Gruplogs berhasil diaktifkan.")
        await message.reply("✅ Gruplogs sudah dibuat dan diaktifkan.")
    except Exception as e:
        await message.reply(f"❌ Gagal membuat gruplogs: {e}")

@Client.on_message(filters.private & ~filters.me)
async def log_private_message(client, message):
    owner = await client.get_me()
    log_id = await logs.get_log_group(owner.id)
    if not log_id:
        return

    try:
        jam = datetime.now().strftime("%H:%M")
        nama = message.from_user.first_name
        text = f"🥷 <b>Ada pesan masuk nih</b>\n\n<b>Dari</b>: {nama}\n<b>Isi</b>: {message.text or 'media'}\n<b>Jam</b>: {jam}"
        await client.send_message(log_id, text)
    except:
        pass

@Client.on_message(filters.group & ~filters.me)
async def log_tag_or_reply(client, message):
    owner = await client.get_me()
    log_id = await logs.get_log_group(owner.id)
    if not log_id:
        return

    is_reply = message.reply_to_message and message.reply_to_message.from_user and message.reply_to_message.from_user.id == owner.id
    is_mention = owner.username and f"@{owner.username}" in (message.text or "")

    if is_reply or is_mention:
        try:
            jam = datetime.now().strftime("%H:%M")
            sender = message.from_user.first_name
            text = f"📢 <b>Notifikasi Grup</b>\n\n<b>Dari</b>: {sender}\n<b>Isi</b>: {message.text or 'media'}\n<b>Jam</b>: {jam}"
            await client.send_message(log_id, text)
        except:
            pass
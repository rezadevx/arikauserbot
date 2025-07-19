from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Daftar plugin dan deskripsi
PLUGINS = {
    "ping": "📡 Cek latency, uptime, dan nama userbot.\n\nPerintah: <code>.ping</code>",
    "alive": "🔋 Menampilkan status userbot, uptime, dan ID.\n\nPerintah: <code>.alive</code>",
    "gcast": "📣 Broadcast ke semua grup.\n\nBalas pesan lalu ketik <code>.gcast</code>",
    "ucast": "📬 Broadcast ke semua PM.\n\nBalas pesan lalu ketik <code>.ucast</code>",
    "addbl": "🚫 Masukkan chat ini ke blacklist broadcast.\n\nPerintah: <code>.addbl</code>",
    "unbl": "✅ Hapus chat ini dari blacklist broadcast.\n\nPerintah: <code>.unbl</code>",
    "setprefix": "✏️ Ubah prefix untuk perintah.\n\nContoh: <code>.setprefix !</code>",
    "gruplogs": "🕵️‍♂️ Aktifkan gruplogs pribadi.\n\nPerintah: <code>.gruplogs on</code>",
}

# Keyboard dua tombol per baris
def build_plugin_keyboard():
    keys = list(PLUGINS.keys())
    keyboard = []
    for i in range(0, len(keys), 2):
        row = []
        for j in range(2):
            if i + j < len(keys):
                plugin = keys[i + j]
                row.append(InlineKeyboardButton(plugin, callback_data=f"help_{plugin}"))
        keyboard.append(row)
    return InlineKeyboardMarkup(keyboard)

# Tombol kembali
def back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Kembali", callback_data="help_back")]
    ])

@Client.on_message(filters.command("help", prefixes=".") & filters.me)
async def show_help_menu(client, message):
    await message.reply(
        "🧰 <b>Daftar Plugin Tersedia:</b>\nKlik tombol untuk melihat deskripsi.",
        reply_markup=build_plugin_keyboard()
    )

@Client.on_callback_query(filters.regex(r"^help_"))
async def help_callback(client: Client, cq: CallbackQuery):
    plugin = cq.data.split("_", 1)[1]

    if plugin == "back":
        await cq.message.edit(
            "🧰 <b>Daftar Plugin Tersedia:</b>\nKlik tombol untuk melihat deskripsi.",
            reply_markup=build_plugin_keyboard()
        )
    else:
        deskripsi = PLUGINS.get(plugin, "❌ Plugin tidak ditemukan.")
        await cq.message.edit(
            f"📦 <b>Plugin:</b> <code>{plugin}</code>\n\n{deskripsi}",
            reply_markup=back_keyboard()
        )
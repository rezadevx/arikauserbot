#!/bin/bash

echo "🚀 Menyalakan Arika Userbot..."

# Aktifkan virtual environment jika ada
if [ -d "venv" ]; then
  source venv/bin/activate
fi

# Jalankan bot
python3 main.py
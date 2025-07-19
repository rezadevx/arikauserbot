import os
from dotenv import load_dotenv

# Muat variabel dari file .env
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")
MONGO_URI = os.getenv("MONGO_URI")
from config import MONGO_URI
from motor.motor_asyncio import AsyncIOMotorClient

class PrefixDB:
    def __init__(self):
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.db = self.client["arika_userbot"]
        self.collection = self.db["prefixes"]

    async def set_prefix(self, user_id: int, prefix: str):
        await self.collection.update_one(
            {"_id": user_id},
            {"$set": {"prefix": prefix}},
            upsert=True
        )

    async def get_prefix(self, user_id: int):
        data = await self.collection.find_one({"_id": user_id})
        return data["prefix"] if data else "."
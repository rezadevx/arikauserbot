from config import MONGO_URI
from motor.motor_asyncio import AsyncIOMotorClient

class BlacklistDB:
    def __init__(self):
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.db = self.client["arika_userbot"]
        self.collection = self.db["blacklist"]

    async def add(self, user_id):
        await self.collection.update_one(
            {"_id": user_id},
            {"$set": {"_id": user_id}},
            upsert=True
        )

    async def remove(self, user_id):
        await self.collection.delete_one({"_id": user_id})

    async def is_blacklisted(self, user_id):
        return bool(await self.collection.find_one({"_id": user_id}))

    async def get_all(self):
        return [doc["_id"] async for doc in self.collection.find({})]
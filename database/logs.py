from config import MONGO_URI
from motor.motor_asyncio import AsyncIOMotorClient

class LogDB:
    def __init__(self):
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.db = self.client["arika_userbot"]
        self.collection = self.db["logs"]

    async def set_log_group(self, user_id: int, group_id: int):
        await self.collection.update_one(
            {"_id": user_id},
            {"$set": {"group_id": group_id}},
            upsert=True
        )

    async def get_log_group(self, user_id: int):
        data = await self.collection.find_one({"_id": user_id})
        return data["group_id"] if data else None
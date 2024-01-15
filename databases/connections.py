from typing import Any, List, Optional
from beanie import init_beanie, PydanticObjectId
from models.rooms import ROOM_DATA
from models.reviews import REVIEW_DATA
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
# 변경 후 코드
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    
    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(),
                          document_models=[ROOM_DATA, REVIEW_DATA])
    
    class Config:
        env_file = ".env"

class Database:
    # model = collection
    def __init__(self, model):
        self.model = model
        pass

    # 전체 리스트
    async def get_all(self):
        documents = await self.model.find_all().to_list()   # find({})
        pass
        return documents

    # 상세 보기
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)  # get = find_one
        if doc:
            return doc
        return False
    
    # 저장
    async def save(self, document) -> None:
        await document.create()
        return None
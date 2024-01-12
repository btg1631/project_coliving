from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class ROOM_DATA(Document):
    brand: Optional[str] = None
    local: Optional[str] = None
    title: Optional[str] = None
    image: Optional[str] = None
    room_type: Optional[str] = None
    room_size : Optional[str] = None
    text : Optional[str] = None
  
    class Settings:
        name = "ROOM_DATA"


from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class ROOM_DATA(Document):
    room_brand: Optional[str] = None
    room_local: Optional[str] = None
    room_title: Optional[str] = None
    room_image: Optional[str] = None
    room_room_type: Optional[str] = None
    room_room_size : Optional[str] = None
    room_text : Optional[str] = None
  
    class Settings:
        name = "ROOM_DATA"


from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class ROOM_DATA(Document):
    room_brand: Optional[str] = None
    room_local: Optional[str] = None    
    room_image: Optional[str] = None
    room_image_two: Optional[str] = None
    room_title: Optional[str] = None
    room_type: Optional[str] = None
    room_any: Optional[str] = None
    room_size : Optional[str] = None
    room_layout : Optional[str] = None
    room_option : Optional[str] = None
    room_default_option : Optional[str] = None
    room_note : Optional[str] = None
  
    class Settings:
        name = "ROOM_DATA"


from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class ENTER_ROOM_DATA(Document):
    address: Optional[str] = None
    dong_address : Optional[str] = None
    ho_address : Optional[str] = None
    price: Optional[str] = None
    # oner: Optional[str] = None
  
    class Settings:
        name = "ENTER_ROOM_DATA"


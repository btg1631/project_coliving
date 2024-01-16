from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class ENTER_USER_DATA(Document):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    phonenumber: Optional[str] = None
    enter_number : Optional[str] = None
  
    class Settings:
        name = "ENTER_USER_DATA"

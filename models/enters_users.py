from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class ENTER_USERS_DATA(Document):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    pswd: Optional[str] = None
    phonenumber: Optional[str] = None
    enter_number : Optional[str] = None
  
    class Settings:
        name = "ENTERS_USERS_DATA"


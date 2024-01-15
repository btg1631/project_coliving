from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class Enter(Document):
    enter_name: Optional[str] = None
    enter_email: Optional[EmailStr] = None
    enter_password: Optional[str] = None
    enter_phonenumber: Optional[str] = None
    sellist1 : Optional[str] = None
    text : Optional[str] = None
  
    class Settings:
        name = "ENTER_DATA"


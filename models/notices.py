from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class NOTICE_DATA(Document):
    notice_title: Optional[str] = None
    notice_text : Optional[str] = None

    class Settings:
        name = "NOTICE_DATA"

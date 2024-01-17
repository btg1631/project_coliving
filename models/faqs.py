from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class FAQ(Document):
    title: Optional[str] = None
    sellist : Optional[str] = None
    text : Optional[str] = None

    class Settings:
        name = "FAQ"

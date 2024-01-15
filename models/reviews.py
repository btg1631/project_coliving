from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class REVIEW_DATA(Document):
    review_title: Optional[str] = None
    review_content: Optional[str] = None
    review_image: Optional[str] = None

    class Settings:
        name = "REVIEW_DATA"


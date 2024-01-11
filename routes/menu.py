from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from beanie import init_beanie

# from toy.databases.connections import Database

# from toy.models.users import user
# collection_user = Database(user)

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

@router.get("/communities", response_class=HTMLResponse)
async def communities(request:Request):
    return templates.TemplateResponse(name="menu/communities.html", context={'request':request})

@router.get("/find_rooms", response_class=HTMLResponse) # 펑션 호출 방식
async def find_rooms(request:Request):
    return templates.TemplateResponse(name="menu/find_rooms.html", context={'request':request})

@router.get("/notices", response_class=HTMLResponse)
async def notices(request:Request):
    return templates.TemplateResponse(name="menu/notices.html", context={'request':request})

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

# 방 찾기
@router.get("/find_rooms", response_class=HTMLResponse) # 펑션 호출 방식
async def find_rooms(request:Request):
    search_dict = {'room_type': 'none', 'room_size': 'none', 'search': ''}
    return templates.TemplateResponse(name="room/find_rooms.html", context={'request':request, 'search_dict':search_dict})

# 방 찾기(검색 클릭시 선택한 옵션과 검색어에 대한 내용이 다음 페이지로 넘어가야함..) 
@router.post("/find_rooms")
async def find_rooms(request:Request):
    search_dict = dict(await request.form())
    print(search_dict)
    return templates.TemplateResponse(name="room/find_rooms.html", context={'request':request, 'search_dict':search_dict})


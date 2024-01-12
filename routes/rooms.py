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
from databases.connections import Database
from models.rooms import ROOM_DATA
collection_rooms = Database(ROOM_DATA)


# 방 찾기
@router.get("/find_rooms", response_class=HTMLResponse) # 펑션 호출 방식
async def find_rooms(request:Request):
    search_dict = {'room_type': 'none', 'room_size': 'none', 'search': ''}
    room_list = await collection_rooms.get_all()
    return templates.TemplateResponse(name="room/find_rooms.html", context={'request':request,
                                                                            'search_dict':search_dict,
                                                                            'rooms':room_list})

# 방 찾기(검색 클릭시 선택한 옵션과 검색어에 대한 내용이 다음 페이지로 넘어가야함..) 
@router.post("/find_rooms")
async def find_rooms(request:Request):
    search_dict = dict(await request.form())
    print(search_dict)
    # 여기서 get_all 말고 search_dict에 대한 필터링이 되어서 get해야함!!
    room_list = await collection_rooms.get_all()
    return templates.TemplateResponse(name="room/find_rooms.html", context={'request':request,
                                                                            'search_dict':search_dict,
                                                                            'rooms':room_list})


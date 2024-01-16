from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from beanie import init_beanie

from databases.connections import Database
from models.enters_rooms import ENTER_ROOM_DATA
collection_room_regist = Database(ENTER_ROOM_DATA)

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

#기업 매물등록 
@router.get("/enter_regists",response_class=HTMLResponse)
async def enter(request:Request):
    return templates.TemplateResponse(name="enter/enter_regists.html",context={'request':request})

#기업 관리자페이지
@router.get("/enter_manages",response_class=HTMLResponse)
async def enter(request:Request):
    return templates.TemplateResponse(name="enter/enter_manages.html",context={'request':request})

#기업 메인페이지
@router.post("/main_enters",response_class=HTMLResponse)
async def enter(request:Request):
    return templates.TemplateResponse(name="enter/main_enters.html",context={'request':request})

#기업 매물 DB 업로드
@router.post("/enter_regists")
async def enter_room_regist(request:Request):
    regist_dict = dict(await request.form())
    print(regist_dict)

    # 저장
    regist = ENTER_ROOM_DATA(**regist_dict)
    await collection_room_regist.save(regist)
    return templates.TemplateResponse(name="enter/main_enters.html",context={'request':request,'regist':regist})
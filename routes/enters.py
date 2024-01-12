from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from beanie import init_beanie

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

#기업 매물등록
@router.get("/enter_regist",response_class=HTMLResponse)
async def enter(request:Request):
    return templates.TemplateResponse(name="enter/enter_regist.html",context={'request':request})

#기업 관리자페이지
@router.get("/enter_manage",response_class=HTMLResponse)
async def enter(request:Request):
    return templates.TemplateResponse(name="enter/enter_manage.html",context={'request':request})
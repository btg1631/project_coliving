from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from beanie import init_beanie

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
@router.get("/main_enters",response_class=HTMLResponse)
async def enter(request:Request):
    return templates.TemplateResponse(name="enter/main_enters.html",context={'request':request})
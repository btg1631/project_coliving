from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from beanie import init_beanie

from databases.connections import Database
from models.qnas import QNA
collection_qna = Database(QNA)

# from toy.databases.connections import Database

# from toy.models.users import user
# collection_user = Database(user)

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

@router.get("/notices", response_class=HTMLResponse)
async def notices(request:Request):
    return templates.TemplateResponse(name="notice/notices.html", context={'request':request})

@router.get("/introductions", response_class=HTMLResponse)
async def introduction(request:Request):
    return templates.TemplateResponse(name="notice/introductions.html", context={'request':request})

# QNA 창으로 이동
@router.get("/qnas", response_class=HTMLResponse)
async def qna(request:Request):
    return templates.TemplateResponse(name="notice/qnas.html", context={'request':request})

# QNA 자세히 보기
@router.get("/qnas_details",response_class=HTMLResponse)
async def qna(request:Request):
    return templates.TemplateResponse(name="notice/qnas_details.html",context={'request':request})

# QNA 입력창으로 이동
@router.get("/qnas_inputs",response_class=HTMLResponse)
async def qna(request:Request):
    return templates.TemplateResponse(name="notice/qnas_inputs.html",context={'request':request})

# QNA DB 업로드
@router.get("/qnas_inputs",response_class=HTMLResponse)
async def qna(request:Request):
    qna_dict = dict(await request.form())
    print(qna_dict)

    return templates.TemplateResponse(name="notice/qnas.html",context={'request':request,'qna_dict':qna_dict})
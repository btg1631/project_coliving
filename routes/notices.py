from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from beanie import init_beanie

from databases.connections import Database
from models.notices import NOTICE_DATA
collection_notice = Database(NOTICE_DATA)
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
    notice_list = await collection_notice.get_all()
    return templates.TemplateResponse(name="notice/notices.html", context={'request':request,
                                                                           'notices':notice_list})
from beanie import PydanticObjectId
@router.get("/noticedetails/{object_id}", response_class=HTMLResponse)
async def notices(request:Request, object_id:PydanticObjectId):
    notice = await collection_notice.get(object_id)
    return templates.TemplateResponse(name="notice/notice_details.html", context={'request':request,
                                                                           'notice':notice})

@router.get("/introductions", response_class=HTMLResponse)
async def introduction(request:Request):
    return templates.TemplateResponse(name="notice/introductions.html", context={'request':request})

# QNA 창으로 이동
@router.get("/qnas", response_class=HTMLResponse)
async def qna(request:Request):
    qna_list = await collection_qna.get_all()
    print(qna_list)
    return templates.TemplateResponse(name="notice/qnas.html", context={'request':request,'qna':qna_list})

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
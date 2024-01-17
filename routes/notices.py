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

@router.get("/notices", response_class=HTMLResponse)
async def notices(request:Request):
    return templates.TemplateResponse(name="notice/notices.html", context={'request':request})

@router.get("/introductions", response_class=HTMLResponse)
async def introduction(request:Request):
    return templates.TemplateResponse(name="notice/introductions.html", context={'request':request})

@router.get("/faqs", response_class=HTMLResponse)
async def faq(request:Request):
    return templates.TemplateResponse(name="notice/faqs.html", context={'request':request})

@router.get("/faqs_details",response_class=HTMLResponse)
async def faq(request:Request):
    return templates.TemplateResponse(name="notice/faqs_details.html",context={'request':request})

@router.get("/faqs_inputs",response_class=HTMLResponse)
async def faq(request:Request):
    return templates.TemplateResponse(name="notice/faqs_inputs.html",context={'request':request})

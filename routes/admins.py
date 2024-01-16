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

@router.get("/admins", response_class=HTMLResponse)
async def admin(request:Request):
    return templates.TemplateResponse(name="admin/admins.html", context={'request':request})

@router.get("/adminusers", response_class=HTMLResponse)
async def adminusers(request:Request):
    return templates.TemplateResponse(name="admin/admin_users.html", context={'request':request})

@router.get("/adminnotices", response_class=HTMLResponse)
async def adminmotice(request:Request):
    return templates.TemplateResponse(name="admin/admin_notices.html", context={'request':request})

@router.get("/adminhouses", response_class=HTMLResponse)
async def adminhouse(request:Request):
    return templates.TemplateResponse(name="admin/admin_houses.html", context={'request':request})

@router.get("/adminfaqs", response_class=HTMLResponse)
async def adminfaq(request:Request):
    return templates.TemplateResponse(name="admin/admin_faqs.html", context={'request':request})

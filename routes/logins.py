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


@router.get("/logins", response_class=HTMLResponse)
async def communities(request:Request):
    return templates.TemplateResponse(name="login/logins.html", context={'request':request})

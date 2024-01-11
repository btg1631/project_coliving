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


@router.get("/communities", response_class=HTMLResponse)
async def communities(request:Request):
    return templates.TemplateResponse(name="community/communities.html", context={'request':request})

@router.get("/promotions", response_class=HTMLResponse)
async def promotion(request:Request):
    return templates.TemplateResponse(name="community/promotions.html", context={'request':request})

@router.get("/moveinreviews", response_class=HTMLResponse)
async def moveinreview(request:Request):
    return templates.TemplateResponse(name="community/moveinreviews.html", context={'request':request})

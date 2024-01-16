from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from beanie import init_beanie

from databases.connections import Database
from models.users import USER_DATA
from models.enters_users import ENTER_USER_DATA
collection_user = Database(USER_DATA)
collection_enter_user = Database(ENTER_USER_DATA)

router = APIRouter()
templates = Jinja2Templates(directory="templates/")

@router.get("/logins", response_class=HTMLResponse)
async def logins(request:Request):
    return templates.TemplateResponse(name="login/logins.html", context={'request':request})

@router.get("/usersignups", response_class=HTMLResponse)
async def usersignups(request:Request):
    return templates.TemplateResponse(name="login/user_sign_ups.html", context={'request':request})

# 일반회원 회원가입 정보 저장
@router.post("/usersignups", response_class=HTMLResponse)
async def usersignups(request:Request):
    user_dict = dict(await request.form())
    print(user_dict)
    # 저장
    users = USER_DATA(**user_dict)
    await collection_user.save(users)
    return templates.TemplateResponse(name="login/logins.html", context={'request':request})

@router.get("/entersignups", response_class=HTMLResponse)
async def entersignups(request:Request):
    return templates.TemplateResponse(name="login/enter_sign_ups.html", context={'request':request})

# 기업회원 회원가입 정보 저장
@router.post("/entersignups", response_class=HTMLResponse)
async def entersignups(request:Request):
    user_dict = dict(await request.form())
    print(user_dict)
    # 저장
    enter_users = ENTER_USER_DATA(**user_dict)
    await collection_enter_user.save(enter_users)
    return templates.TemplateResponse(name="login/logins.html", context={'request':request})




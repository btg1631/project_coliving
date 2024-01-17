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

@router.get("/admins", response_class=HTMLResponse)
async def admin(request:Request):
    return templates.TemplateResponse(name="admin/admins.html", context={'request':request})

@router.get("/adminusers", response_class=HTMLResponse)
async def adminusers(request:Request):
    user_dict = dict(request._query_params)
    print(user_dict)
    conditions = {}
    try :
        search_word = user_dict["word"]
    except:
        search_word = None
    if search_word:     # 검색어 작성
        conditions = { 'name' : { '$regex': user_dict["word"] }}

    message = "일치하는 검색 결과가 없습니다."
    user_list = await collection_user.getsbyconditions(conditions)
    return templates.TemplateResponse(name="admin/admin_users.html", context={'request':request
                                                                              , "message":message
                                                                              ,'users':user_list})

@router.get("/admin_enterusers", response_class=HTMLResponse)
async def admin_enterusers(request:Request):
    user_dict = dict(request._query_params)
    print(user_dict)
    conditions = {}
    try :
        search_word = user_dict["word"]
    except:
        search_word = None
    if search_word:     # 검색어 작성
        conditions = { 'name' : { '$regex': user_dict["word"] }}

    message = "일치하는 검색 결과가 없습니다."
    enter_user_list = await collection_enter_user.getsbyconditions(conditions)
    return templates.TemplateResponse(name="admin/admin_enter_users.html", context={'request':request
                                                                              , "message":message
                                                                              ,'users':enter_user_list})
from beanie import PydanticObjectId
# 일반회원 삭제
@router.get("/delete_user/{object_id}", response_class=HTMLResponse)
async def delete_user(request: Request, object_id:PydanticObjectId):
    await collection_user.delete_one(object_id)

    user_list = await collection_user.get_all()
    return templates.TemplateResponse(name="admin/admin_users.html", context={'request':request
                                                                              , 'users':user_list})

# 기업회원 삭제
@router.get("/delete_enter_user/{object_id}", response_class=HTMLResponse)
async def delete_enter_user(request: Request, object_id:PydanticObjectId):
    await collection_enter_user.delete_one(object_id)

    enter_user_list = await collection_enter_user.get_all()
    return templates.TemplateResponse(name="admin/admin_enter_users.html", context={'request':request
                                                                                    , 'users':enter_user_list})


@router.get("/adminnotices", response_class=HTMLResponse)
async def adminmotice(request:Request):
    return templates.TemplateResponse(name="admin/admin_notices.html", context={'request':request})

@router.get("/adminhouses", response_class=HTMLResponse)
async def adminhouse(request:Request):
    return templates.TemplateResponse(name="admin/admin_houses.html", context={'request':request})

@router.get("/adminfaqs", response_class=HTMLResponse)
async def adminfaq(request:Request):
    return templates.TemplateResponse(name="admin/admin_faqs.html", context={'request':request})

from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

# 회원 가입 form    /users/form
@router.post("/form", response_class=HTMLResponse) # 펑션 호출 방식
async def insert(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="users/inserts.html"
                                      , context={'request':request})

@router.get("/form", response_class=HTMLResponse) # 펑션 호출 방식
async def insert(request:Request):
    print(dict(request._query_params))
    return templates.TemplateResponse(name="users/inserts.html"
                                      , context={'request':request
                                                 , 'first' :5
                                                 , 'second':6})


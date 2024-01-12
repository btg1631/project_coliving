from fastapi import FastAPI

app = FastAPI()

from databases.connections import Settings
settings = Settings()
@app.on_event("startup")
async def init_db():
    await settings.initialize_database()

from fastapi.middleware.cors import CORSMiddleware
# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from routes.notices import router as notice_router
app.include_router(notice_router, prefix="/notice")
from routes.rooms import router as room_router
app.include_router(room_router, prefix="/room")
from routes.communities import router as community_router
app.include_router(community_router, prefix="/community")
from routes.admins import router as admin_router
app.include_router(admin_router, prefix="/admin")
from routes.logins import router as login_router
app.include_router(login_router, prefix="/login")
from routes.my_pages import router as mypage_router
app.include_router(mypage_router, prefix="/mypage")

from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app.mount("/css", StaticFiles(directory="templates\\css\\"), name="static_css")

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory = "templates/")
@app.get("/")
async def root(request:Request):

    return templates.TemplateResponse("main.html"
                                      , {'request':request})
@app.post("/")
async def root(request:Request):
    user_dict = dict(await request.form())
    print(user_dict)
    return templates.TemplateResponse("main.html"
                                      , {'request':request})

@app.get("/enter")
async def root(request:Request):

    return templates.TemplateResponse("main_enter.html"
                                      , {'request':request})

@app.post("/enter")
async def root(request:Request):
    user_dict = dict(await request.form())
    print(user_dict)
    return templates.TemplateResponse("main_enter.html"
                                      , {'request':request})

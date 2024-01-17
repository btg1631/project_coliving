from fastapi import FastAPI
from beanie import init_beanie

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
from routes.enters import router as enter_router
app.include_router(enter_router,prefix="/enter")

from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app.mount("/css", StaticFiles(directory="templates/css"), name="static_css")
app.mount("/images", StaticFiles(directory="images"), name="static_img")

from databases.connections import Database
from models.rooms import ROOM_DATA
from models.reviews import REVIEW_DATA
from models.enters_rooms import ENTER_ROOM_DATA

collection_rooms = Database(ROOM_DATA)
collection_reviews = Database(REVIEW_DATA)
collection_room_regist = Database(ENTER_ROOM_DATA)

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory = "templates/")
@app.get("/")
async def root(request:Request):
    room_list = await collection_rooms.get_all()
    review_list = await collection_reviews.get_all()
    room_list = room_list[:6]
    review_list = review_list[:4]
    return templates.TemplateResponse(name="main.html"
                                      , context={'request':request,
                                                  'rooms':room_list,
                                                  'reviews':review_list})
@app.post("/")
async def root(request:Request):
    user_dict = dict(await request.form())
    print(user_dict)
    room_list = await collection_rooms.get_all()
    review_list = await collection_reviews.get_all()
    room_list = room_list[:6]
    review_list = review_list[:4]
    return templates.TemplateResponse("main.html"
                                      , {'request':request,
                                         'rooms':room_list,
                                        'reviews':review_list})


@app.get("/enter")
async def root(request:Request):

    return templates.TemplateResponse("enter/main_enters.html"
                                      , {'request':request})

@app.post("/enter")
async def root(request:Request):
    user_dict = dict(await request.form())
    print(user_dict)
    regist_dict = dict(await request.form())
    print(regist_dict)

    # 저장
    regist = ENTER_ROOM_DATA(**regist_dict)
    await collection_room_regist.save(regist)
    return templates.TemplateResponse("enter/main_enters.html", {'request':request})


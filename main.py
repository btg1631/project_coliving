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


from routes.menu import router as menu_router
app.include_router(menu_router, prefix="/menu")

from fastapi import Request
from fastapi.templating import Jinja2Templates

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory = "templates/")
@app.get("/")
async def root(request:Request):

    return templates.TemplateResponse("main.html"
                                      , {'request':request})


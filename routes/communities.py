from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from beanie import init_beanie

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

from databases.connections import Database
from models.reviews import REVIEW_DATA
collection_review = Database(REVIEW_DATA)

@router.get("/communities", response_class=HTMLResponse)
async def communities(request:Request):
    return templates.TemplateResponse(name="community/communities.html", context={'request':request})

@router.get("/promotions", response_class=HTMLResponse)
async def promotion(request:Request):
    return templates.TemplateResponse(name="community/promotions.html", context={'request':request})

from typing import Optional
# 입주 리뷰 모두 보여주기
@router.get("/moveinreviews/{page_number}")
@router.get("/moveinreviews", response_class=HTMLResponse)
async def moveinreview(request:Request, page_number: Optional[int] = 1):
    user_dict = dict(request._query_params)
    print(user_dict)
    # db.answers.find({'name':{ '$regex': '김' }})
    # { 'name': { '$regex': user_dict.word } }
    conditions = { }
    try :
        search_word = user_dict["word"]
    except:
        search_word = None
    if search_word:     # 검색어 작성
        conditions = {'review_title' : { '$regex': user_dict["word"] }}
    # review_list = await collection_review.get_all()
    review_list, pagination = await collection_review.getsbyconditionswithpagination(conditions
                                                                     ,page_number)
    return templates.TemplateResponse(name="community/moveinreviews.html", context={'request':request,
                                                                                    'reviews':review_list,
                                                                                    'pagination' : pagination })
# 리뷰 특정 단어로 검색하기
@router.post("/searchmoveinreviews", response_class=HTMLResponse)
async def moveinreview(request:Request):
    search_dict = dict(await request.form())
    print(search_dict)
    return templates.TemplateResponse(name="community/moveinreviews.html", context={'request':request})

from beanie import PydanticObjectId
# 리뷰 상세보기
@router.get("/reviewdetails/{object_id}", response_class=HTMLResponse)
async def moveinreview(request:Request, object_id:PydanticObjectId):
    review = await collection_review.get(object_id)
    return templates.TemplateResponse(name="community/review_details.html", context={'request':request,
                                                                                     'review':review})
# 리뷰 쓰기(빈공간)
@router.get("/writereview", response_class=HTMLResponse)
async def moveinreview(request:Request):
    return templates.TemplateResponse(name="community/write_reviews.html", context={'request':request})

# 글작성 완료 후 db 저장
@router.post("/writereviewend", response_class=HTMLResponse)
async def writereviewend(request:Request):
    review_dict = dict(await request.form())
    print(review_dict)
    # 저장
    reviews = REVIEW_DATA(**review_dict)
    await collection_review.save(reviews)

    # review_list = await collection_review.get_all()
    return templates.TemplateResponse(name="community/review_details.html", context={'request':request,
                                                                                    'review':reviews})



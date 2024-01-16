# 웹 크롤링 동작      # 셀레니움에서 웹드라이버 임포트
from selenium import webdriver   # 셀레니움에서 웹드라이버 임포트
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
import time

# ChromeDriver 실행
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# 주소입력
browser.get("https://dears.kr/ko")
# browser2 = browser.get("https://mangrove.city/")

# 가능 여부에 대한 OK 받음
pass
# html 파일 받음(and 확인)
# html = browser.page_source
# print(html)

# 정보 회득
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
time.sleep(3)
# 팝업창 닫기 버튼 클릭
# body > div:nth-child(1) > main > div.fixed.left-1\/2.top-1\/2.z-\[106\].w-\[320px\].-translate-x-1\/2.-translate-y-1\/2.border.border-black.desktop\:max-h-\[447px\] > div > button:nth-child(2)
close = browser.find_element(by=By.CSS_SELECTOR, value="div > button:nth-child(2)>span")
close.click()

# 상품 하나 전체
# body > div:nth-child(1) > main > section:nth-child(5) > div > div > div.grid.grid-cols-2.gap-x-10.gap-y-\[80px\] > div:nth-child(1)

time.sleep(3)

# items = browser2.find_elements(by=By.CSS_SELECTOR, value= "div:nth-child(1)")
for x in range(1,4):
    items = browser.find_elements(by=By.CSS_SELECTOR,value="div.grid.grid-cols-2.gap-x-10.gap-y-\[80px\] > div:nth-child({})".format(x))
    element_item = browser.find_element(by=By.CSS_SELECTOR,value="h3.text-xl")
    print(element_item)


    # for i in range(len(items)):
    #     # 
        
    #     title = element_item.text

    # print("title : {}".format(title))

    
def connect_mongo() : 
    # mongodb compass 띄우기
    from pymongo import MongoClient
    # mongodb에 접속
    mongoClient = MongoClient("mongodb://192.168.10.10:27017")
    # database 연결
    database = mongoClient["project_coliving"]
    # collection 작업
    room_infor = database['ROOM_INFOR']
    # room_infor.delete_many({})
    return room_infor

time.sleep(3)
# iframe으로 전환(dears, mangrove)
# browser.switch_to.frame('iframe')
items = browser.find_elements(by=By.CSS_SELECTOR, value= "div:nth-child(1)")
for i in range(4):
    # 상품 하나 전체
    # body > div:nth-child(1) > main > section:nth-child(5) > div > div > div.grid.grid-cols-2.gap-x-10.gap-y-\[80px\] > div:nth-child(1)
    items = browser.find_elements(by=By.CSS_SELECTOR, value= "div:nth-child(1)")
    # items = browser2.find_elements(by=By.CSS_SELECTOR, value= "div:nth-child(1)")
    item = items[i]
    item.click()
    time.sleep(2)
    try:
        # dears 썸네일
        # div:nth-child(1) > div.relative.border.border-slate-200 > div.carousel-root > div > div > ul > li:nth-child(2) > div
        element_thumbnail_dears = browser.find_element(by=By.CSS_SELECTOR,value = "div > ul > li:nth-child(2) > div").text
    except NoSuchElementException:
        element_thumbnail_dears = "" 
    try:
        # dears 방 이름
        # div.flex.items-center.gap-x-4 > h3
        element_room_name_dears = browser.find_element(by=By.CSS_SELECTOR,value = "div.flex.items-center.gap-x-4 > h3")
    except NoSuchElementException:
        element_room_name_dears = ""
    try:
        # dears 방 구조 타입
        # div.mt-4.grid.gap-y-2.whitespace-pre-wrap.font-normal.leading-6.text-slate-800.desktop\:mt-5.desktop\:gap-y-2\.5.desktop\:text-lg > div > span
        element_room_type_dears = browser.find_element(by=By.CSS_SELECTOR,value = "div > span").text
    except NoSuchElementException:
        element_room_type_dears = ""
    try:
        # dears 거주인원/평수
        # div.mt-4.grid.gap-y-2.whitespace-pre-wrap.font-normal.leading-6.text-slate-800.desktop\:mt-5.desktop\:gap-y-2\.5.desktop\:text-lg > p:nth-child(2)
        element_numberOfResidenceAndPy = browser.find_element(by=By.CSS_SELECTOR,value = "p:nth-child(2)")
    except NoSuchElementException:
        element_numberOfResidenceAndPy= ""
    try:
        # dears 집 구성(e.g.방1,화장실1)
        # div.mt-4.grid.gap-y-2.whitespace-pre-wrap.font-normal.leading-6.text-slate-800.desktop\:mt-5.desktop\:gap-y-2\.5.desktop\:text-lg > p:nth-child(3)
        element_house_composition = browser.find_element(by=By.CSS_SELECTOR,value = "p:nth-child(3)")
    except NoSuchElementException:
        element_house_composition = ""
    try:
        # dears 세대 추가 옵션
        # div:nth-child(2) > div.mt-\[30px\].flex.flex-col.items-start.desktop\:mt-6 > div.mb-6.grid.gap-y-2.desktop\:gap-y-2\.5 > div
        element_additional_option = browser.find_element(by=By.CSS_SELECTOR,value = "div.mb-6.grid.gap-y-2.desktop\:gap-y-2\.5 > div")
    except NoSuchElementException:
        elemeelement_additional_optionnt_ = ""
    try:
        # dears 기본 옵션
        # div.mt-\[30px\].flex.flex-col.items-start.desktop\:mt-6 > div.mb-6.grid.gap-y-2.desktop\:gap-y-2\.5
        element_basic_option = browser.find_element(by=By.CSS_SELECTOR,value = "div.mb-6.grid.gap-y-2.desktop\:gap-y-2\.5")
    except NoSuchElementException:
        element_basic_option = ""
    try:
        # dears 월 이용료
        # div.flex.w-full.flex-col.items-center.justify-center.gap-1.bg-slate-50.px-5.pb-5.pt-\[16px\]
        element_feepermonth = browser.find_element(by=By.CSS_SELECTOR,value = "div.flex.w-full.flex-col.items-center.justify-center.gap-1.bg-slate-50.px-5.pb-5.pt-\[16px\]")
    except NoSuchElementException:
        element_feepermonth = ""
    try:
        # dears 비고(참고내용)
        # div:nth-child(5) > div.mt-\[30px\].flex.flex-col.items-start.desktop\:mt-6 > p
        element_reference = browser.find_element(by=By.CSS_SELECTOR,value = "div:nth-child(5) > div.mt-\[30px\].flex.flex-col.items-start.desktop\:mt-6 > p")
    except NoSuchElementException:
        element_reference = ""
    # try:
    #     # mangrove 썸네일
    #     # #wp-spaios-bxslider-2 > div:nth-child(2) > div > div
    #     element_thumbnail_mangrove = browser.find_element(by=By.CSS_SELECTOR,value = "#wp-spaios-bxslider-2 > div:nth-child(2) > div > div")
    # except NoSuchElementException:
    #     element_thumbnail_mangrove = ""
    # try:
    #     # mangrove 방 이름
    #     # div > div > h4
    #     element_room_name_mangrove = browser.find_element(by=By.CSS_SELECTOR,value = "")
    # except NoSuchElementException:
    #     element_room_name_mangrove = ""
    # try:
    #     # mangrove 방 구조 타입
    #     # div > div > table
    #     element_room_type_mangrove = browser.find_element(by=By.CSS_SELECTOR,value = "div > div > table")
    # except NoSuchElementException:
    #     element_room_type_mangrove = ""
    # try:
    #     # 포함사항
    #     # div.et_pb_column.et_pb_column_3_8.et_pb_column_inner.et_pb_column_inner_4 > div > div
    #     element_inclusion = browser.find_element(by=By.CSS_SELECTOR,value = "div.et_pb_column.et_pb_column_3_8.et_pb_column_inner.et_pb_column_inner_4 > div > div")
    # except NoSuchElementException:
    #     element_inclusion = ""

    # pass

    room_infor = connect_mongo()

    room_infor.insert_one({"dears 썸네일" : element_thumbnail_dears,
                                "dears 방 이름" : element_room_name_dears,
                                "dears 방 구조 타입" : element_room_type_dears,
                                "dears 거주인원/평수" : element_numberOfResidenceAndPy,
                                "dears 집 구성" : element_house_composition,
                                "dears 세대 추가 옵션" : element_additional_option,
                                "dears 기본 옵션" : element_basic_option,
                                "dears 월 이용료" : element_feepermonth,
                                "dears 비고" : element_reference})
                                # "mangrove 썸네일" : element_thumbnail_mangrove,
                                # "mangrove 방 이름" : element_room_name_mangrove,
                                # "mangrove 방 구조 타입" : element_room_type_mangrove,
                                # "포함사항" : element_inclusion})

    pass

    # browser.switch_to.frame('ifrmReview')                                                       # ifrmReview frame으로 변경
    # element_body = browser.find_element(by=By.CSS_SELECTOR,value="body")
    # previous_scrollHeight = 0                                                                   # 기본 브라우저 높이 변수 지정
    # time.sleep(3)

# 브라우저 종료
browser.quit()
pass
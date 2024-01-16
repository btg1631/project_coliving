# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# 몽고db 저장
from pymongo import MongoClient
# mongodb에 접속
mongoClient = MongoClient("mongodb://192.168.10.10:27017")
# database 연결
database = mongoClient["project_coliving"]
# collection 작업
room_infor = database['DEARS_PANGYO']

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities
from selenium.webdriver.common.by import By
# - 주소 입력
browser.get("https://dears.kr/ko")
time.sleep(2)
# 팝업 창 닫기 버튼 클릭
close = browser.find_element(by=By.CSS_SELECTOR, value="div > button:nth-child(2)>span")
close.click()
time.sleep(5)

# - 정보 획득

# 전체 상품 정보
selector_value = "div.grid.grid-cols-2.gap-x-10.gap-y-\[80px\] > div"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
for element_item in element_bundle[0:4]:
    try:
    # dears 썸네일
    # body > div:nth-child(1) > main > section:nth-child(5) > div > div > div.grid.grid-cols-2.gap-x-10.gap-y-\[80px\] > div:nth-child(1) > div.relative.border.border-slate-200
        element_image = browser.find_element(by=By.CSS_SELECTOR, value="div:nth-child(1) > div.relative.border.border-slate-200")
        image = element_image.get_attribute('src')
        # selector_value_thumbnail = "div:nth-child(1) > div.relative.border.border-slate-200"
        # element_thumbnail = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_thumbnail)
        # thumbnail = element_thumbnail.text
    except: 
        image = "None"
    time.sleep(2)

    # 상품 제목
    try:
        selector_value_title = "div.flex.items-center.gap-x-4 > h3"
        element_title = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_title)
        title = element_title.text
    except: 
        title = "None"
        
    # 방 구조 타입
    try:
        selector_value_room_type = "div > span"
        element_room_type = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_room_type)
        room_type = element_room_type.text
    except: 
        room_type = "None"

    # 기타(시설,세대옵션)
    # body > div:nth-child(1) > main > section:nth-child(5) > div > div > div.grid.grid-cols-2.gap-x-10.gap-y-\[80px\] > div:nth-child(4) > div.mt-\[30px\].flex.flex-col.items-start.desktop\:mt-6 > div.mt-4.grid.gap-y-2.whitespace-pre-wrap.font-normal.leading-6.text-slate-800.desktop\:mt-5.desktop\:gap-y-2\.5.desktop\:text-lg > div > div
    try:
        selector_value_household_option = "div.mt-4.grid.gap-y-2.whitespace-pre-wrap.font-normal.leading-6.text-slate-800.desktop\:mt-5.desktop\:gap-y-2\.5.desktop\:text-lg > div > div"
        element_household_option = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_household_option)
        household_option = element_household_option.text
    except: 
        household_option = "None"

    # 거주인원/평수
    try:
        selector_value_numberOfResidenceAndPy = "p:nth-child(2)"
        element_numberOfResidenceAndPy = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_numberOfResidenceAndPy)
        numberOfResidenceAndPy = element_numberOfResidenceAndPy.text
    except: 
        numberOfResidenceAndPy = "None"

    # 집 구성(e.g.방1,화장실1)
    try:
        selector_value_house_composition = "p:nth-child(3)"
        element_house_composition = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_house_composition)
        house_composition = element_house_composition.text
    except: 
        house_composition = "None"
        
    # 세대 추가 옵션
    try:
        selector_value_additional_option = "div.mb-6.grid.gap-y-2.desktop\:gap-y-2\.5 > div"
        element_additional_option = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_additional_option)
        additional_option = element_additional_option.text
    except: 
        additional_option = "None"
    
    # 기본 옵션
    try:
        selector_value_basic_option = "div.mb-6.grid.gap-y-2.desktop\:gap-y-2\.5"
        element_basic_option = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_basic_option)
        basic_option = element_basic_option.text
    except: 
        basic_option = "None"

    # 월 이용료(old price_정상가)
    try:
        # body > div:nth-child(1) > main > section:nth-child(5) > div > div > div.grid.grid-cols-2.gap-x-10.gap-y-\[80px\] > div:nth-child(1) > div.mt-\[30px\].flex.flex-col.items-start.desktop\:mt-6 > div.flex.w-full.flex-col.items-center.justify-center.gap-1.bg-slate-50.px-5.pb-5.pt-\[16px\] > div
        selector_value_old_price = "div.flex.w-full.flex-col.items-center.justify-center.gap-1.bg-slate-50.px-5.pb-5.pt-\[16px\] > div"
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_old_price)
        old_price = element_old_price.text
    except: 
        old_price = "None"

    # 월 이용료(new price_할인가)
    try:
        # body > div:nth-child(1) > main > section:nth-child(5) > div > div > div.grid.grid-cols-2.gap-x-10.gap-y-\[80px\] > div:nth-child(1) > div.mt-\[30px\].flex.flex-col.items-start.desktop\:mt-6 > div.flex.w-full.flex-col.items-center.justify-center.gap-1.bg-slate-50.px-5.pb-5.pt-\[16px\] > span
        selector_value_new_price = "div.flex.w-full.flex-col.items-center.justify-center.gap-1.bg-slate-50.px-5.pb-5.pt-\[16px\] > span"
        element_new_price = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_new_price)
        new_price = element_new_price.text
    except: 
        new_price = "None"

    # 비고(참고내용)
        # body > div:nth-child(1) > main > section:nth-child(5) > div > div > div.grid.grid-cols-2.gap-x-10.gap-y-\[80px\] > div:nth-child(1) > div.mt-\[30px\].flex.flex-col.items-start.desktop\:mt-6 > p
        # body > div:nth-child(1) > main > section:nth-child(5) > div > div > div.grid.grid-cols-2.gap-x-10.gap-y-\[80px\] > div:nth-child(4) > div.mt-\[30px\].flex.flex-col.items-start.desktop\:mt-6 > p
    try:
        selector_value_reference = "div.mt-\[30px\].flex.flex-col.items-start.desktop\:mt-6 > p"
        element_reference = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_reference)
        reference = element_reference.text
    except: 
        reference = "None"


    print("썸네일 : {}, 제목 : {}, 룸타입 : {}, 기타(시설,세대옵션) : {}, 거주인원/평수 : {}, 집 구성 : {}, 세대 추가 옵션 : {}, 기본 옵션 : {}, 월 이용 정상가 : {}, 월 이용 할인가 : {}, 비고 : {}".format(title, room_type, household_option, numberOfResidenceAndPy, house_composition, additional_option, basic_option, old_price, new_price, reference))
    room_infor.insert_one({"썸네일" : image
                            , "제목" : title
                            , "룸타입" : room_type
                            , "기타" : household_option
                            , "거주인원/평수" : numberOfResidenceAndPy
                            , "집 구성" : house_composition
                            , "세대 추가 옵션" : additional_option
                            , "기본 옵션" : basic_option
                            , "월 이용 정상가" : old_price
                            , "월 이용 할인가" : new_price
                            , "비고": reference})
    pass
pass

# 브라우저 종료
browser.quit()
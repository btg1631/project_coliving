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
# 썸네일 이미지
selector_images = "div.carousel-root > div > div > ul > li:nth-child(2) > div"
element_images = browser.find_elements(by=By.CSS_SELECTOR, value=selector_images)
for element_item in element_bundle[0:4]:
    for element_img in element_images[0:4]:    # 썸네일 이미지 4개 가져오기 범위 지정
        element_image = browser.find_element(by=By.CSS_SELECTOR, value="li:nth-child(2) > div > img")
        image = element_image.get_attribute('src')
        pass
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


    print("room_image : {}, room_title : {}, room_type : {}, room_any : {}, room_size : {}, room_layout : {}, room_option : {}, room_default_option : {}, room_price : {}, room_discounted_price : {}, room_note : {}".format(image, title, room_type, household_option, numberOfResidenceAndPy, house_composition, additional_option, basic_option, old_price, new_price, reference))
    room_infor.insert_one({"room_image" : image
                            , "room_title" : title
                            , "room_type" : room_type
                            , "room_any" : household_option
                            , "room_size" : numberOfResidenceAndPy
                            , "room_layout" : house_composition
                            , "room_option" : additional_option
                            , "room_default_option" : basic_option
                            , "room_price" : old_price
                            , "room_discounted_price" : new_price
                            , "room_note": reference})
    pass
pass

# 브라우저 종료
browser.quit()
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
room_infor = database['DEARS_MYEONGDONG']

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities
from selenium.webdriver.common.by import By

# - 주소 입력
browser.get("https://www.dearsmd.com/")
time.sleep(5)

# # 팝업 창(1,2,3) 닫기 버튼 클릭
# # body > div:nth-child(2) > form > span > a
# close_buttons = browser.find_elements(by=By.CSS_SELECTOR, value="div:nth-child(2) > form > span > a")
# for button in close_buttons:
#     button.click()
#     time.sleep(5)

# - 정보 획득

# 메뉴 - Rooms&Prices : #header > div.h_box.clearfix > ul > li:nth-child(3)
selector_element = 'div.h_box.clearfix > ul > li:nth-child(3)'
element_dears_menu = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)
time.sleep(1)
# 웹 요소 클릭
element_dears_menu.click()
time.sleep(2)

# 전체 상품 정보
for i in range(1, 4):
    selector_value = "div.roomR.inlineB > ul > li:nth-child({})".format(i)
    # #content > div.s_contents > div > div > div.roomR.inlineB > ul > li:nth-child(1)
    element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)

    # 썸네일 이미지 (룸 별 2개씩)
    selector_images_first = "ul > div.owl-stage-outer > div > div:nth-child(5)"
    selector_images_second = "ul > div.owl-stage-outer > div > div:nth-child(6)"
    element_images_first = browser.find_elements(by=By.CSS_SELECTOR, value=selector_images_first)
    element_images_second = browser.find_elements(by=By.CSS_SELECTOR, value=selector_images_second)
    for element_item in element_bundle:
        for element_img in element_images_first:
            element_image = element_img.find_element(by=By.CSS_SELECTOR, value=selector_images_first)
            image = element_image.get_attribute('src')
            pass
        time.sleep(2)
    for element_item in element_bundle:
        for element_img in element_images_second:
            element_image = element_img.find_element(by=By.CSS_SELECTOR, value=selector_images_second)
            image = element_image.get_attribute('src')
            pass
        time.sleep(2)

    # 상품 제목
    try:
        selector_value_title = "div.room_text > strong"
        element_title = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_title)
        title = element_title.text
    except:
        title = "None"

    # contents (층수/뷰/방구성/면적)
    #content > div.s_contents > div > div > div.roomR.inlineB > ul > li:nth-child(1) > div.room_text > p
    try :
        selector_value_contents = "div.room_text > p"
        element_contents = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_contents)
        contents = element_contents.text
    except :
        contents = "None"

    print("room_image_one : {}, room_image_two : {}, room_title : {}, room_contents : {}".format(element_images_first, element_images_second, title, contents))
    room_infor.insert_one({"room_image_one" : element_images_first
                           , "room_image_two" : element_images_second
                            ,"room_title" : title
                            ,"room_contents" : contents})
    pass
pass

# 브라우저 종료
browser.quit()
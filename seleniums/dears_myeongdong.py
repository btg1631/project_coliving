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

# 썸네일 이미지 (룸 별 2개씩)
# selector_images = "ul > div.owl-stage-outer > div > div.owl-item.active > li"
# element_images = browser.find_elements(by=By.CSS_SELECTOR, value=selector_images)
# 두 번째 이미지 : https://www.dearsmd.com/images/sub/room_img01_2.png
# #content > div.s_contents > div > div > div.roomR.inlineB > ul > li:nth-child(1) > ul > div.owl-stage-outer > div > div.owl-item.active
# selector_second_images = "div.owl-stage-outer > div > div.owl-item.active"
# element_second_images = browser.find_elements(by=By.CSS_SELECTOR, value=selector_second_images)
# for element_item in element_bundle:
#     for element_img in element_images:
#         element_image = browser.find_element(by=By.CSS_SELECTOR, value="div.owl-item.active > li > img")
#         image = element_image.get_attribute('src')
#     pass
#     for element_second_item in element_bundle:
#         for element_second_img in element_second_images:
#             element_second_image = browser.find_element(by=By.CSS_SELECTOR, value="div.owl-stage-outer > div > div.owl-item.active")
#             #content > div.s_contents > div > div > div.roomR.inlineB > ul > li:nth-child(1) > ul > div.owl-stage-outer > div > div.owl-item.active
#             second_image = element_second_image.get_attribute('src')
#         pass
#     time.sleep(2)
# for element_item in element_bundle:
for i in range(1, 4):
    selector_value = "div.roomR.inlineB > ul > li:nth-child({})".format(i)
    element_item = browser.find_element(by=By.CSS_SELECTOR, value=selector_value)
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

    # 썸네일 이미지 (룸 별 2개씩)
    selector_images = "ul > div.owl-stage-outer > div > div:nth-child(5)"
    selector_images = "ul > div.owl-stage-outer > div > div:nth-child(6)"
    element_images = element_item.find_elements(by=By.CSS_SELECTOR, value=selector_images)

    print("room_image : {}, room_title : {}, room_contents : {}".format(images, title, contents))
    room_infor.insert_one({"room_image" : images
                            ,"room_title" : title
                            ,"room_contents" : contents})
    pass
pass

# 브라우저 종료
browser.quit()
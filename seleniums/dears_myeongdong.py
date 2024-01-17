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

selector_value = "div.roomR.inlineB > ul > li"
# #content > div.s_contents > div > div > div.roomR.inlineB > ul > li:nth-child(1)
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)

# 전체 상품 정보
for element_item in element_bundle:
    # 상품 제목
    try:
        selector_value_title = "div.room_text > strong"
        element_title = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_title)
        title = element_title.text
    except:
        title = "None"
    # 이미지 1
    try:
        element_images_first = "div:nth-child(5) > li > img"
        element_image1 = element_item.find_element(by=By.CSS_SELECTOR, value=element_images_first)
        image1 = element_image1.get_attribute('src')
    except:
        image1 = "None"
    # 이미지 2
    try:
        element_images_second = "div:nth-child(6) > li > img"
        element_image2 = element_item.find_element(by=By.CSS_SELECTOR, value=element_images_second)
        image2 = element_image2.get_attribute('src')
    except:
        image2 = "None"

    # contents (층수/뷰/방구성/면적)
    #content > div.s_contents > div > div > div.roomR.inlineB > ul > li:nth-child(1) > div.room_text > p
    #content > div.s_contents > div > div > div.roomR.inlineB > ul > li > div.room_text > p
    try :
        selector_value_contents = "div.room_text > p"
        element_contents = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_contents)
        contents = element_contents.text
    except :
        contents = "None"

    print("room_image_one : {}, room_image_two:{}, room_title:{}, room_contents : {}".format(image1, image2, title, contents))
    room_infor.insert_one({"room_image_one" : image1
                            , "room_image_two" : image2
                            , "room_title" : title
                            , "room_contents" : contents})
    pass
# ------------------------------------------------------------------------------------------------------------------------
# Rooms - Stay L 클릭
selector_stayl = '#content > ul > li.on > a'
element_move_stayl = browser.find_element(by=By.CSS_SELECTOR, value=selector_stayl)
time.sleep(3)
element_move_stayl.click()
# browser.execute_script("arguments[0].click();", element_move_stayl)
time.sleep(2)

selector_value_stayl = "div > div.roomR.inlineB > ul > li"
element_bundle_stayl = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value_stayl)

# 전체 상품 정보
for element_item_stayl in element_bundle_stayl:
    # 상품 제목
    try:
        selector_value_title_stayl = "div.room_text > strong"
        element_title_stayl = element_item_stayl.find_element(by=By.CSS_SELECTOR, value=selector_value_title_stayl)
        title_stayl = element_title_stayl.text
    except:
        title_stayl = "None"
    # 이미지 1
    try:
        element_images_first_stayl = "div:nth-child(4) > li > img"
        element_image1_stayl = element_item_stayl.find_element(by=By.CSS_SELECTOR, value=element_images_first_stayl)
        image1_stayl = element_image1_stayl.get_attribute('src')
    except:
        image1_stayl = "None"
    # 이미지 2
    try:
        element_images_second_stayl = "div:nth-child(5) > li > img"
        element_image2_stayl = element_item_stayl.find_element(by=By.CSS_SELECTOR, value=element_images_second_stayl)
        image2_stayl = element_image2_stayl.get_attribute('src')
    except:
        image2_stayl = "None"

    # contents (층수/뷰/방구성/면적)
    try :
        selector_value_contents_stayl = "div.room_text > p"
        element_contents_stayl = element_item_stayl.find_element(by=By.CSS_SELECTOR, value=selector_value_contents_stayl)
        contents_stayl = element_contents_stayl.text
    except :
        contents_stayl = "None"

    print("room_image_one : {}, room_image_two:{}, room_title:{}, room_contents : {}".format(image1_stayl, image2_stayl, title_stayl, contents_stayl))
    room_infor.insert_one({"room_image_one" : image1_stayl
                            , "room_image_two" : image2_stayl
                            , "room_title" : title_stayl
                            , "room_contents" : contents_stayl})
    pass

pass

# 브라우저 종료
browser.quit()
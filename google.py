from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
#검색창 찾기
elem = driver.find_element_by_name("q")
# 검색어 입력 - 유동
elem.send_keys("pycon")
# 엔터키
elem.send_keys(Keys.RETURN)

# 스크롤을 먼저 다 내린다
SCROLL_PAUSE_TIME = 1.0

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page 스크롤 내리고 로딩 되는 동안 대기
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height 이전 높이와 다음 높이가 같다면 스탑
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try: # 더보기 버튼 클릭
            driver.find_element_by_css_selector("input.mye4qd").click()
        except:
            break
    last_height = new_height

# 사진 선택
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        src = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")
        urllib.request.urlretrieve(src, str(count) + ".jpg")
        count += 1
    except:
        pass
#
driver.close()

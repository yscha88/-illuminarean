from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

short_cut_sleep = 0.3 # debug를 위해서 눈으로 확인해야 할 때 설정하는 값, default == 0

# web_driver 초기 환경 설정
url = "https://illuminarean.com/"
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080) # 테스트 환경에 따라서 size 조절

# 웹 사이트 접속
driver.get(url)

# 인재풀 등록 모달 팝업 확인 및 닫기, 없으면 닫기 동작 부시
var_welcom_popup = "body > div.ReactModalPortal > div > div > div"
var_welcom_popup_button_close = "/html/body/div[4]/div/div/div/div/button[2]"
if driver.find_element(By.CSS_SELECTOR, var_welcom_popup).is_enabled():
    driver.find_element(By.XPATH, var_welcom_popup_button_close).click()
sleep(short_cut_sleep)

# 네비게이션바가 존재하는지 확인
navigation = driver.find_elements(By.TAG_NAME, "nav")
assert len(navigation) == 1

# 네이게이션바에 메뉴가 4개 미만인지 확인, "work" 메뉴를 클릭
for nav_item in navigation[0].find_elements(By.TAG_NAME, "a"):
    count = 0
    try:
        if str(nav_item.text).lower().find("work") > -1:
            nav_item.click()
        else:
            count += 1
    except:
        assert count <= 4
sleep(short_cut_sleep)

# GOODVIBE WORKS 바로가기 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div[2]/div/div[3]/div/a').click()

# 새 탭에서 열리므로 핸들링 포커싱을 다음 팝업으로 변경
driver.switch_to.window(driver.window_handles[1])
sleep(short_cut_sleep)

# 무료 체험 신청 버튼 (상단에 1개, 하단에 1개 존재함)
button1 = "#fullpage > div.section.css-29ulp9.e1ph4usi9.fp-section.active.fp-table.fp-completely > div > div > div:nth-child(2) > button"
button2 = "#fullpage > div.section.fp-auto-height.css-143pacz.e1ph4usi0.fp-section.fp-table.active.fp-completely > div > div.css-1nq33sk.e49wrg10 > button"

# 각 버튼으로 열리는 메뉴의 class가 동일한지 보장할 수 없다고 가정, 동일한 동작인지 체크
# 버튼 1번 테스트
driver.find_element(By.CSS_SELECTOR, button1).click()
sleep(short_cut_sleep)

table = driver.find_element(By.CSS_SELECTOR, "body > div.ReactModalPortal > div > div > div > div > div > div > div > div.css-1c95w5k.e1oaq22c4").find_elements(By.TAG_NAME, "dl")
for row in table:
    title = row.find_element(By.TAG_NAME, "dt")
    description = row.find_element(By.TAG_NAME, "dd")
    match title.text:
        case "회사명":
            description.find_element(By.TAG_NAME, "input").send_keys("모노리스")
            # assert description.text == "모노리스"
            sleep(short_cut_sleep)

        case "대표자명":
            description.click()
            description.find_element(By.TAG_NAME, "input").send_keys("김종석, 김나영")
            # assert description.text == "김종석, 김나영"
            sleep(short_cut_sleep)

        case "사업자유형":
            pass

        case "직원수":
            description.click()
            description.find_element(By.TAG_NAME, "input").send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER)
            sleep(short_cut_sleep)

            # assert description.text == "201-500 명"
        case "담당자명":
            description.find_element(By.TAG_NAME, "input").send_keys("차요셉")
            sleep(short_cut_sleep)

            # assert description.text == "차요셉"
        case "이메일":
            description.find_element(By.TAG_NAME, "input").send_keys("ys.cha@gmail.com")
            sleep(short_cut_sleep)

            # assert description.text == "ys.cha@gmail.com"
        case "휴대폰 번호":
            description.find_element(By.TAG_NAME, "input").send_keys("010-5649-0669")
            sleep(short_cut_sleep)

            # assert description.text == "010-5649-0669"
        case "담당 업무":
            description.click()
            jobs = driver.find_element(By.CSS_SELECTOR, "body > div.ReactModalPortal > div > div > div > div > div > div > div > div.css-1c95w5k.e1oaq22c4 > dl.duties > dd > div > div.css-y10ynn.el0tj999 > div > div.css-s0v51g.el0tj995").find_elements(By.TAG_NAME, "button")
            jobs_name = list(map(lambda x: x.text, jobs))
            sleep(short_cut_sleep)

            random_1 = random.randrange(0, len(jobs_name))
            select_1 = jobs_name[random_1]
            jobs_name.pop(random_1)
            for job in jobs:
                if job.text == select_1:
                    job.click()
            sleep(short_cut_sleep)

            random_2 = random.randrange(0, len(jobs_name))
            select_2 = jobs_name[random_2]
            description.find_element(By.TAG_NAME, "input").send_keys(select_2, Keys.ENTER)
            for job in jobs:
                if job.text == select_2:
                    job.click()
            sleep(short_cut_sleep)

            description.find_element(By.CSS_SELECTOR, "body > div.ReactModalPortal > div > div > div > div > div > div > div > div.css-1c95w5k.e1oaq22c4 > dl.duties > dd > div > div.css-y10ynn.el0tj999 > div > div.css-1bfxy5v.el0tj994 > button:nth-child(2)").click()
            sleep(short_cut_sleep)

terms = driver.find_element(By.CSS_SELECTOR, "body > div.ReactModalPortal > div > div > div > div > div > div > div > div.css-1c95w5k.e1oaq22c4 > div").find_elements(By.TAG_NAME, "label")
assert len(terms) == 2
sleep(short_cut_sleep)

driver.find_element(By.CSS_SELECTOR, "body > div.ReactModalPortal > div > div > div > div > div > div > div > div.css-1c95w5k.e1oaq22c4 > div > div:nth-child(1) > label > span > div").click()
sleep(short_cut_sleep)

driver.find_element(By.CSS_SELECTOR, "body > div.ReactModalPortal > div > div > div > div > div > div > div > div.css-1c95w5k.e1oaq22c4 > div > div:nth-child(2) > label > span > div").click()
sleep(short_cut_sleep)


driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(10) > button").click()
sleep(short_cut_sleep)

driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(12) > div > div > div > div > div > div > button:nth-child(2)").click()
sleep(short_cut_sleep)


# 두번째 버튼 테스트
_flag = 0
while True:
    try:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        driver.implicitly_wait(3)
        driver.find_element(By.CSS_SELECTOR, button2).click()
        sleep(short_cut_sleep)
        break
    except:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        driver.implicitly_wait(3)
        _flag += 1
    finally:
        if _flag > 4:
            raise Exception("무료 체험 신청 버튼을 찾을 수 없습니다.")

assert True
# 중복 테스트는 생략..

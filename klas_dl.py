import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pages_list = [
    "https://klas.kw.ac.kr/std/lis/evltn/OnlineCntntsStdPage.do", #온라인 컨텐츠
    "https://klas.kw.ac.kr/std/lis/evltn/PrjctStdPage.do", #팀플
    "https://klas.kw.ac.kr/std/lis/evltn/OnlineTestStdPage.do", #온라인 시험
    "https://klas.kw.ac.kr/std/lis/sport/QustnrStdPage.do", #설문
    "https://klas.kw.ac.kr/std/lis/evltn/DscsnStdPage.do", #토론
    "https://klas.kw.ac.kr/std/lis/evltn/TaskStdPage.do", #과제
    "https://klas.kw.ac.kr/std/lis/evltn/AnytmQuizStdPage.do", #퀴즈
    "https://klas.kw.ac.kr/std/lis/sport/6972896bfe72408eb72926780e85d041/BoardListStdPage.do", #강의자료실
    "https://klas.kw.ac.kr/std/lis/sport/d052b8f845784c639f036b102fdc3023/BoardListStdPage.do" #공지사항
]
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome(options=options)  # 크롬드라이버 경로

def klas_dl(myID, myPW):
    url_login = "https://klas.kw.ac.kr/" #KLAS 로그인 페이지 주소
    driver.get(url_login)

    #로그인
    driver.find_element(By.ID, 'loginId').send_keys(myID)
    driver.find_element(By.ID, 'loginPwd').send_keys(myPW)
    driver.find_element(By.CLASS_NAME, 'btn').click()

    time.sleep(1)

    #강의자료==========================================================================================
    url = pages_list[7]
    driver.get(url)
    time.sleep(2)

#     # 학기 선택
#     semester_dropdown = driver.find_element(By.NAME, "selectYearhakgi")
#     select_semester = Select(semester_dropdown)
#     select_semester.select_by_index(1)
#     time.sleep(2)

    # 강의 선택
    subj_dropdown = driver.find_element(By.NAME, "selectSubj")
    select_subj = Select(subj_dropdown)
    print(select_subj.options)
    total_table = []

    count_subj = len(select_subj.options)
    for i in range(0, count_subj):  # 모든 강의 순회하면서 내용 조회
        subj_dropdown = driver.find_element(By.NAME, "selectSubj")
        select_subj = Select(subj_dropdown)
        select_subj.select_by_index(i)
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        lists = soup.select('#appModule > tbody')
        table = driver.find_element(By.XPATH, "//*[@id='appModule']/table/tbody")
        try:
            driver.find_element(By.CSS_SELECTOR, "#appModule > table > tbody > tr:nth-child(1) > td.lft").click()
            time.sleep(1.5)
            driver.find_element(By.CSS_SELECTOR, "#appModule > div.board_view > div:nth-child(2) > div > a").click()
            time.sleep(1.5)
            driver.back()
        except:
            pass
    time.sleep(2)
    driver.quit()


klas_dl(sys.argv[1],sys.argv[2])

import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('chromedriver.exe')  # 크롬드라이버 경로
pages_list = [
    "https://klas.kw.ac.kr/std/lis/evltn/OnlineCntntsStdPage.do", #온라인 컨텐츠
    "https://klas.kw.ac.kr/std/lis/evltn/PrjctStdPage.do", #팀플
    "https://klas.kw.ac.kr/std/lis/evltn/OnlineTestStdPage.do", #온라인 시험
    "https://klas.kw.ac.kr/std/lis/sport/QustnrStdPage.do", #설문
    "https://klas.kw.ac.kr/std/lis/evltn/DscsnStdPage.do", #토론
    "https://klas.kw.ac.kr/std/lis/evltn/TaskStdPage.do", #과제
    "https://klas.kw.ac.kr/std/lis/evltn/AnytmQuizStdPage.do", #퀴즈
]
def klas_login(myID, myPW):
    url_login = "https://klas.kw.ac.kr/" #KLAS 로그인 페이지 주소
    driver.get(url_login)

    #로그인
    driver.find_element(By.ID, 'loginId').send_keys(myID)
    driver.find_element(By.ID, 'loginPwd').send_keys(myPW)
    driver.find_element(By.CLASS_NAME, 'btn').click()

    time.sleep(3)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def accessOC():
    url = pages_list[0]
    driver.get(url)
    time.sleep(3)

    #학기 선택
    semester_dropdown = driver.find_element(By.NAME, "selectYearhakgi")
    select_semester = Select(semester_dropdown)
    select_semester.select_by_index(1)
    time.sleep(3)

    #강의 선택
    subj_dropdown = driver.find_element(By.NAME, "selectSubj")
    select_subj = Select(subj_dropdown)

    count_subj = len(select_subj.options)
    #첫번째 강의의 셀렉터:
    # prjctList > tbody > tr:nth-child(2) > td.lft
    #내용 비교가 아니라, prjctList의 전체 테이블의 tr 태그 개수를 비교해야
    for i in range(0,count_subj): # 모든 강의 순회하면서 내용 조회
        select_subj.select_by_index(i)
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        lists = soup.select('#prjctList > tbody')
        with open(os.path.join(BASE_DIR, 'a.txt'), 'w+') as f:
            f.write(lists[0].text.strip())
        # for l in lists:
        #     print(l.text.strip())

    # 내용의 업데이트 판별: latest.txt를 만들어, 내용이 같은지 확인

    # select_subj.select_by_index(1)
    # time.sleep(3)
    #
    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')

    # lists = soup.select('#prjctList > tbody')
    # for l in lists:
    #     print(l.text.strip())

def accessQZ():
    url = pages_list[6]
    driver.get(url)
    time.sleep(3)

    # 학기 선택
    semester_dropdown = driver.find_element(By.NAME, "selectYearhakgi")
    select_semester = Select(semester_dropdown)
    select_semester.select_by_index(1)
    time.sleep(3)

    # 강의 선택
    subj_dropdown = driver.find_element(By.NAME, "selectSubj")
    select_subj = Select(subj_dropdown)

    count_subj = len(select_subj.options)
    # 첫번째 강의의 셀렉터:
    # prjctList > tbody > tr:nth-child(2) > td.lft
    # 내용 비교가 아니라, prjctList의 전체 테이블의 tr 태그 개수를 비교해야
    for i in range(0, count_subj):  # 모든 강의 순회하면서 내용 조회
        select_subj.select_by_index(i)
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        lists = soup.select('#prjctList > tbody')
        with open(os.path.join(BASE_DIR, 'a.txt'), 'w+') as f:
            f.write(lists[0].text.strip())
        # for l in lists:
        #     print(l.text.strip())
if __name__ == '__main__':
    klas_login(myID, myPW)
    accessOC()

    # list_subj = soup.select('#appSelectSubj > div.col-md-7 > div > div.col-9 > select')
    # print('갯수: ',len(list_subj))
    #
    # for i in list_subj:
    #     print(i.text.strip())

import os
import time
import sys
from bs4 import BeautifulSoup
#Selenium ver 4.9.1 주의, 4.10.0 부터 옵션 오류
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

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
    "https://klas.kw.ac.kr/std/lis/sport/d052b8f845784c639f036b102fdc3023/BoardListStdPage.do"  # 공지사항
]
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)  # 크롬드라이버 경로
# 전체 리스트 담을 테이블
total_table = []

def klas_eve(myID, myPW):
    url_login = "https://klas.kw.ac.kr/" #KLAS 로그인 페이지 주소
    driver.get(url_login)

    #로그인
    driver.find_element(By.ID, 'loginId').send_keys(myID)
    driver.find_element(By.ID, 'loginPwd').send_keys(myPW)
    driver.find_element(By.CLASS_NAME, 'btn').click()

    time.sleep(2)

    # 공지사항==========================================================================================
    url = pages_list[8]
    driver.get(url)
    time.sleep(2)

    # # 학기 선택
    # semester_dropdown = driver.find_element(By.NAME, "selectYearhakgi")
    # select_semester = Select(semester_dropdown)
    # select_semester.select_by_index(1)
    # time.sleep(2)

    # 강의 선택
    subj_dropdown = driver.find_element(By.NAME, "selectSubj")
    select_subj = Select(subj_dropdown)


    count_subj = len(select_subj.options)
    for i in range(0, count_subj):  # 모든 강의 순회하면서 내용 조회
        select_subj.select_by_index(i)
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        table = driver.find_element(By.XPATH, "//*[@id='appModule']/table/tbody")
        try:
            tr = table.find_elements(By.TAG_NAME, "tr")
            for j in range(0, len(tr)):
                total_table.append(
                    select_subj.options[i].text.strip() + ', ' + tr[j].find_element(By.CLASS_NAME, "lft").text.strip())
        except:
            pass

    #온라인 클래스==========================================================================================
    url = pages_list[0]
    driver.get(url)
    time.sleep(2)

    # 학기 선택
    # semester_dropdown = driver.find_element(By.NAME, "selectYearhakgi")
    # select_semester = Select(semester_dropdown)
    # select_semester.select_by_index(1)
    # time.sleep(2)

    # 강의 선택
    subj_dropdown = driver.find_element(By.NAME, "selectSubj")
    select_subj = Select(subj_dropdown)

    # 전체 강의 리스트 담을 테이블

    count_subj = len(select_subj.options)
    for i in range(0, count_subj):  # 모든 강의 순회하면서 내용 조회
        select_subj.select_by_index(i)
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        lists = soup.select('#prjctList > tbody')

        table = driver.find_element(By.XPATH, "//*[@id='prjctList']/tbody")
        try:
            tr = table.find_elements(By.TAG_NAME, "tr")
            for j in range(0, len(tr)):
                total_table.append(
                    select_subj.options[i].text.strip() + ', ' + tr[j].find_element(By.CLASS_NAME, "lft").text.strip())
        except:
            pass

    #퀴즈 ===============================================================================================
    url = pages_list[6]
    driver.get(url)
    time.sleep(2)

    # 학기 선택
    # semester_dropdown = driver.find_element(By.NAME, "selectYearhakgi")
    # select_semester = Select(semester_dropdown)
    # select_semester.select_by_index(1)
    # time.sleep(2)

    # 강의 선택
    subj_dropdown = driver.find_element(By.NAME, "selectSubj")
    select_subj = Select(subj_dropdown)

    # 전체 퀴즈 리스트 담을 테이블

    count_subj = len(select_subj.options)
    for i in range(0, count_subj):  # 모든 강의 순회하면서 내용 조회
        # print("과목명: ",select_subj.options[i].text.strip())
        select_subj.select_by_index(i)
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        lists = soup.select('#prjctList > tbody')

        table = driver.find_element(By.XPATH, "//*[@id='prjctList']/tbody")
        try:
            tr = table.find_elements(By.TAG_NAME, "tr")
            for j in range(0, len(tr)):
                total_table.append(
                    select_subj.options[i].text.strip() + ', ' + tr[j].find_element(By.CLASS_NAME, "lft").text.strip())
        except:
            pass

    #과제========================================================================================================
    url = pages_list[5]
    driver.get(url)
    time.sleep(2)

    # 학기 선택
    # semester_dropdown = driver.find_element(By.NAME, "selectYearhakgi")
    # select_semester = Select(semester_dropdown)
    # select_semester.select_by_index(1)
    # time.sleep(2)

    # 강의 선택
    subj_dropdown = driver.find_element(By.NAME, "selectSubj")
    select_subj = Select(subj_dropdown)

    #전체 과제 리스트 담을 테이블

    count_subj = len(select_subj.options)
    for i in range(0,count_subj): # 모든 강의 순회하면서 내용 조회
        # print("과목명: ",select_subj.options[i].text.strip())
        select_subj.select_by_index(i)
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        lists = soup.select('#prjctList > tbody')
        table = driver.find_element(By.XPATH, "//*[ @ id = 'appModule'] /div/div[3]/ table")
        try:
            tr = table.find_elements(By.TAG_NAME, "tbody")
            for j in range(0, len(tr)):
                total_table.append(select_subj.options[i].text.strip() +', '+ tr[j].find_element(By.CLASS_NAME,"lft").text.strip())
        except:
            pass

# 최초 실행시에 f_read 이 부분 주석처리하고 실행해주세요, print(status) 까지요
    with open(os.path.join(BASE_DIR, 'latest_table.txt'), 'r+', encoding = 'utf-8') as f_read:
        #다른 점 있으면 0, 없으면 1 print
        status = 1
        for i in range(0, len(total_table)):
            temp = f_read.readline()
            if(total_table[i].strip()  == temp.strip()):
                status = 1
            else:
                status = 0
                break
        f_read.close()
        print(status)
# 여기까지요
    with open(os.path.join(BASE_DIR, 'latest_table.txt'), 'w+', encoding = 'utf-8') as f_write:
        for k in total_table:
            f_write.write(k+'\n')
        f_write.close()
    driver.quit()
klas_eve(sys.argv[1],sys.argv[2])

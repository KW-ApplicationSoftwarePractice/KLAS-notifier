import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pages_list = [
    "https://klas.kw.ac.kr/std/lis/evltn/OnlineCntntsStdPage.do", #온라인 컨텐츠
    "https://klas.kw.ac.kr/std/lis/evltn/PrjctStdPage.do", #팀플
    "https://klas.kw.ac.kr/std/lis/evltn/OnlineTestStdPage.do", #온라인 시험
    "https://klas.kw.ac.kr/std/lis/sport/QustnrStdPage.do", #설문
    "https://klas.kw.ac.kr/std/lis/evltn/DscsnStdPage.do", #토론
    "https://klas.kw.ac.kr/std/lis/evltn/TaskStdPage.do", #과제
    "https://klas.kw.ac.kr/std/lis/evltn/AnytmQuizStdPage.do", #퀴즈
    "https://klas.kw.ac.kr/std/lis/sport/6972896bfe72408eb72926780e85d041/BoardListStdPage.do" #강의자료실
]

driver = webdriver.Chrome('chromedriver.exe')  # 크롬드라이버 경로

def klas_login(myID, myPW):
    url_login = "https://klas.kw.ac.kr/" #KLAS 로그인 페이지 주소
    driver.get(url_login)

    #로그인
    driver.find_element(By.ID, 'loginId').send_keys(myID)
    driver.find_element(By.ID, 'loginPwd').send_keys(myPW)
    driver.find_element(By.CLASS_NAME, 'btn').click()

    time.sleep(2)
def accessOC(): #온라인 클래스에 접근
    url = pages_list[0]
    driver.get(url)
    time.sleep(2)

    #학기 선택
    semester_dropdown = driver.find_element(By.NAME, "selectYearhakgi")
    select_semester = Select(semester_dropdown)
    select_semester.select_by_index(1)
    time.sleep(2)

    #강의 선택
    subj_dropdown = driver.find_element(By.NAME, "selectSubj")
    select_subj = Select(subj_dropdown)

    #전체 강의 리스트 담을 테이블
    OC_table = []

    count_subj = len(select_subj.options)
    for i in range(0,count_subj): # 모든 강의 순회하면서 내용 조회
        # print("과목명: ",select_subj.options[i].text.strip())
        select_subj.select_by_index(i)
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        lists = soup.select('#prjctList > tbody')

        table = driver.find_element(By.XPATH, "//*[@id='prjctList']/tbody")
        try:
            tr = table.find_elements(By.TAG_NAME, "tr")  # 여기서의 갯수변동 추적하면 될듯, 그리고 업데이트 내용은 class = "lft"
            #print("강의 갯수: ",len(tr))
            for j in range(0, len(tr)):
                #print(tr[i].find_element(By.CLASS_NAME,"lft").text.strip())
                OC_table.append(select_subj.options[i].text.strip() +', '+ tr[j].find_element(By.CLASS_NAME,"lft").text.strip())
                #가능하면 강의 보기 url도 파싱해서 저장하는게 좋겠음 -> url 따오기 어려움
        except:
            print("강의 없음")
    for k in OC_table:
        print(k)
    # =============================================================================================
    # 내용의 업데이트 판별: OC_table을 txt 파일로 저장, 실행 시 마다 기존의 txt 파일과 새로 만들어진 OC_table 비교
    # 같지 않다면, 새로 만들어진 OC_table - txt 파일 의 내용을 전달해줌.
    # =============================================================================================
    with open(os.path.join(BASE_DIR, 'latest_OC.txt'), 'r+') as f_read:
        i=0
        while(True):
            if OC_table[i] != f_read.readline(i):
                print("기존 캐시와 현재 강의게시판에 다른 내용이 있어요!")
                isThereUpdate(True)
                break
            else:
                i += 1
        f_read.close()

    with open(os.path.join(BASE_DIR, 'latest_OC.txt'), 'w+') as f_write:
        for k in OC_table:
            f_write.write(k+'\n')
        f_write.close()

def accessQZ():
    url = pages_list[6]
    driver.get(url)
    time.sleep(2)

    # 학기 선택
    semester_dropdown = driver.find_element(By.NAME, "selectYearhakgi")
    select_semester = Select(semester_dropdown)
    select_semester.select_by_index(1)
    time.sleep(2)

    # 강의 선택
    subj_dropdown = driver.find_element(By.NAME, "selectSubj")
    select_subj = Select(subj_dropdown)

    #전체 퀴즈 리스트 담을 테이블
    QZ_table = []

    count_subj = len(select_subj.options)
    for i in range(0,count_subj): # 모든 강의 순회하면서 내용 조회
        # print("과목명: ",select_subj.options[i].text.strip())
        select_subj.select_by_index(i)
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        lists = soup.select('#prjctList > tbody')

        table = driver.find_element(By.XPATH, "//*[@id='prjctList']/tbody")
        try:
            tr = table.find_elements(By.TAG_NAME, "tr")  # 여기서의 갯수변동 추적하면 될듯, 그리고 업데이트 내용은 class = "lft"
            #print("강의 갯수: ",len(tr))
            for j in range(0, len(tr)):
                #print(tr[i].find_element(By.CLASS_NAME,"lft").text.strip())
                QZ_table.append(select_subj.options[i].text.strip() +', '+ tr[j].find_element(By.CLASS_NAME,"lft").text.strip())
                #가능하면 강의 보기 url도 파싱해서 저장하는게 좋겠음 -> url 따오기 어려움
        except:
            print("강의 없음")
    for k in QZ_table:
        print(k)
    #Update된 내용, 캐시파일 저장 및 비교 및 업데이트
    with open(os.path.join(BASE_DIR, 'latest_QZ.txt'), 'r+') as f_read:
        i=0
        while(True):
            if QZ_table[i] != f_read.readline(i):
                print("기존 캐시와 현재 퀴즈게시판에 다른 내용이 있어요!")
                isThereUpdate(True)
                break
            else:
                i += 1
        f_read.close()

    with open(os.path.join(BASE_DIR, 'latest_QZ.txt'), 'w+') as f_write:
        for k in QZ_table:
            f_write.write(k+'\n')
        f_write.close()

def accessHW():
    url = pages_list[5]
    driver.get(url)
    time.sleep(2)

    # 학기 선택
    semester_dropdown = driver.find_element(By.NAME, "selectYearhakgi")
    select_semester = Select(semester_dropdown)
    select_semester.select_by_index(1)
    time.sleep(2)

    # 강의 선택
    subj_dropdown = driver.find_element(By.NAME, "selectSubj")
    select_subj = Select(subj_dropdown)

    #전체 과제 리스트 담을 테이블
    HW_table = []

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
            tr = table.find_elements(By.TAG_NAME, "tbody")  # 여기서의 갯수변동 추적하면 될듯, 그리고 업데이트 내용은 class = "lft"
            for j in range(0, len(tr)):
                #print(tr[i].find_element(By.CLASS_NAME,"lft").text.strip())
                HW_table.append(select_subj.options[i].text.strip() +', '+ tr[j].find_element(By.CLASS_NAME,"lft").text.strip())
        except:
            print("과제 없음")
    for k in HW_table:
        print(k)
    # 캐시
    with open(os.path.join(BASE_DIR, 'latest_HW.txt'), 'r+') as f_read:
        i=0
        while(True):
            if HW_table[i] != f_read.readline(i):
                print("기존 캐시와 현재 과제게시판에 다른 내용이 있어요!")
                isThereUpdate(True)
                break
            else:
                i += 1
        f_read.close()

    with open(os.path.join(BASE_DIR, 'latest_HW.txt'), 'w+') as f_write:
        for k in HW_table:
            f_write.write(k+'\n')
        f_write.close()

def isThereUpdate(bool):
    if bool == True:
        return 1;
    else:
        return 0;
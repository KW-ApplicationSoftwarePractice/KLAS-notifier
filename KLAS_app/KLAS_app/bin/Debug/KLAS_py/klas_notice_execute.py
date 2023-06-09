import os
import sys
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def klas_notice(myID, myPW):

    driver = webdriver.Chrome('chromedriver.exe') #크롬드라이버 경로
    url_login = "https://klas.kw.ac.kr/" #KLAS 로그인 페이지 주소
    driver.get(url_login)

    #로그인
    driver.find_element(By.ID, 'loginId').send_keys(myID)
    driver.find_element(By.ID, 'loginPwd').send_keys(myPW)
    driver.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(3)

    #강의 정보 불러오기
    url_lecture = "https://klas.kw.ac.kr/std/lis/evltn/LctrumHomeStdPage.do" #온라인 강의 주소
    driver.get(url_lecture)
    time.sleep(3)
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    lecture_class = []
    lecture_name = []
    lecture_end = []
    cls_num = 1

    try:
        while(True):
            driver.find_element(By.XPATH, '//*[@id="appSelectSubj"]/div[2]/div/div[2]/select/option[' + str(cls_num) + ']').click()
            driver.get("https://klas.kw.ac.kr/std/lis/evltn/LctrumHomeStdPage.do")
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            time.sleep(3)
            
            lecture_tbody = soup.select('div.tablelistbox > table > tbody > tr')
            if len(lecture_tbody) == 1:
                pass
            else:
                for i in range(1,len(lecture_tbody)):
                    if "100%" in lecture_tbody[i].select_one("td:nth-child(6)").text:
                        pass
                    else:
                        lecture_class.append(soup.select_one('#appHeaderSubj > div > div > div.col-md-10.subtitle > span.subjectname').text)
                        lecture_name.append((lecture_tbody[i].select_one("td:nth-child(4)")).get_text())
                        lecture_end.append((lecture_tbody[i].select_one("td:nth-child(5)")).get_text().strip())

            cls_num = cls_num + 1
            lecture_tbody.clear()
    except:
        pass

    notice_lecture = []
    for i in range (0,len(lecture_name)): 
        notice_lecture.append(lecture_class[i] + "~~~" + lecture_name[i] + "~~~" + lecture_end[i] + "\n")

    driver = webdriver.Chrome('chromedriver.exe') #크롬드라이버 경로
    url_login = "https://klas.kw.ac.kr/" #KLAS 로그인 페이지 주소
    driver.get(url_login)

    #로그인
    driver.find_element(By.ID, 'loginId').send_keys(myID)
    driver.find_element(By.ID, 'loginPwd').send_keys(myPW)
    driver.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(3)

    #과제 정보 불러오기
    url_homework = "https://klas.kw.ac.kr/std/lis/evltn/TaskStdPage.do" #과제 주소
    driver.get(url_homework)
    time.sleep(3)
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    homework_class = []
    homework_name = []
    homework_end = []
    cls_num = 1

    try:
        while(True):
            driver.find_element(By.XPATH, '//*[@id="appSelectSubj"]/div[2]/div/div[2]/select/option[' + str(cls_num) + ']').click()
            driver.get("https://klas.kw.ac.kr/std/lis/evltn/TaskStdPage.do")
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            time.sleep(3)
            
            homework_table = soup.select('#appModule > div > div.tablelistbox > table > tbody')
            if len(homework_table) == 1:
                pass
            else:
                for i in range(0,len(homework_table)):
                    if "미제출" in homework_table[i].select_one("tr:nth-child(1) > td:nth-child(4)").text:
                        homework_class.append(soup.select_one('#appHeaderSubj > div > div > div.col-md-10.subtitle > span.subjectname').text)
                        homework_name.append((homework_table[i].select_one("tr:nth-child(1) > td.lft")).get_text())#appModule > div > div.
                        homework_end.append((homework_table[i].select_one("tr:nth-child(1) > td:nth-child(3)")).get_text().strip())
                    else:
                        pass

            cls_num = cls_num + 1
            homework_table.clear()
    except:
        pass

    notice_homework = []
    for i in range (0,len(homework_name)): 
        notice_homework.append(homework_class[i] + "~~~" + homework_name[i] + "~~~" + homework_end[i] + "\n")


    driver = webdriver.Chrome('chromedriver.exe') #크롬드라이버 경로
    url_login = "https://klas.kw.ac.kr/" #KLAS 로그인 페이지 주소
    driver.get(url_login)

    #로그인
    driver.find_element(By.ID, 'loginId').send_keys(myID)
    driver.find_element(By.ID, 'loginPwd').send_keys(myPW)
    driver.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(3)

    #퀴즈 정보 불러오기
    url_homework = "https://klas.kw.ac.kr/std/lis/evltn/AnytmQuizStdPage.do" #퀴즈 주소
    driver.get(url_homework)
    time.sleep(3)
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    quiz_class = []
    quiz_name = []
    quiz_end = []
    cls_num = 1

    try:
        while(True):
            driver.find_element(By.XPATH, '//*[@id="appSelectSubj"]/div[2]/div/div[2]/select/option[' + str(cls_num) + ']').click()
            driver.get("https://klas.kw.ac.kr/std/lis/evltn/AnytmQuizStdPage.do")
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            time.sleep(3)

            quiz_tbody = soup.select('#prjctList > tbody > tr')
            if len(quiz_tbody) == 1:
                pass
            else:
                for i in range(0,len(quiz_tbody)):
                    if "미응시" in quiz_tbody[i].select_one("td:nth-child(6)").text:
                        quiz_class.append(soup.select_one('#appHeaderSubj > div > div > div.col-md-10.subtitle > span.subjectname').text)
                        quiz_name.append((quiz_tbody[i].select_one("td:nth-child(4)")).get_text())
                        quiz_end.append((quiz_tbody[i].select_one("td:nth-child(5)")).get_text().strip())
                    else:
                        pass

            cls_num = cls_num + 1
            quiz_tbody.clear()
    except:
        pass

    notice_quiz = []
    for i in range (0,len(quiz_name)): 
        notice_quiz.append(quiz_class[i] + "~~~" + quiz_name[i] + "~~~" + quiz_end[i] + "\n")

    return_string = ""

    for ltxt in notice_lecture:
        return_string = return_string + ltxt
    return_string = return_string + "///" + "\n"

    for htxt in notice_homework:
        return_string = return_string + htxt
    return_string = return_string + "///" + "\n"

    for qtxt in notice_quiz:
        return_string = return_string + qtxt

    """
    과목~~~강의제목~~~강의기간
    과목~~~강의제목~~~강의기간
    ///
    과목~~~과제제목~~~과제기간
    과목~~~과제제목~~~과제기간
    ///
    과목~~~퀴즈제목~~~퀴즈기간
    과목~~~퀴즈제목~~~퀴즈기간
    """

    print (return_string)



klas_notice(sys.argv[1],sys.argv[2])

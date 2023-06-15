import os
import sys
import time
import datetime
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

def klas_renew(myID, myPW):
    lecture_renew_class = []
    lecture_renew_name = []
    lecture_renew_time = []

    homework_renew_class = []
    homework_renew_name = []
    homework_renew_time = []

    quiz_renew_class = []
    quiz_renew_name = []
    quiz_renew_time = []

    return_text = ""

    driver = webdriver.Chrome('chromedriver.exe') #크롬드라이버 경로

    url_login = "https://klas.kw.ac.kr/" #KLAS 로그인 페이지 주소
    url_main = "https://klas.kw.ac.kr/std/cmn/frame/Frame.do" #메인 페이지 주소
    url_lecture = "https://klas.kw.ac.kr/std/lis/evltn/LctrumHomeStdPage.do" #강의 주소
    url_homework = "https://klas.kw.ac.kr/std/lis/evltn/TaskStdPage.do" #과제 주소
    url_quiz = "https://klas.kw.ac.kr/std/lis/evltn/AnytmQuizStdPage.do" #퀴즈 주소

    
    #KLAS 로그인
    driver.get(url_login)
    driver.find_element(By.ID, 'loginId').send_keys(myID)
    driver.find_element(By.ID, 'loginPwd').send_keys(myPW)
    driver.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(3)


    #강의 정보 불러오기
    driver.get(url_lecture)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(3)

    class_index = 1
    try:
        while(True):
            driver.find_element(By.XPATH, '//*[@id="appSelectSubj"]/div[2]/div/div[2]/select/option[' + str(class_index) + ']').click()
            driver.get(url_lecture)
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
                        lecture_renew_class.append(soup.select_one('#appHeaderSubj > div > div > div.col-md-10.subtitle > span.subjectname').text)
                        lecture_renew_name.append((lecture_tbody[i].select_one("td:nth-child(4)")).get_text())
                        lecture_renew_time.append((lecture_tbody[i].select_one("td:nth-child(5)")).get_text().strip())

            class_index = class_index + 1
            lecture_tbody.clear()
    except:
        pass


    #과제 정보 불러오기
    driver.get(url_homework)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(3)

    class_index = 1
    try:
        while(True):
            driver.find_element(By.XPATH, '//*[@id="appSelectSubj"]/div[2]/div/div[2]/select/option[' + str(class_index) + ']').click()
            driver.get(url_homework)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            time.sleep(3)
            
            homework_table = soup.select('#appModule > div > div.tablelistbox > table > tbody')

            if len(homework_table) == 1:
                pass
            else:
                for i in range(0,len(homework_table)):
                    if "미제출" in homework_table[i].select_one("tr:nth-child(1) > td:nth-child(4)").text:
                        homework_renew_class.append(soup.select_one('#appHeaderSubj > div > div > div.col-md-10.subtitle > span.subjectname').text)
                        homework_renew_name.append((homework_table[i].select_one("tr:nth-child(1) > td.lft")).get_text())
                        homework_renew_time.append((homework_table[i].select_one("tr:nth-child(1) > td:nth-child(3)")).get_text().strip())
                    else:
                        pass

            class_index = class_index + 1
            homework_table.clear()
    except:
        pass


    #퀴즈 정보 불러오기
    driver.get(url_quiz)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(3)

    class_index = 1
    try:
        while(True):
            driver.find_element(By.XPATH, '//*[@id="appSelectSubj"]/div[2]/div/div[2]/select/option[' + str(class_index) + ']').click()
            driver.get(url_quiz)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            time.sleep(3)

            quiz_tbody = soup.select('#prjctList > tbody > tr')

            if len(quiz_tbody) == 1:
                pass
            else:
                for i in range(0,len(quiz_tbody)):
                    if "미응시" in quiz_tbody[i].select_one("td:nth-child(6)").text:
                        quiz_renew_class.append(soup.select_one('#appHeaderSubj > div > div > div.col-md-10.subtitle > span.subjectname').text)
                        quiz_renew_name.append((quiz_tbody[i].select_one("td:nth-child(4)")).get_text())
                        quiz_renew_time.append((quiz_tbody[i].select_one("td:nth-child(5)")).get_text().strip())
                    else:
                        pass

            class_index = class_index + 1
            quiz_tbody.clear()
    except:
        pass


    #WinForm으로 전달할 return_text 구현
    if (len(lecture_renew_class) != 0):
        for i in range(0, len(lecture_renew_class)):
            return_text = return_text + lecture_renew_class[i] + "////" + lecture_renew_name[i] + "////" + lecture_renew_time[i] + "\n"
    else:
        pass
    return_text = return_text + "####" + "\n"
    if (len(homework_renew_class) != 0):
        for i in range(0, len(homework_renew_class)):
            return_text = return_text + homework_renew_class[i] + "////" + homework_renew_name[i] + "////" + homework_renew_time[i] + "\n"
    else:
        pass
    return_text = return_text + "####" + "\n"
    if (len(quiz_renew_class) != 0):
        for i in range(0, len(quiz_renew_class)):
            return_text = return_text + quiz_renew_class[i] + "////" + quiz_renew_name[i] + "////" + quiz_renew_time[i] + "\n"
    else:
        pass

    """
    강의명1////강의이름1////강의기간1
    강의명2////강의이름2////강의기간2
    강의명3////강의이름3////강의기간3
    ####
    강의명1////과제이름1////과제기간1
    강의명2////과제이름2////과제기간2
    강의명3////과제이름3////과제기간3
    ####
    강의명1////퀴즈이름1////퀴즈기간1
    강의명2////퀴즈이름2////퀴즈기간2
    강의명3////퀴즈이름3////퀴즈기간3
    """

    print(return_text)
    

    #KLAS와 Google Calender 동기화
    creds_filename = 'credentials.json'
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    
    credential_path = os.path.join('./', 'credentials_sample.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(creds_filename, SCOPES)
        credentials = tools.run_flow(flow, store)
    service = build('calendar', 'v3', credentials=credentials)

    today = datetime.date.today().isoformat()
    event = {
                'summary': '', # 일정 제목
                'description': 'KLAS-notifier', # 일정 설명
                'start': { # 시작 날짜
                    'dateTime': today + 'T09:00:00',
                    'timeZone': 'Asia/Seoul'
                },
                'end': { # 종료 날짜
                    'dateTime': today + 'T10:00:00',
                    'timeZone': 'Asia/Seoul'
                }
            }
        
    #캘린더의 모든 일정 불러오기
    page_token = None
    event_list = []

    while True:
        events_tmp = service.events().list(calendarId='primary', pageToken=page_token).execute()
        for event_tmp in events_tmp['items']:
            event_list.append(event_tmp)
        page_token = events_tmp.get('nextPageToken')
        if not page_token:
            break

    #Description 이 'KLAS-notifier' 이면 전부 삭제
    for event_search in event_list:
        if event_search.get("description") and event_search["description"] == "KLAS-notifier":
            service.events().delete(calendarId='primary', eventId=event_search['id']).execute()

    #KLAS의 미완료 항목과 동기화
    info_split = []
    if (len(lecture_renew_class) != 0): #강의 동기화
        for i in range (0, len(lecture_renew_class)):
            info_split = [lecture_renew_class[i], lecture_renew_name[i], lecture_renew_time[i]]
            time_text = (info_split[2])[-16:]
            time_text_list = time_text.split(' ')
            time_hour_and_min = 'T' + time_text_list[1] + ':00' 
            event['summary'] = "[" + info_split[0] + "] " + info_split[1]
            event['start'] = {'dateTime' : time_text_list[0] + time_hour_and_min, 'timeZone' : 'Asia/Seoul'}
            event['end'] = event['start']
            service.events().insert(calendarId='primary', body=event).execute()
    else:
        pass
    if (len(homework_renew_class) != 0): #과제 동기화
        for i in range (0, len(homework_renew_class)):
            info_split = [homework_renew_class[i], homework_renew_name[i], homework_renew_time[i]]
            time_text = (info_split[2])[-19:]
            time_text_list = time_text.split(' ')
            time_hour_and_min = 'T' + time_text_list[1]
            event['summary'] = "[" + info_split[0] + "] " + info_split[1]
            event['start'] = {'dateTime' : time_text_list[0] + time_hour_and_min, 'timeZone' : 'Asia/Seoul'}
            event['end'] = event['start']
            service.events().insert(calendarId='primary', body=event).execute()
    else:
        pass
    if (len(quiz_renew_class) != 0): #퀴즈 동기화
        for i in range (0, len(quiz_renew_class)):
            info_split = [quiz_renew_class[i], quiz_renew_name[i], quiz_renew_time[i]]
            time_text = (info_split[2])[-16:]
            time_text_list = time_text.split(' ')
            time_hour_and_min = 'T' + time_text_list[1] + ':00'
            event['summary'] = "[" + info_split[0] + "] " + info_split[1]
            event['start'] = {'dateTime' : time_text_list[0] + time_hour_and_min, 'timeZone' : 'Asia/Seoul'}
            event['end'] = event['start']
            service.events().insert(calendarId='primary', body=event).execute()
    else:
        pass

klas_renew(sys.argv[1], sys.argv[2])

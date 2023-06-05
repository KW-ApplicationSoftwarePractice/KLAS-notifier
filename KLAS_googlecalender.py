import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

import klas_notice

def klas_automating(myID, myPW):
    creds_filename = 'credentials.json'
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    flow = InstalledAppFlow.from_client_secrets_file(creds_filename, SCOPES)
    creds = flow.run_local_server(port=0)

    today = datetime.date.today().isoformat()
    service = build('calendar', 'v3', credentials=creds)
    
    event = {
            'summary': '', # 일정 제목
            'description': '', # 일정 설명
            'start': { # 시작 날짜
                'dateTime': today + 'T09:00:00',
                'timeZone': 'Asia/Seoul'
            },
            'end': { # 종료 날짜
                'dateTime': today + 'T10:00:00',
                'timeZone': 'Asia/Seoul'
            }
        }
    
    lecture_events = klas_notice.klas_notice_lecture(myID, myPW)
    for lecture_event in lecture_events:
        info_split = lecture_event.split('/')
        time_text = (info_split[2])[-16:]
        time_text_list = time_text.split(' ')
        time_hour_and_min = 'T' + time_text_list[1] + ':00'
        event['summary'] = "[" + info_split[0] + "] " + info_split[1]
        event['start'] = {'dateTime' : time_text_list[0] + time_hour_and_min, 'timeZone' : 'Asia/Seoul'}
        event['end'] = event['start']
        service.events().insert(calendarId='primary', body=event).execute()
    
    homework_events = klas_notice.klas_notice_homework(myID, myPW)
    for homework_event in homework_events:
        info_split = homework_event.split('/')
        time_text = (info_split[2])[-19:]
        time_text_list = time_text.split(' ')
        time_hour_and_min = 'T' + time_text_list[1]
        event['summary'] = "[" + info_split[0] + "] " + info_split[1]
        event['start'] = {'dateTime' : time_text_list[0] + time_hour_and_min, 'timeZone' : 'Asia/Seoul'}
        event['end'] = event['start']
        service.events().insert(calendarId='primary', body=event).execute()

    quiz_events = klas_notice.klas_notice_quiz(myID, myPW)
    for quiz_event in quiz_events:
        info_split = quiz_event.split('/')
        time_text = (info_split[2])[-16:]
        time_text_list = time_text.split(' ')
        time_hour_and_min = 'T' + time_text_list[1] + ':00'
        event['summary'] = "[" + info_split[0] + "] " + info_split[1]
        event['start'] = {'dateTime' : time_text_list[0] + time_hour_and_min, 'timeZone' : 'Asia/Seoul'}
        event['end'] = event['start']
        service.events().insert(calendarId='primary', body=event).execute()
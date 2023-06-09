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
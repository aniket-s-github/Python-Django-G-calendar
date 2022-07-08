from django.http import HttpResponse
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

scope = ['https://www.googleapis.com/auth/calendar.events.readonly']
# scope = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file('C:\\Users\\dilip\\PycharmProjects\\client_secret.json', scopes=scope)
creds = None

# def GoogleCalendarInitView(request):
#     return HttpResponse("""<h> Home Page </h>
#     <a href="https://www.calendar.google.com"> Google Calendar</a>""")

def home(request):
    return HttpResponse("<body><h1>Django Google Calender</h1> <a href='/rest/v1/calendar/init/'>Start</a></body>")

def GoogleCalendarInitView(request):
    creds = flow.run_local_server()
    # creds = flow.run_console()
    if creds:
        return HttpResponse("<a href='/rest/v1/calendar/redirect/'>show</a>")
    else:
        return HttpResponse("Error Occured! Permission denied!")

def GoogleCalendarRedirectView(request):
    service = build('calendar', 'v3', credentials=creds)
    events = service.calendarList().list().execute()
    return HttpResponse(events)

from __future__ import print_function
from email import message
import discord
import random
import os
from discord.ext import commands
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
bot = commands.Bot(command_prefix='.', description = "Hi :)")
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Colossal Cave Adventure"))



            
@bot.command(name='quote',help = 'gives John quote')
async def quotes(ctx):
    John_quotes = [
    "So we do have class friday ya?", 
    "I don't think you understand what that is.", 
    "Can you go back to your error please." , 
    "Sara's actually getting worse at programming.", 
    "Do you have a program?", 
    "Can you get off pinterest and work on your program please.",
    "Most likely.", 
    "No!", 
    "Why don't you go lie under that table.", 
    "This would be better if it had legs.",
    "Making a text based rpg is kind of simple for you at this point.",
    "I would only consider teaching advanced physics if it were an emergency.",
    "What does that mean? tic tac?",
    "If you're doing loops and texts again, I will not be happy.",
    "Yeah I intentionally reformatted all these computers just to destory your golf program.",
    "The funny thing is I learned to write code by hand.",
    "Like maybe it's like really really trouble.",
    "I wonder if you can maybe like make the bottom layer disapear once in a while",
    "It has a little picture of a (hand motion). Have fun.",
    "Hey it's the string I've been looking for.",
    "Are you going to poison your computer science teacher so I can sub?"

    ]
    response = random.choice(John_quotes)
    await ctx.send(response)

@bot.command(name='schedule',help = 'coming soon to a John bot near you')
async def quotes(ctx,arg):
    username = str(ctx.message.author.id)
    response = ""
    arg = arg.lower()
    if username == os.environ['DISCORD_ID']:
        response = arg + "'s breakdown is:\n"
    else:
        response = "no\n"
    def main(response,arg):
        
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
            today = datetime.datetime.now(datetime.timezone.utc).astimezone()
            today = today.replace(hour=0, minute=0, second=0, microsecond=0)
            tomorrow = today + datetime.timedelta(days=1)
            tomorrow = tomorrow.isoformat()
            today = today.isoformat()
            now = datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat()
            todayend = datetime.datetime.now(datetime.timezone.utc).astimezone()
            todayend = todayend.replace(hour=23, minute=59, second=59, microsecond=0)
            tomorrowend = todayend + datetime.timedelta(days=1)
            tomorrowend = tomorrowend.isoformat()
            todayend = todayend.isoformat()
            #print('Getting the upcoming 10 events')
            if response == "no":
                return response
            if arg == 'today':
                events_result = service.events().list(calendarId='u5va2sqv38sv6a3v700pou832jfcjv8i@import.calendar.google.com', timeMin=today,
                                                    timeMax = todayend, singleEvents=True,
                                                    orderBy='startTime', timeZone = 'EST').execute()
                events_result1 = service.events().list(calendarId='npm38bcvh7rhs2pltu8p16ob7p5k71bj@import.calendar.google.com', timeMin=today,
                                                    timeMax = todayend, singleEvents=True,
                                                    orderBy='startTime', timeZone = 'EST').execute()
                events_result2 = service.events().list(calendarId='gckyoshi@gmail.com', timeMin=today,
                                                    timeMax = todayend, singleEvents=True,
                                                    orderBy='startTime', timeZone = 'EST').execute()
                events = events_result.get('items', [])
                events1 = events_result1.get('items', [])
                events2 = events_result2.get('items', [])
            elif arg == 'tomorrow':
                events_result = service.events().list(calendarId='u5va2sqv38sv6a3v700pou832jfcjv8i@import.calendar.google.com', timeMin=tomorrow,
                                                    timeMax = tomorrowend, singleEvents=True,
                                                    orderBy='startTime', timeZone = 'EST').execute()
                events_result1 = service.events().list(calendarId='npm38bcvh7rhs2pltu8p16ob7p5k71bj@import.calendar.google.com', timeMin=tomorrow,
                                                    timeMax = tomorrowend, singleEvents=True,
                                                    orderBy='startTime', timeZone = 'EST').execute()
                events_result2 = service.events().list(calendarId='gckyoshi@gmail.com', timeMin=tomorrow,
                                                    timeMax = tomorrowend, singleEvents=True,
                                                    orderBy='startTime', timeZone = 'EST').execute()
            else:
                return "not valid argument"
            def dayschedule(event_result,event_result1,event_result2,response):
                events = events_result.get('items', [])
                events1 = events_result1.get('items', [])
                events2 = events_result2.get('items', [])
                for event in events1:
                    if "US Assembly" in event['summary']:
                        check = 1
                    else:
                        check = 0
                if not events and check == 0 and not events2:
                    response += 'free all day, go watch some anime\n'
                    return response
        # Prints the start and name of the next 10 events
                total_events = []
                for event in events:
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    end = event['end'].get('dateTime', event['end'].get('date'))
                    start = start.replace("T", " ")
                    start = start[:-6]
                    start = datetime.datetime.strptime(start,'%Y-%m-%d %H:%M:%S')
                    end = end.replace("T", " ")
                    end = end[:-6]
                    end = datetime.datetime.strptime(end,'%Y-%m-%d %H:%M:%S')
                    total_events.append(start)
                    total_events.append(end)
            #print(datetime.datetime.strftime(start,"%I:%M"), "-", datetime.datetime.strftime(end,"%I:%M"), event['summary'])
            
            
            #if start and end date are equal no free time
            #if not equal then free time
                for event in events1:
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    end = event['end'].get('dateTime', event['end'].get('date'))
                    if "US Assembly" in event['summary']:
                    #print(start, "-", end, event['summary'])
                        start = start.replace("T", " ")
                        start = start[:-6]
                        start = datetime.datetime.strptime(start,'%Y-%m-%d %H:%M:%S')
                        end = end.replace("T", " ")
                        end = end[:-6]
                        end = datetime.datetime.strptime(end,'%Y-%m-%d %H:%M:%S')
                        total_events.append(start)
                        total_events.append(end)
                    #print(datetime.datetime.strftime(start,"%I:%M"), "-", datetime.datetime.strftime(end,"%I:%M"), event['summary'])
            
                    else:
                        hi = 1
                if len(total_events) != 0:
                    sorted_events = sorted(total_events)
                    for i in range(1,len(sorted_events)-1,2):
                        if sorted_events[i] != sorted_events[i+1]:
                            free = "You have free time from " + datetime.datetime.strftime(sorted_events[i] ,"%I:%M") + "-" + datetime.datetime.strftime(sorted_events[i+1] ,"%I:%M") + "\n"
                            response += str(free)
                    last_class = "and your last class ends at " + datetime.datetime.strftime(sorted_events[-1] ,"%I:%M") + "\n"
                    response += str(last_class)
                for event in events2:
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    end = event['end'].get('dateTime', event['end'].get('date'))
                    start = start.replace("T", " ")
                    start = start[:-6]
                    start = datetime.datetime.strptime(start,'%Y-%m-%d %H:%M:%S')
                    end = end.replace("T", " ")
                    end = end[:-6]
                    end = datetime.datetime.strptime(end,'%Y-%m-%d %H:%M:%S')
                    calendar_events = "You have an event " + event['summary'] + " at " + datetime.datetime.strftime(start,"%I:%M") + "-" + datetime.datetime.strftime(end,"%I:%M %p") + "\n"
                    response += str(calendar_events)
                return response
            response = dayschedule(events_result,events_result1,events_result2,response)
        except HttpError as error:
            print('An error occurred: %s' % error)
        print(response)
        return response

    if __name__ == '__main__':
        message = main(response,arg)
        await ctx.send(message)
#to update do git add . then git commit -m "message" then git push

bot.run(os.environ['DISCORD_TOKEN'])

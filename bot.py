from __future__ import print_function
from email import message
import discord
import random
import os
from discord.ext import commands
import datetime
import os.path
import time
import asyncio
import pytz
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
bot = commands.Bot(command_prefix='.', description = "Hi :)")
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
WHEN = datetime.time(8, 0, 0)  # 8:00 AM
tz = pytz.timezone('US/Eastern')
channel_id = 957382034744033361
guild_id = 724158861979942922
#defining out of discord bot for use in functions

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

    #uses arg supplied with command to get schedule to specified day
        advance = 0
        if arg == 'today':
            advance = 0
        elif arg == "tomorrow":
            advance = 1
        elif arg.isdigit() == True:
            advance = int(arg)
        #sets day and day end for specified day to get events on that day
        day = datetime.datetime.now(datetime.timezone.utc).astimezone()
        day = day.replace(hour=0, minute=0, second=0, microsecond=0)
        day = day + datetime.timedelta(days=advance)
        dayend = day.replace(hour=23, minute=59, second=59, microsecond=0)
        day = day.isoformat()
        dayend = dayend.isoformat()
        now = datetime.datetime.now(datetime.timezone.utc).astimezone()
        #checking if user who gave the command is intended user
        if response == "no" or response == "invalid input":
            return response
        #getting events
        events_result = service.events().list(calendarId='u5va2sqv38sv6a3v700pou832jfcjv8i@import.calendar.google.com', timeMin=day,
                                            timeMax = dayend, singleEvents=True,
                                            orderBy='startTime', timeZone = 'EST').execute()
        events_result1 = service.events().list(calendarId='npm38bcvh7rhs2pltu8p16ob7p5k71bj@import.calendar.google.com', timeMin=day,
                                            timeMax = dayend, singleEvents=True,
                                            orderBy='startTime', timeZone = 'EST').execute()
        events_result2 = service.events().list(calendarId='gckyoshi@gmail.com', timeMin=day,
                                            timeMax = dayend, singleEvents=True,
                                            orderBy='startTime', timeZone = 'EST').execute()
        #setting end of day for to only get free time within school day  
        endOfDay = now.replace(hour=15, minute=15, second=0)
        endOfDay = endOfDay + datetime.timedelta(days=advance)
        #function that sorts the events to give result
        def dayschedule(event_result,event_result1,event_result2,response,dayend):
            events = events_result.get('items', [])
            events1 = events_result1.get('items', [])
            events2 = events_result2.get('items', [])
            check = 0
            sport = 0
            #"if not events1" will be false even if there are events in it that don't take up my time (not assembly)
            for event in events1:
                if "US Assembly" in event['summary']:
                    check = 1
                else:
                    check = 0
            if not events and check == 0 and not events2:
                response += 'free all day, go watch some anime\n'
                return response
            dayend = datetime.datetime.strftime(dayend,'%Y-%m-%d %H:%M:%S')
            dayend = datetime.datetime.strptime(dayend,'%Y-%m-%d %H:%M:%S')
            total_events = []
            #grabs start and end time for all events
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start)
                end = event['end'].get('dateTime', event['end'].get('date'))
                if "Tennis" in event['summary']:
                    sport = 1
                start = start.replace("T", " ")
                start = start[:-6]
                start = datetime.datetime.strptime(start,'%Y-%m-%d %H:%M:%S')
                end = end.replace("T", " ")
                end = end[:-6]
                end = datetime.datetime.strptime(end,'%Y-%m-%d %H:%M:%S')
                total_events.append(start)
                total_events.append(end)
        #print(datetime.datetime.strftime(start,"%I:%M"), "-", datetime.datetime.strftime(end,"%I:%M"), event['summary'])
            #grabs assembly because it's not in my schedule
            for event in events1:
                start = event['start'].get('dateTime', event['start'].get('date'))
                end = event['end'].get('dateTime', event['end'].get('date'))
                if "US Assembly" in event['summary']:
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
            #gets free time and adds to response
            if len(total_events) != 0:
                sorted_events = []
                check = datetime.datetime.strftime(dayend, '%m-%d')
                check = datetime.datetime.strptime(check,'%m-%d')
                saving_start = '03-13'
                savings_end = "11-6"
                savings_start = datetime.datetime.strptime(saving_start,'%m-%d')
                savings_end = datetime.datetime.strptime(savings_end,'%m-%d')
                if (savings_start < check and check < savings_end):
                    for i in total_events:
                        sorted_events.append(i +datetime.timedelta(hours = +1))
                sorted_events.append(dayend)
                sorted_events.append(dayend)
                sorted_events = sorted(sorted_events)
                if (sorted_events.index(dayend) != -1 and sorted_events.index(dayend) != -2):
                    sorted_events = sorted_events[:-2]
                for i in range(1,len(sorted_events)-1,2):
                    if sorted_events[i] != sorted_events[i+1]:
                        free = "You have free time from " + datetime.datetime.strftime(sorted_events[i] ,"%I:%M") + "-" + datetime.datetime.strftime(sorted_events[i+1] ,"%I:%M") + "\n"
                        response += str(free)
                if sport == 1:
                    last_class = "And you have tennis until 5:45\n"
                    response += str(last_class)
            #gets other events and adds to calendar
            for event in events2:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start)
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
        response = dayschedule(events_result,events_result1,events_result2,response,endOfDay)
    except HttpError as error:
        print('An error occurred: %s' % error)
    print(response)
    return response
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Colossal Cave Adventure"))

async def called_once_a_day():  # Fired every day
    print("lkshfds")
    await bot.wait_until_ready()  # Make sure your guild cache is ready so the channel can be found via get_channel
    channel = bot.get_guild(guild_id).get_channel(channel_id) # Note: It's more efficient to do bot.get_guild(guild_id).get_channel(channel_id) as there's less looping involved, but just get_channel still works fine
    print(channel)
    await channel.send(main("today's breakdown is:\n","today"))

async def background_task():
    now = datetime.datetime.now(tz)
    now = now.replace(tzinfo=None)
    print(now)
    if now.time() > WHEN:  # Make sure loop doesn't start after {WHEN} as then it will send immediately the first time as negative seconds will make the sleep yield instantly
        print("hello")
        tomorrow = datetime.datetime.combine(now.date() + datetime.timedelta(days=1), datetime.time(0))
        seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
        await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start 
    while True:
        now = datetime.datetime.now(tz)
        now = now.replace(tzinfo=None)
        target_time = datetime.datetime.combine(now.date(), WHEN)  
        seconds_until_target = (target_time - now).total_seconds()
        print(seconds_until_target)
        await asyncio.sleep(seconds_until_target)  # Sleep until we hit the target time
        await called_once_a_day()  # Call the helper function that sends the message
        tomorrow = datetime.datetime.combine(now.date() + datetime.timedelta(days=1), datetime.time(0))
        seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
        await asyncio.sleep(seconds)
            
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

@bot.command(name='schedule',help ="""Gets free time for a day in the future
 Usage: ".schedule x" where x is how manys in the future you want your free time for
  You can use today or tomorrow instead of 0 and 1 respectively.""")
async def quotes(ctx,arg):
    username = str(ctx.message.author.id)
    response = ""
    arg = arg.lower()
    if username == os.environ['DISCORD_ID']:
        if arg == '0' or arg == "today":
            response = "today's breakdown is:\n"
        elif arg == '1' or arg == "tomorrow":
            response = "tomorrow's breakdown is:\n"
        elif arg.isdigit():
            response = "The breakdown in " + arg + " days is: \n"
        else:
            response = "invalid input"
    else:
        response = "no\n"
    if __name__ == '__main__':
        message = main(response,arg)
        await ctx.send(message)
#to update do git add . then git commit -m "message" then git push
if __name__ == '__main__':
    bot.loop.create_task(background_task())
    bot.run(os.environ['DISCORD_TOKEN'])

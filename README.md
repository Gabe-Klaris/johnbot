# johnbot
#Code for discord bot<br />
#Bot made with quotes from John<br />
#Also integrates with google calendar<br />
#steps for making your own are below<br />
#:) :( <br />




#Requirements for bot: github account and git, heroku account, discord account and bot, pip and python downloaded on computer

#Step 1: Download your "my schedule" and "school schedule" from the calendars and events tab on veracross.              
#Make sure you download these to your personal email calendar and not your school email.   


#Step2: Clone this repo using git clone https://github.com/Tubby101/johnbot <br />

#Step 3: Create an Heroku account and create an App <br />
#Connect your cloned github repo to the Heroku App in the deploy tab(or if this feature is still down, use heroku CLI with this tutorial:(https://devcenter.heroku.com/articles/heroku-cli)<br />
#Enable automatic deploys (if using github) or if using heroku CLI push the all the files in the repo to the app<br />
#Go to the resources tab and enable worker dynos(without a added card the bot will be up for about 3/4th of the month, with the card it will always be up)<br />


#Step4: Now there are 8 variables to fill in, first the discord variables. <br />
#First create an application at this link https://discord.com/developers/applications<br /> 
#Copy the discord token and story it as DISCORD_ID in your config vars<br />
#Go to "URL generator" under the OAuth2 tab and click on the "bot" tick mark, then copy the url at the bottom of the page, paste it in your browser and add the bot to your server<br />
#In the server create a channel for the auto messages to go into, and copy the id of the channel by right clicking it, put that in the config vars with the key "channel_id"<br />
#Also copy the id of the server, and put that with "guild_id", you can also copy your own user id and put it with the key "DISCORD_ID" (this makes it so only you can access your schedule) <br />

#Step 5: We will now get the ids of the calendars used<br />
#First put the email you downloaded the veracross calendars to in config vars with "calendar_email".<br />
#Now go to your google calendar and on the left of your screen there should be a list of your calendars.<br />
#Click on the three dots next to the name of your classes schedule(should be "all classes" and go to settings. <br />
#scroll down to "integrate calendar" and there should be a field named "Calendar ID", copy this field and save it with "classes_schedule_id" in config vars. <br />
#Do the same with the school schedule calendar, and save the id with "veracross_school_schedule_id". <br />

#Step 6: For the last step we need to generate the token to link to your calendar <br />
#first download the google api library using this command in your terminal "pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib"<br />
#Now run the quickstart.py file using the command "python quickstart.py"<br />
#If either of these dont work, make sure you have everything install correctly<br />
#Log into the google account you saved the calendars on, and accept the authorization(basically you are using the connection to google calendar I set up instead of setting one up on your own, It doesn't give me access to anything).<br />
#Once the authoirzation for the app is finished, the file "token.json" should have been created in the folder you ran quickstart.py in <br />
#copy the contents of the file into heroku config vars with the key "GOOGLE_APPLICATION_CREDENTIALS".<br />

#Step 7: Push again to the reset all dynos in heroku, and your app should build and run.<br />

#:) =(^.^)=









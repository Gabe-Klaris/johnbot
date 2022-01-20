import discord
import random
import os
from discord.ext import commands
bot = commands.Bot(command_prefix='.', description = "Hi :)")

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
    "Are you going to poison you computer science teacher so I can sub?"

    ]
    response = random.choice(John_quotes)
    await ctx.send(response)

@bot.command(name='schedule',help = 'coming soon to a John bot near you')
async def quotes(ctx,arg):
    username = str(ctx.message.author.id)
    if username == os.environ['DISCORD_TOKEN']:
        response = arg
    else:
        response = "no"
    await ctx.send(response)
#to update do git add . then git commit -m "message" then git push

bot.run(os.environ['DISCORD_TOKEN'])

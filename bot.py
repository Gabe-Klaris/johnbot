import discord
import random
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

            
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
    "If you're doing loops and texts again, i will not be happy."
    ]
    response = random.choice(John_quotes)
    await ctx.send(response)



bot.run(os.environ['DISCORD_TOKEN'])

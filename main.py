import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

import webserver #for running bot 24/7

load_dotenv() #gathers discord token from .env file
token = os.getenv('DISCORD_TOKEN')

#LOGGING FOR BOT DEBUG :P
handler = logging.FileHandler(filename = 'discord.log', mode = 'w')

#INTENTS (so bot can do shit)
intents = discord.Intents.default()
intents.message_content = True #allows bot to send message, attachments, etc.
intents.members = True #access to member join/leave, public profile info, etc. (for changing nicknames)

#MAKING THE BOT
bot = commands.Bot(command_prefix = '!', intents = intents)#for l8r if we want to mention bot with "!"

#BOT EVENTS
@bot.event 
async def on_ready(): #just to check when bot starts running in debug
    print(f"USERNAME: {bot.user.name}")
    print(f"TOKEN: {token}")
    

@bot.event #MESSAGING EVENT
async def on_message(message):
    if message.author == bot.user: #makes sure no infinite loops happen :p
        return
    if "yesburger" in message.content.lower():
        #reply with image of dog with yesburger
        await message.reply (file= discord.File("yesburger.png"))
        

    await bot.process_commands(message)

#RUNNING THE BOT
bot.run(token, log_handler = handler, log_level = logging.DEBUG)
webserver.keep_alive()


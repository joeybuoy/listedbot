#Discord Bot listed.py
# using packages discord.py & python-dotenv

#import packages
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

#assign token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

description= "To organize ideas with your group"
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

#simplify bot command events
bot = commands.Bot(command_prefix='/', description=description, intents=intents)


#example prompt /add coraline to $movielist
#initialize database

#adding to list
@bot.command()
async def add(ctx,arg):
    # extracting idea name and list name from message
    splitString = arg.split("$")
    frontmsg= splitString[1]
    ideaname= frontmsg.pop(-1)
    listname.tlt= splitString[2]
    try:
       # pull from database
    except Exception:
       #search database for match
       await ctx.send(f"{listname_tlt} doesn't exist :< !")
       return
   #append new idea to existing list
    listname= [listname;ideaname];
   
          ctx.send(f"{ideaname} added to {listname.tlt}!")
       

"""
#removing from list (by number) /remove
    
#archive from list /archive
#renaming list /rename

"""
#view lists
@bot.command()
async def view(ctx, arg)
msg= str(arg)
        listname= msg[1:]
              # search in database for match
              for number, listname in enumerate(listname):
              await #print list header
                     print(number, listname)
#create list
@bot.command()
async def create(ctx,*,arg):
    #enter new list into database
  total_lists=[total_lists], str(arg)]
    await ctx.send(f"{arg} added to lists!")
        
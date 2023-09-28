# -*- coding: utf-8 -*-
#Discord Bot listed.py
# using packages discord.py & python-dotenv

#import packages
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import sqlite3

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
con = sqlite3.connect("listedbot.db")
cur = con.cursor()

#adding to list
@bot.command()
async def add(ctx,arg, case_insensitive = True):
    # extracting idea name and list name from message
    splitString = arg.split("$")
    frontmsg= splitString[1]
    ideaname= frontmsg.pop(-1)
    listname_tlt= splitString[2]
    
    # find and add to database
    try:
     result = cur.execute("""
    INSERT INTO ? VALUES (?) """, (listname.tlt,ideaname))

   #ctx.send(f'{ideaname} added to {listname\_tlt}!')
    
    except Exception:
       result.fetchone() is None
       await ctx.send(f"{listname_tlt} doesn't exist :< !")
       return

#removing from list (by number) /remove $movielist 3
#also used to remove lists themselves
@bot.command()
async def remove(ctx,arg,int, case_insensitive=True):
       removal_int= int
     #  if "-" in (message.content.lower()).replace(" ", ""):
         
#archive from list /archive

#same as removal except pop is a move if archive x doesnt exist, create it
#renaming list /rename

#@bot.command()
#async def rename(ctx,arg):
       #remove $ from movielist
       #search for it in database
       #rename key
        
#view lists
@bot.command()
async def view(ctx, arg)
msg= str(arg)
        listname= msg[1:]
              # search in database for match
             
              try:
            result= res.fetchall("SELECT idea name FROM ?",(arg))
              for number, result in enumerate(result):
              await print f"{arg}"
                     print(number, result)
              except Exception:
                 result.fetchall() is None
                 await ctx.send(f"{listname_tlt} doesn't exist :< !")
                 return
              
                     
#create list
@bot.command()
async def create(ctx,*,arg):
    #enter new list into database
    tb_create = f"CREATE TABLE [{arg}](idea name)"
    conn.execute(tb_create)
    await ctx.send(f"{arg} added to lists!")
        
#Discord Bot listed.py
# using packages discord.py & python-dotenv

#import packages
import os
import discord
from dotenv import load_dotenv

#assign token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

###Example:delete ---> UNNECESSARY
#this code prints a welcome message to client (user) when they first connect to a discord server
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

#this runs the client event through the bot token
client.run(TOKEN)

#CLIENT EVENTS
#adding to list
#removing from list
#archive from list
#calling list
#renaming list

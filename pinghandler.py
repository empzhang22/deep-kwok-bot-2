debug = True
andrew_debug = False
andrew_debug2 = False

import os

import discord
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
ANDREW = int(os.getenv('ANDREW_ID'))

async def ping_handler(client, message):
    if debug: print("in ping_handler")
    if "extract_message" in message.content:
        await andrew_message_extractor(client)

# Performed testing to arrive at Andrew's user ID
async def andrew_message_extractor(client):
    file = open('andrew_text.txt', 'w', encoding="utf-8")
    if debug: print("in andrew_message_extractor")
    guild = discord.utils.get(client.guilds, name=GUILD)
    for channel in guild.channels:
        if andrew_debug: 
            print("*****CHANNEL NAME: " + channel.name + "*****")
            print(type(channel))
        if isinstance(channel, discord.channel.TextChannel):
            # channel.history uses an asyncrhonous iterator so everything must use async and await
            await andrew_message_extractor_helper(file, channel)
    file.close()
    if debug: print("finished")
    
async def andrew_message_extractor_helper(file, channel):
    if debug: print("in andrew_message_extractor_helper")
    async for message in channel.history(limit=10000):
        if andrew_debug:
            print(message.author.id)
            #print(message.content)
        if message.author.id == ANDREW: 
            if andrew_debug2: print(message.content)
            file.write(message.content + "\n")
    if andrew_debug: print('-----------------------------')

    # Writing into a txt file using Python: https://blog.enterprisedna.co/python-write-to-file/
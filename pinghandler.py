debug = True
andrew_debug = False
andrew_debug2 = False
respond_debug = True

import os

import model

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
ANDREW = int(os.getenv('ANDREW_ID'))

# Handles messages where the bot was mentioned or 'pinged'. For now, has two built-in functions to 
# recognize what text was in the message as a shortcut for slash commands
async def ping_handler(client, message):
    if debug: print("in ping_handler")
    if "extract_message" in message.content:
        await andrew_message_extractor(client)
    
    if "extract_long" in message.content:
        await andrew_message_extractor2(client)

    if "generate" in message.content:
        await respond(client, message)

# Performed testing to arrive at Andrew's user ID
# When prompted, combs through every channel in the server to write data to the 'andrew_text.txt' file, 
# the training corpus for the model
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

async def andrew_message_extractor2(client):
    file = open('andrew_text_long.txt', 'w', encoding="utf-8")
    if debug: print("in andrew_message_extractor2")
    guild = discord.utils.get(client.guilds, name=GUILD)
    for channel in guild.channels:
        if andrew_debug: 
            print("*****CHANNEL NAME: " + channel.name + "*****")
            print(type(channel))
        if isinstance(channel, discord.channel.TextChannel):
            # channel.history uses an asyncrhonous iterator so everything must use async and await
            await andrew_message_extractor_helper2(file, channel)
            file.write("\n")
    file.close()
    if debug: print("finished")

# The message extractor relies on an asynchronous iterator, 'for message in channel.history'.
# Can control number of messages to analyze per channel by the 'limit' param
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

async def andrew_message_extractor_helper2(file, channel):
    if debug: print("in andrew_message_extractor_helper2")
    async for message in channel.history(limit=20000):
        if andrew_debug:
            print(message.author.id)
            #print(message.content)
        if message.author.id == ANDREW: 
            if andrew_debug2: print(message.content)
            file.write(message.content)
    if andrew_debug: print('-----------------------------')

    # Writing into a txt file using Python: https://blog.enterprisedna.co/python-write-to-file/

# A function to respond to a given message with some generated text.
async def respond(client, message):
    if debug: print("in respond")
    context = message.content.replace('<@1186775215892598795>', '')
    context = context.strip()
    if respond_debug: print('context: ' + context)
    await model.generate_text(message, context)
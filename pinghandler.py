debug = True
message_debug = False
content_debug = False
respond_debug = True

import os

import model

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
USER_ID = int(os.getenv('USER_ID'))
USER_NAME = os.getenv('USER_NAME')

# Handles messages where the bot was mentioned or 'pinged'. For now, has two built-in functions to 
# recognize what text was in the message as a shortcut for slash commands
async def ping_handler(client, message):
    if debug: print("in ping_handler")
    if "extract_message" in message.content:
        await message_extractor(client)
    
    if "extract_long" in message.content:
        await long_message_extractor(client)

    if "generate" in message.content:
        await respond(client, message)

# Performed testing to arrive at a user ID
# When prompted, combs through every channel in the server to write data to the '{user}_text.txt' file, 
# the training corpus for the model
async def message_extractor(client):
    file = open(f'{USER_NAME}_text.txt', 'w', encoding="utf-8")
    if debug: print("in message_extractor")
    guild = discord.utils.get(client.guilds, name=GUILD)
    for channel in guild.channels:
        if message_debug: 
            print("*****CHANNEL NAME: " + channel.name + "*****")
            print(type(channel))
        if isinstance(channel, discord.channel.TextChannel):
            # channel.history uses an asyncrhonous iterator so everything must use async and await
            await message_extractor_helper(file, channel)
    file.close()
    if debug: print("finished")

async def long_message_extractor(client):
    file = open(f'{USER_NAME}_long.txt', 'w', encoding="utf-8")
    if debug: print("in long_message_extractor")
    guild = discord.utils.get(client.guilds, name=GUILD)
    for channel in guild.channels:
        if message_debug: 
            print("*****CHANNEL NAME: " + channel.name + "*****")
            print(type(channel))
        if isinstance(channel, discord.channel.TextChannel):
            # channel.history uses an asyncrhonous iterator so everything must use async and await
            await long_message_extractor_helper(file, channel)
            file.write("\n")
    file.close()
    if debug: print("finished")

# The message extractor relies on an asynchronous iterator, 'for message in channel.history'.
# Can control number of messages to analyze per channel by the 'limit' param
async def message_extractor_helper(file, channel):
    if debug: print("in message_extractor_helper")
    async for message in channel.history(limit=10000):
        if message_debug:
            print(message.author.id)
            #print(message.content)
        if message.author.id == USER_ID: 
            if content_debug: print(message.content)
            file.write(message.content + "\n")
    if message_debug: print('-----------------------------')

async def long_message_extractor_helper(file, channel):
    if debug: print("in long_message_extractor_helper")
    async for message in channel.history(limit=20000):
        if message_debug:
            print(message.author.id)
            #print(message.content)
        if message.author.id == USER_ID: 
            if content_debug: print(message.content)
            file.write(message.content)
    if message_debug: print('-----------------------------')

    # Writing into a txt file using Python: https://blog.enterprisedna.co/python-write-to-file/

# A function to respond to a given message with some generated text.
async def respond(client, message):
    if debug: print("in respond")
    context = message.content.replace('<@1186775215892598795>', '')
    context = context.strip()
    if respond_debug: print('context: ' + context)
    await model.generate_text(USER_NAME, message, context)
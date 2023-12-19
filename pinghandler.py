debug = True

import os

import discord
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

def ping_handler(client, message):
    if "extract_message" in message.content:
        andrew_message_extractor(client)

def andrew_message_extractor(client):
    guild = discord.utils.get(client.guilds, name=GUILD)
    for channel in guild.channels:
        for 
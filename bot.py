# base tutorial: https://realpython.com/how-to-make-a-discord-bot-python/
debug = True

import os

import discord
from dotenv import load_dotenv

import pinghandler

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# A Client is an object that represents a connection to Discord. A Client handles events, 
# tracks state, and generally interacts with Discord APIs
# modified: https://stackoverflow.com/questions/73421068/client-discord-client-typeerror-client-init-missing-1-required-keywor
client = discord.Client(intents=discord.Intents.default())

# handles the event when the Client has established a connection to Discord and it has finished 
# preparing the data that Discord has sent, such as login state, guild and channel data, and more
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    # client.guilds: SequenceProxy(dict_values([<Guild id=711036166257770517 name='milk' shard_id=0 chunked=False member_count=80>]))
    guild = discord.utils.get(client.guilds, name=GUILD)
    
    if debug:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

    channels = []
    for channel in guild.channels:
        channels.append(channel.name)

    if debug:
        print(f'{client.user} can see the following channels:\n')
        for name in channels:
            print(name)

@client.event
async def on_message(message):
    if debug: print(message.content)
    if message.author == client.user:
        return
    pinghandler.ping_handler(message)

client.run(TOKEN)
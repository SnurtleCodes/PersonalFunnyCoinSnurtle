import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import requests
import os



BOT_PREFIX = ("!")
TOKEN = 'NTk1NzUwNjAzNjUzNzc1Mzkz.XRviFw.9F_Lohwz4sRccgS8Gp9YQl9lshw'

client = discord.Client()
client = Bot(command_prefix=BOT_PREFIX)

@client.command()
async def wasitfunny():
    possible_responses = [
        "Per the judgement from the committee of comedy, we have decided that the joke was indeed funny",
        "Per the judgement from the committee of comedy, we have decided that the joke was not fucking funny you cretin",
        ]
    await client.say(random.choice(possible_responses))

@client.command()
async def isitfunny(funny_subject):
    responses = [
        "Nah that wasn't really funny",
        "There is no funny present",
        "YOU FORGOT THE FUNNY",
        "There is no comedy present here",
        "hahaaaaa",
        "Funnt",
        "Hey man that's pretty funny thanks for sharing",
        "jajajajajajajajajaja",
        ]
    await client.say("regarding " + str(funny_subject) + ", " + random.choice(responses))


@client.command()
async def isitironic(irony_subjects):
    irony_responses = [
        "one irony point",
        "that's pretty ironic man",
        "ironic",
        "no irony present",
        "minus irony point",
        "where is the irony? I was told there would be irony?",
        ]
    await client.say(random.choice(irony_responses))

afc = 0
mfc = 0
cfc = 0
anfc = 0


@client.command()
async def alexfc(anum):
    global afc
    afc = afc + int(anum)
    await client.say("Alex has " + str(afc) + " funny coins")

@client.command()
async def muhfc(mnum):
    global mfc
    mfc = mfc + int(mnum)
    await client.say("Muhammad has " + str(mfc) + " funny coins")

@client.command()
async def chrisfc(cnum):
    global cfc
    cfc = cfc+ int(cnum)
    await client.say("Chris has " + str(cfc) + " funny coins")

@client.command()
async def antfc(anthnum):
    global anfc
    anfc = anfc + int(anthnum)
    await client.say("Anthony has " + str(anfc) + " funny coins")

    


client.run(str(os.environ.get(TOKEN)))

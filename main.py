#-----------------------------------------------------------------------------
# Name:        Discord_Bot (python.py)
# Purpose:     To be a bot
#
# Author:      Ethan Wang
# Created:     24-Nov-2018
# Updated:     24-Nov-2018
#-----------------------------------------------------------------------------

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import time

bot = commands.Bot(command_prefix='?')
TOKEN = os.environ['TOKEN']

frames_path = '/Users/EthanWang/Discord_Bot/frames.txt'

@bot.event
async def on_ready():
    print("My name is " + bot.user.name)


@bot.event
async def on_message(message):

    input = message.content

    # Counter Mr. Seidel bot
    if input.startswith("**Hey!**"):
        await bot.send_message(message.channel, "**HeY!** yOu cAn'T sEnd ThAT meSsaAgGe hERe! COnfIdENcE: 69%")

    # Help centre
    if input.startswith("?help"):
        await bot.send_message(message.channel, "kys")

    # Prevent overriding
    await bot.process_commands(message)

@bot.command()
async def surgery(arg1):
    # Surgery meme
    first_letter = arg1[0:1]
    if first_letter in ['a', 'e', 'i', 'o']:
        await bot.say("they did surgery on an " + arg1)
    elif first_letter == '@':
        await bot.say("they did surgery on " + arg1)
    else:
        await bot.say("they did surgery on a " + arg1)

@bot.command()
async def say(arg1):
    # Sends message to general text channel
    await bot.send_message(discord.Object(id='515992928246824963'), arg1)

@bot.command()
async def display():
    frame = ''
    count = 0
    while count < len(frame[4].rstrip()):
        with open(frames_path, 'r') as file:
            data = file.readlines()
            data[4] += 'O'
            for line in data:
                frame += line
        await bot.say(frame)
        count += 1

@bot.command()
async def tax(price):
    n = float(price)
    await bot.say("$" + format(n, '.2f') + " + HST 13% = $" + format(n, '.2f') + " + $" +
                  format(round(n*0.13, 2), '.2f') + " = $" + format(round(n*1.13, 2), '.2f'))

@bot.command()
async def sum(*args):
    sum = 0
    for arg in args:
        sum += float(arg)
    await bot.say("sum = " + str(sum))

@bot.command()
async def dif(arg1, arg2):
    await bot.say(arg1 + " - " + arg2 + " = " + str(float(arg1) - float(arg2)))

@bot.command()
async def vsound(temp):
    await bot.say("the speed of sound at " + temp + "C is " + str(331.4 + 0.606*float(temp)) + "m/s")




bot.run(TOKEN)
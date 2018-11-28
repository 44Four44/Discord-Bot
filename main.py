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
    await bot.change_presence(game=discord.Game(name="with sand", type=1))

down_votes = ['project management', 'compsci', 'comp sci', 'emerging tech', 'main program', 'culminating', 'exam']

@bot.event
async def on_message(message):

    input = message.content

    # Help centre
    if input.startswith("?help"):
        await bot.send_message(message.channel, "kys")

    # Downvote
    if any(x in input for x in down_votes):
        await bot.add_reaction(message, '👎')

    # Prevent overriding
    await bot.process_commands(message)

@bot.event
async def on_member_update(before, after):
    if str(after.status) == "offline":
        await bot.send_message(discord.Object(id='515992928246824963'), "{} died ;-;".format(after.name))
    if str(after.status) == "online":
        await bot.send_message(discord.Object(id='515992928246824963'), "welcome back {}".format(after.name))

@bot.event
async def on_message_edit(before, after):
    await bot.send_message(after.channel, "nice typo")


@bot.event
async def on_message_delete(message):
    await bot.send_message(message.channel, "i saw that")


@bot.command()
async def surgery(object):
    # Surgery meme
    first_letter = object[0:1]
    if first_letter in ['a', 'e', 'i', 'o']:
        await bot.say("they did surgery on an " + object)
    elif first_letter == '@':
        await bot.say("they did surgery on " + object)
    else:
        await bot.say("they did surgery on a " + object)

@bot.command()
async def say(arg1):
    # Sends message to general text channel
    await bot.send_message(discord.Object(id='515992928246824963'), arg1)

@bot.command()
async def display():
    frame = ''
    count = 0
    while count < 202:
        frame += 'O'
        await bot.say(frame)
        count += 1
        time.sleep(0.5)

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
    await bot.say("the speed of sound at " + temp + "°C is " + str(331.4 + 0.606*float(temp)) + "m/s")

@bot.command()
async def kms():
    await bot.say("─────────────────▄▄█▀▀▀▀▀▀▀▄▄─\n"
                  "───────────────▄█▀░░░░░░░░░░▀▀\n"
                  "─────────────▄█▀░░░░░░░░░░░░░░\n"
                  "────────────▄▀░░░░░░░░░░░░░░░░\n"
                  "──────────▄█░░░░░░▄░░░░░░░░▄░░\n"
                  "──────────█░░░░░░█▀█░░░░░░█▀█░\n"
                  "─────▄───█░░░░░░░█─█░░░░░░█─█░\n"
                  "─▄█▀██▀▄▄▀░░░░░░░█─█░░░░░░█─█░\n"
                  "▀▒▒▒▒▒▀█▀▄▄░░░░░░███░░░░░░███░\n"
                  "▒▒▄▄▄▒▒█▓▓▀▀█▄░░░███░░░░░░███░\n"
                  "▒▄███▄▒█▓▓▓▓▓▀█▄░█▓█░░░░░░█▓█░\n"
                  "▒█████▒█▓▓▓▓▓▓▓▀██▓█░░░░░░█▓█░\n"
                  "▒▀███▀▒█▓▓▓▓▓▓▓▓█▀█▀░░░░░░▀█▀░\n"
                  "▄▒▀▀▀▒█▄▄▄▄▓▓▓▓▓█░░░░░░░░░░░░░\n"
                  "▀▄▒▒▒▒▄▀▀████▄▄▄█░░░░░░░░░░░░░\n"
                  "█▒▒▒▒▒█▓▓▓▓▓▓▀▀▀█░░░░░░░░░░░░░\n"
                  "█▒▒▒▒█▀▓▓▓▓▓▓▓▓▓█░█░░░░░░░░█░░\n"
                  "█▒▀▀▒█▓▓▓▓▓▓▓▓▓▄▀░██▄▄░░▄▄██░░\n"
                  "█▒▒▒▒█▓▓▓█▓▓▓▓▓█▄░░▀▀████▀▀░░░\n"
                  "─█▄▄██▄▄▄▀▓▓▓▓▓█▀▄░░░░░░░░░░░░\n"
                  "───█▀▄▓▓▄▄▓▓▓▓▓█░░█░░░░░░░░░░░\n"
                  "───█░█▓█░░█▄▓▓█░░░█░░░░░░░░░░░\n"
                  "───█░█▓█░░░█▓▓█░░▄▀░░░░░░░░░░░\n"
                  "───▀▄█▓█▄▀▀█▓▓█░█░░░░░░░░░░░░░\n"
                  "───▄▄█▓▓▀▀▀▄▄▀█▄▀▄░░░░░░░░░░░░\n"
                  "─▄▀▒▒▒█▀▀▀▀░▄▀██░█░░░░░░░░░░░░\n"
                  "▄▀▒▒▒▒█░░░░░█▄▀▀█▀░░░░░░░░░░░░")


@bot.command()
async def bomb(start_time):
    count = int(start_time)
    while count > 0:
        await bot.say(":bomb:{}".format(count))
        count -= 1
        time.sleep(1)
    await bot.say("boom.")


@bot.command()
async def shoot(member: discord.Member):
    await bot.say("{},:gun: you've been shot at! Quick, type 'duck'".format(member.mention))
    msg = await bot.wait_for_message(timeout=2, author=member, content='duck')
    if msg:
        await bot.say("whew, that was a close one")
    else:
        await bot.say("You've been killed! you snooze you lose")

bot.run(TOKEN)
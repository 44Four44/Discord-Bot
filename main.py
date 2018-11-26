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

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print("My name is " + bot.user.name)

bot.run("NTE1OTg5OTAwNTQ2NTM5NTMw.Dt0Lqw.6AWESViOUJv8Fom5Hb_9Dm46Y8A")

#!/usr/bin/python3.9

import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

# loading environment config
load_dotenv(dotenv_path=".config")

# getting discord bot token
token = os.getenv("TOKEN")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
        print(f'Logged on as {bot.user}!')

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}') # print message
    await bot.process_commands(message) ## needed to prossess commands cause we are overriding on_message method !!
    ## do not remove pls (aman never remove this !!!!!)
    # without it i was going crazy

# sample test command
@bot.command()
async def test(ctx):
    await ctx.send('/tts Bitch \nlol')

# running bot
bot.run(token)

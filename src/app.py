#!/usr/bin/python3.9
from config import bot, token, asyncio
from commands import ping
from commands import echo
from commands import purge
from commands import kick_mute_ban

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}') # print message
    await bot.process_commands(message) ## needed to prossess commands cause we are overriding on_message method !!
    ## do not remove pls (aman never remove this !!!!!)
    # without it i was going crazy

# running bot
bot.run(token)

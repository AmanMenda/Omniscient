#!/usr/bin/python3.9
import os
from config import bot, token, info_channel, discord
from commands import ping
from commands import echo
from commands import purge
from commands import kick

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}') # print message
    await bot.process_commands(message) ## needed to prossess commands cause we are overriding on_message method !!
    ## do not remove pls (aman never remove this !!!!!)
    # without it i was going crazy

#Messages pas encore personnalisables
@bot.event
async def on_member_join(member: discord.Member):
    guild = member.guild
    #system_channel utilise le channel defini pour recevoir des messages systemes.
    #Si il n'est pas defini, on doit envoyer le message dans un channel random
    if guild.system_channel is not None:
        message = f"Welcome {member.mention} to {guild.name} !"
        await guild.system_channel.send(message)

@bot.event
async def on_member_remove(member: discord.Member):
    guild = member.guild
    if guild.system_channel is not None:
        message = f"Bye Bye {member.mention}"
        await guild.system_channel.send(message)
# running bot
bot.run(token)

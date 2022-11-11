from config import *

@bot.event
async def on_member_remove(member: discord.Member):
    guild = member.guild
    if guild.system_channel is not None:
        message = f"Bye Bye {member.mention}"
        await guild.system_channel.send(message)
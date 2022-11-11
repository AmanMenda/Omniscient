import discord
from config import bot
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


# @bot.command()
# @has_permissions(mute_members=True)
# async def mute(ctx, member: discord.Member):
#     counter = 0
#     with open("spam_detect.txt", "r+") as file:
#         for line in file:
#             if line.strip("\n") == str(ctx.author.id):
#                 counter += 1
#         file.writelines(f"{ctx.author.id}\n")
#         if counter > 8:
#             await ctx.send(f"Can't mute this user")

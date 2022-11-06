import discord
from config import bot
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

import discord
from config import bot
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

#check if the person who is using this command is an admin
@bot.command(name='kick', hidden=True, help="Kick a member")
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.author.top_role.permissions.administrator:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked. `Reason:` {reason}")
    else:
        await ctx.send("Only admins can kick members")

@kick.error
async def kick_err(ctx, error):
    if isinstance(error, commands.Forbidden):
        await ctx.send(f"You have not given the bot proper permissions to kick members")



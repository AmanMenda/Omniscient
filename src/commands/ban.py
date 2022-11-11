import discord
from config import bot
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

#Ban a member
@bot.command(hidden=True, help="Ban a member")
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author.top_role.permissions.administrator:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned. `Reason:` {reason}")
    else:
        await ctx.send("Only admins can ban members")

@ban.error
async def ban_err(ctx, error):
    if isinstance(error, commands.Forbidden):
        await ctx.send(f"You have not given the bot proper permissions to ban members")


#unban a banned member
@bot.command(hidden=True, help="Unban a member")
async def unban(ctx, member: discord.Member, *, reason=None):
    if ctx.author.top_role.permissions.administrator:
        await member.unban(reason=reason)
        await ctx.send(f"{member.mention} has been unbanned.")
    else:
        await ctx.send("Only admins can unban members")

@unban.error
async def unban_err(ctx, error):
    if isinstance(error, commands.Forbidden):
        await ctx.send(f"You have not given the bot proper permissions to unban members")

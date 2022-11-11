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

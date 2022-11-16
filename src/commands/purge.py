from config import bot, commands
from config import asyncio

@bot.command(help="Delete a number n of messages")
@commands.has_permissions(manage_messages=True)
async def purge(ctx, n: int):
    if n == 0:
        await ctx.channel.send(limit=n + 1)
        return await ctx.channel.send(f"Please, provide a valid number")
    messages_history = [message async for message in ctx.channel.history(limit=n + 1)]
    if (len(messages_history) < n + 1):
        return await ctx.send("Not enough messages to delete !")
    else:
        deleted = await ctx.channel.purge(limit=n + 1)
        return await ctx.send(f"`!purge` used by {ctx.author.mention}")

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.Forbidden):
        await ctx.send(f"You do not have proper permissions to delete the message")
    elif isinstance(error, commands.NotFound):
        await ctx.send(f"The message has already been deleted")
    else:
        await ctx.send(f"Deleting the message failed")
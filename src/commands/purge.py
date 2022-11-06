from config import bot, commands
from config import has_permissions, MissingPermissions

@bot.command()
@has_permissions(manage_messages=True)
async def purge(ctx, n: int):
    messages_history = [message async for message in ctx.channel.history(limit=n + 1)]
    for message in messages_history:
        await message.delete()
    await ctx.send(f"`!purge` used by {ctx.author.mention}")

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.Forbidden):
        await ctx.send(f"You do not have proper permissions to delete the message")
    elif isinstance(error, commands.NotFound):
        await ctx.send(f"The message has already been deleted")
    else:
        await ctx.send(f"Deleting the message failed")
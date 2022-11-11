from config import bot

@bot.command(help="Work as the echo command in bash")
#keyword-only arg (*,...) allows us to take whatever come after the echo command as one arg
async def echo(ctx, *, args):
    await ctx.send(args)

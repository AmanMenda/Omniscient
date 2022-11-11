from config import commands
from .help import HelpCommand

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        help_command = HelpCommand()
        help_command.cog = self
        bot.help_command = help_command

async def setup(bot: commands.Bot):
    await bot.add_cog(HelpCog(bot))
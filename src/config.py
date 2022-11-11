import os
import discord, asyncio
from dotenv import load_dotenv
from discord.ext import commands
from commands.help_module.help import HelpCommand
from commands.help_module.helpCog import HelpCog, setup

# loading environment config
load_dotenv(dotenv_path=".config")

# getting discord bot token
token = os.getenv("TOKEN")
info_channel = os.getenv("INFO_EVENT_CHANNEL")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
bot.help_command = HelpCommand()

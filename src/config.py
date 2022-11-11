import os
import discord, asyncio
from dotenv import load_dotenv
from discord.ext import commands    
from help.help import Help
from help.helpCog import HelpCog, setup

# loading environment config
load_dotenv(dotenv_path=".config")

# getting discord bot token
token = os.getenv("TOKEN")
info_channel = os.getenv("INFO_EVENT_CHANNEL")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
bot.help_command = Help()

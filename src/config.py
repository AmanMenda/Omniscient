import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

# loading environment config
load_dotenv(dotenv_path=".config")

# getting discord bot token
token = os.getenv("TOKEN")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
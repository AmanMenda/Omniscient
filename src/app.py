#!/usr/bin/python3.9
import os
from config import *
from commands import ping
from commands import purge
from commands import kick
from commands import kick_mute_ban
from events import on_member_join
from events import on_member_remove
from events import on_message
from events import on_ready

# running bot
bot.run(token)

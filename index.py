import os
import discord
import asyncio

from discord.ext.commands import DefaultHelpCommand
from data import Bot
from utils import permissions, default
from utils.data import Bot, HelpFormat
from datetime import datetime

client = discord.Client()

config = default.get("config.json")
description = """
Fuck me - Ahiga - AKA Big Cock Hammer- AKA Drunk fucking sad lowlife - AKA Big chief.
"""

bot = Bot(
    command_prefix=config.prefix,
    prefix=config.prefix,
    command_attrs=dict(hidden=True),
    help_command=HelpFormat(),
    message_list = {}
)

print("Purging fags...")
#bot = Bot(command_prefix=config.prefix, prefix=config.prefix, command_attrs=dict(hidden=True), help_command=HelpFormat())
bot.startup = datetime.now()

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

bot.run(config.token)

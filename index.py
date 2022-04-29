import os
import io
import discord
import asyncio
import contextlib
import textwrap
import json

from pathlib import Path
from discord.ext.commands import DefaultHelpCommand
from data import Bot
from utils import permissions, default, repo
from utils.evalutil import clean_code, Pag
from utils.data import Bot, HelpFormat
from datetime import datetime
from discord.ext import commands 
from discord import utils

client = discord.Client()

config = default.get("config.json")
description = """
Fuck me - Ahiga - AKA Big Cock Hammer- AKA Drunk fucking sad lowlife - AKA Big chief.
"""

intents = discord.Intents.all()
print("Intents loaded")

bot = Bot(
    command_prefix=commands.when_mentioned_or('.'),
    prefix=config.prefix,
    command_attrs=dict(hidden=True),
    help_command=HelpFormat(),
    message_list = {},
    intents = intents
)

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd} loaded")
bot.blacklisted_users = []

print("Purging fags...")
bot.startup = datetime.now()

@bot.command(name="eval")
@commands.check(repo.is_owner)
async def _eval(ctx, *, code):
    code = clean_code(code)

    local_variables = {
        "discord": discord,
        "commands": commands,
        "bot": bot,
        "ctx": ctx,
        "channel": ctx.channel,
        "author": ctx.author,
        "guild": ctx.guild,
        "message": ctx.message
    }

    stdout = io.StringIO()

    try:
        with contextlib.redirect_stdout(stdout):
            exec(
                f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,
            )

            obj = await local_variables["func"]()
            result = f"{stdout.getvalue()}\n-- {obj}\n"
    except Exception as e:
        result = f"{e}"

    pager = Pag(
        timeout=100,
        entries=[result[i: i + 2000] for i in range(0, len(result), 2000)],
        length=1,
        prefix="```py\n",
        suffix="```"
    )

    await pager.start(ctx)

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.author.id == bot.user.id:
        return
    if message.author.id in bot.blacklisted_users:
        return
    if discord.utils.get(message.author.roles, name="Hardmute") != None:
        await message.delete();
        return
    await bot.process_commands(message)

@bot.command()
async def blacklist(ctx, member: discord.User):
    if ctx.author.id in config.owners:
        bot.blacklisted_users.append(member.id)
        data = read_json("blacklist")
        data["blacklistedUsers"].append(member.id)
        write_json(data, "blacklist")
        await ctx.send(f"Blacklisted **{member.name}**")

@bot.command()
async def whitelist(ctx, member: discord.User):
    if ctx.author.id in config.owners:
        bot.blacklisted_users.append(member.id)
        data = read_json("blacklist")
        data["blacklistedUsers"].remove(member.id)
        write_json(data, "blacklist")
        await ctx.send(f"Whitelisted **{member.name}**")

def read_json(filename):
    with open(f"{cwd}/{filename}.json", "r") as file:
        data = json.load(file)
    return data
def write_json(data, filename):
    with open(f"{cwd}/{filename}.json", "w") as file:
        json.dump(data, file, indent=4)

bot.run(config.token)

import discord
import traceback
import psutil
import os
import urllib.request
import re

from io import BytesIO
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import errors
from utils import default
from bs4 import BeautifulSoup
from asyncio import sleep
from utils import lists, permissions, http, default


async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        await ctx.send_help(str(ctx.invoked_subcommand))
    else:
        await ctx.send_help(str(ctx.command))


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_command_error(self, ctx, err):
        if isinstance(err, errors.MissingRequiredArgument) or isinstance(err, errors.BadArgument):
            await send_cmd_help(ctx)

        elif isinstance(err, errors.CommandInvokeError):
            err = err.original

            _traceback = traceback.format_tb(err.__traceback__)
            _traceback = ''.join(_traceback)
            error = ('```py\n{2}{0}: {3}\n```').format(type(err).__name__, ctx.message.content, _traceback, err)

            embed = discord.Embed(color=7091547)
            embed.description = f'{error}'
            await ctx.send(embed=embed)

        elif isinstance(err, errors.CheckFailure):
            pass

        elif isinstance(err, errors.CommandOnCooldown):
            #await ctx.send(f"This command is on cooldown... try again in {err.retry_after:.2f} seconds.")
            return

        elif isinstance(err, errors.CommandNotFound):
            pass

def setup(bot):
    bot.add_cog(ErrorHandler(bot))

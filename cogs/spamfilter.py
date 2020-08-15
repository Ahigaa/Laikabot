import discord
import traceback
import psutil
import os
import aiohttp
import random

from discord.ext import commands
from discord.ext.commands import errors
from utils import default
from utils import lists, permissions, http, default, antispam
from discord import Webhook, AsyncWebhookAdapter


async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        await ctx.send_help(str(ctx.invoked_subcommand))
    else:
        await ctx.send_help(str(ctx.command))


class SpamFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())
 
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
                return
        else:
            self.bot.loop.create_task(antispam.addSpamCounter(user = message.author, bott = self.bot))
            self.bot.loop.create_task(antispam.reduceSpamCounter(user = message.author, bott = self.bot))



def setup(bot):
    bot.add_cog(SpamFilter(bot))
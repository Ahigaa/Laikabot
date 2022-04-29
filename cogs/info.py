import time
import discord
import psutil
import os
import datetime
import random

from asyncio import sleep
from datetime import datetime
from discord.ext import commands
from utils import repo, default, lists

def f_time(time):
    h, r = divmod(int(time.total_seconds()), 3600)
    m, s = divmod(r, 60)
    d, h = divmod(h, 24)

    return "%02d:%02d:%02d:%02d" % (d, h, m, s)

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        """ Pong! """
        ans = random.choice(lists.ping)
        before = time.monotonic()
        message = await ctx.send("Pong")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pinged {ans}   |   {int(ping)}ms")

    @commands.command(aliases=['info', 'stats', 'status', 'serveruse'])
    @commands.guild_only()
    async def about(self, ctx):
        """ About the bot """
        ramUsage = self.process.memory_full_info().rss / 1024**2
        avgmembers = round(len(self.bot.users) / len(self.bot.guilds))
        uptime = f_time(datetime.now() - self.bot.startup)
        embedColour = ctx.me.top_role.colour

        embed = discord.Embed(colour=embedColour)
        embed.add_field(name="🔌 Last boot", value=default.timeago(datetime.now() - self.bot.uptime), inline=False)
        embed.add_field(name=u'🕓 Uptime', value=uptime + "\n\u200b", inline=False)
        embed.add_field(
            name=f"⚙ Developer{'' if len(self.config.owners) == 1 else 's'}",
            value=', '.join([str(self.bot.get_user(x)) for x in self.config.owners]),
            inline=True)
        embed.add_field(name="🧬 Library", value="discord.py", inline=True)
        embed.add_field(name="⚔️ Servers", value=f"{len(ctx.bot.guilds)} ( avg: {avgmembers} users/server )", inline=True)
        embed.add_field(name="💾 Commands loaded", value=len([x.name for x in self.bot.commands]), inline=True)
        embed.add_field(name="🔥 RAM", value=f"{ramUsage:.2f} MB", inline=True)
        embed.add_field(name='⏱ Latency', value=f'{round(self.bot.latency * 1000)} ms', inline=True)

        await ctx.send(content=f"ℹ About **{ctx.bot.user}** | **{repo.version}**", embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))

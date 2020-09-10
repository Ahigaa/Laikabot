import discord
import traceback
import psutil
import os
import urllib.request
import re
import random
import asyncio
import aiohttp

from io import BytesIO
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import errors
from utils import default
from bs4 import BeautifulSoup
from asyncio import sleep
from utils import lists, permissions, http, default
from discord import Webhook, AsyncWebhookAdapter

async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        await ctx.send_help(str(ctx.invoked_subcommand))
    else:
        await ctx.send_help(str(ctx.command))


async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        await ctx.send_help(str(ctx.invoked_subcommand))
    else:
        await ctx.send_help(str(ctx.command))

class Blacklisted(commands.CheckFailure): pass

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    def bot_check_once(self, ctx):
        blacklist = default.get("config.json").blacklist
        if ctx.author.id in blacklist:
            raise Blacklisted()
        else:
            return True

    async def on_command_error(self, ctx, error):
        if isinstance(error, Blacklisted):
            await ctx.send("You cannot use this command.")

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_guild_join(self, guild):
        if not self.config.join_message:
            return

        try:
            to_send = sorted([chan for chan in guild.channels if chan.permissions_for(guild.me).send_messages and isinstance(chan, discord.TextChannel)], key=lambda x: x.position)[0]
        except IndexError:
            pass
        else:
            await to_send.send(self.config.join_message)

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_command(self, ctx):
        try:
            print(f"{ctx.guild.name} > {ctx.author} > {ctx.message.clean_content}")
        except AttributeError:
            print(f"Private message > {ctx.author} > {ctx.message.clean_content}")

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_ready(self):
        if not hasattr(self.bot, 'uptime'):
            self.bot.uptime = datetime.utcnow()

        print(f'Ready: {self.bot.user} | Servers: {len(self.bot.guilds)} | Members: {len(set(self.bot.get_all_members()))}')
        await self.bot.change_presence(activity=discord.Activity(name=f'{self.config.playing}', type=discord.ActivityType.streaming, url='https://www.twitch.tv/search?term=fucking%20go%20to%20https%3A%2F%2Finitiate.space%2F%20faggot'))

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_member_join(self, member):
        try:
            channel = self.bot.get_user(member.id)
            embed = discord.Embed(color=0x21d3f3)
            embed.description = f"RULES:\n\n» 0.   Love Lain.\n» 1.   Respect the channel topic. Erotic content goes in #⁄h⁄.\n» 2.   Lolicon, shotacon, child pornography, scatological pornography, and guro are not permitted on INITIATE.\n» 3.   Respect the Discord Terms of Service at all times.n» 4.   Do not cause harm to INITIATE or any of it's close affiliates or one of the members of it's community be it through Doxxing, Hacking, Account Hijacking or any other applicable reasons.\n» 5.   Lewding Lain is ban and considered the greatest sin.\n» 6.   Please do not bring systemspace drama here! We would like everyone to have a new beginning!\n» 7.   Please keep shitposting to a minimum in #degeneral ! excessive shitposting goes in #indica \n» 8.   Keep your trannyposting in DMs! Talking like a fucking queer is just fine, just no pics.\n» 9.   Non of that animal roleplay/cosplay or whatever the fuck furries do.\n» 10. For the love of god don't fucking beg for mod you hypercuck!\n» 11. No thots and remember to violate human rights!\n» 12. Use common sense when posting. If you think something is not alright to post in for example #degeneral then it most likely isn't.\n» 13. Please read https://initiate.space/omniverse/ while you're at it! (optional)"
            await channel.send(embed=embed)
        except Exception as e:
            return

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message):
        if ". irid" in message.content:
            await message.delete()
    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message):
        if ".irid" in message.content:
            await message.delete()

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message):
        user = message.author
        channelid = message.channel.name
        if channelid == "verification":
            if discord.utils.get(user.roles, name="Heimdallar") != None:
                return
            elif "@" in message.content:
                return
            else:
                await message.delete()
        elif discord.utils.get(user.roles, name="Muted") != None:
            await message.delete()


    #Message logger for backup server (general)
    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message):
        if "irid" in message.content:
            return
        user = message.author
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('Webhook goes here', adapter=AsyncWebhookAdapter(session))
            username = message.author.display_name
            pfp = message.author.avatar_url_as(size=1024)
            await webhook.send(f'{message.content}', username=str(username), avatar_url=str(pfp))



    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message):
        if "color" in message.content:
            return
        elif "#" in message.content:
            color = message.content
            color = color.replace("#","")
            #await message.channel.send(f"{color}")
            try:
                r = await http.get(f"https://api.alexflipnote.dev/colour/{color}", res_method="json", no_cache=True)
            except aiohttp.ClientConnectorError:
                return await message.channel.send("The API seems to be down...")
            except aiohttp.ContentTypeError:
                return

            embed = discord.Embed(color=r["int"])
            embed.set_thumbnail(url=r["image"])
            embed.set_image(url=r["image_gradient"])

            embed.add_field(name="HEX", value=r['hex'], inline=True)
            embed.add_field(name="RGB", value=r['rgb'], inline=True)
            embed.add_field(name="Int", value=r['int'], inline=True)
            embed.add_field(name="Brightness", value=r['brightness'], inline=True)

            await message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Events(bot))

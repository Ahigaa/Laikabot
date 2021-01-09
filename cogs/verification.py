import time
import discord
import psutil
import os
import json
import urllib.request
import random
import sqlite3
import re
import aiohttp

from datetime import datetime
from discord.ext import commands
from io import BytesIO
from utils import repo, default, lists, http, dataIO
from discord import Permissions

from discord.utils import get

class verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.process = psutil.Process(os.getpid())
        self.config = default.get("config.json")
        self._last_result = None

    @commands.guild_only()
    @commands.command()
    async def irid(self, ctx, *, fuckingid: str):
        """ IRID [your irid] """

        DB_NAME = "database name goes here"
        db_path = os.path.abspath("database path goes here" + DB_NAME + ".db")
        print(f"{db_path}")
        self.db = sqlite3.connect(db_path)
        self.db_cursor = self.db.cursor()

        self.db_cursor.execute("SELECT * FROM user WHERE active=1 AND irid=?", (fuckingid,))
        ID = fuckingid
        guild = ctx.guild
        channel = self.bot.get_channel(set channel id here)
        usr = ctx.message.author
        response = self.db_cursor.fetchone()
        if response:
            role = discord.utils.get(ctx.guild.roles, name="-online-")
            await usr.add_roles(role)
            try:
                self.db_cursor.execute("UPDATE `user` SET `discordTag` = '" + str(usr) + "' WHERE `user`.`irid` = '" + str(fuckingid) + "'")
                self.db.commit()
                self.db.close()
            except Exception as e:
                await ctx.send(f"Could not insert into table!")
                self.db.close()
        else:
            await ctx.send("User not signed up!")
        await ctx.message.delete()
        self.db.close()

    @commands.guild_only()
    @commands.command(hidden=True)
    @commands.check(repo.is_owner)
    async def showtable(self, ctx):
        """ w """

        DB_NAME = "database name goes here"
        db_path = os.path.abspath("database path goes here" + DB_NAME + ".db")
        print(f"{db_path}")
        self.db = sqlite3.connect(db_path)
        self.db_cursor = self.db.cursor()

        listing = self.db_cursor.execute("SELECT * FROM user")
        response = self.db_cursor.fetchall()
        for row in response:
            embed = discord.Embed(color=7091547, title=f"**__Listing__**")
            #Embed the table here
            await ctx.send(embed=embed)
            self.db.close()
        self.db.close()

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        channel = self.bot.get_channel(set channel id here)
        author_id = str(after.id)

        if len(before.roles) < len(after.roles):
            new_role = next(role for role in after.roles if role not in before.roles)
            if new_role.name in ('-online-'):
                try:
                    embed = discord.Embed(color=0x21d3f3)
                    embed.description = f"{after.mention} just verified!"
                    embed.add_field(name="Account created:", value=default.date(after.created_at), inline=True)
                    embed.add_field(name="Joined this server:", value=default.date(after.joined_at), inline=False)
                    embed.add_field(name="Verification:", value=":white_check_mark: Verified!", inline=False)
                    await channel.send(embed=embed)

                    return await channel.send(f"{after.mention} Change your color by doing .color [hexcode]")
                except Exception as e:
                    await channel.send(f"{e}")


    @commands.command()
    @commands.guild_only()
    async def verify(self, ctx):
        """ Re-verify your IRID """
        try:
            role_names = [role.name for role in ctx.author.roles]
            role_names = role_names[1:]
            for role in role_names:
                fuck = discord.utils.get(ctx.guild.roles, name=f"{role}")
                #await ctx.send(f"{fuck}")
                await ctx.author.remove_roles(fuck)
        except Exception as e:
            await ctx.send(e)


    @commands.command(aliases=['colour'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def color(self, ctx, color: str):
        """ fuck """
        async with ctx.channel.typing():
            if color == "random":
                color = "%06x" % random.randint(0, 0xFFFFFF)

            if color[:1] == "#":
                color = color[1:]

            if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', color):
                return await ctx.send("You're only allowed to enter HEX (0-9 & A-F)")
            cleaned = color.replace("#", "")
            myunendinghate = int(cleaned, 16)
            guild = ctx.guild
            fuckk = str(color)
            try:
                try:
                    rolel = []
                    for role in ctx.author.roles:
                        if "#" in role.name:
                            rolel.append(role.id)
                    roler = discord.Object(id=rolel[0])
                    await ctx.author.remove_roles(roler)
                except:
                    pass
                try:
                    fuckk = f(color)
                    therole = discord.utils.get(ctx.guild.roles, name=f"{fuckk}") 
                    await ctx.author.add_roles(therole)
                    await ctx.message.add_reaction(chr(0x2705))

                except Exception as e:
                    await guild.create_role(name=fuckk, colour=discord.Colour(myunendinghate))
                    therole = discord.utils.get(ctx.guild.roles, name=f"{fuckk}") 
                    await ctx.author.add_roles(therole)
                    await ctx.message.add_reaction(chr(0x2705))

            except Exception as e:
                await ctx.send(e)

def setup(bot):
    bot.add_cog(verification(bot))


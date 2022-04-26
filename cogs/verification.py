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
import base64
import asyncio


from github import Github
from github import InputGitTreeElement

from datetime import datetime, timedelta
from discord.ext import commands, tasks
from io import BytesIO
from utils import repo, default, lists, http, dataIO
from discord import Permissions

from discord.utils import get

async def generate_stats(ctx, days):
    all_members = set(m.id for m in ctx.guild.members)
    active_members = set()

    for channel in ctx.guild.text_channels:

        i = 0
        async for message in channel.history(limit=40000, after=datetime.now() - timedelta(int(days))):
            i += 1
            active_members.add(message.author.id)
        print(i)

    inactive_members = all_members.difference(active_members)
    banned_members = active_members.difference(all_members)

    all_mem = len(all_members)
    act_mem = len(active_members)
    ina_mem = len(inactive_members)
    ban_mem = len(banned_members)
    string = f'**Here are the following statistics for the past {days} day(s):**\n' \
             f'```ALL: {all_mem}\nACTIVE: {act_mem}\nINACTIVE: {ina_mem}\nACTIVE BUT BANNED: {ban_mem}\n```'
    return inactive_members, string

class verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.process = psutil.Process(os.getpid())
        self.config = default.config()


    @commands.Cog.listener()
    async def on_ready(self):
        self.kickinactive.start()

    @tasks.loop(hours=0.8)
    async def kickinactive(self):
        print(f"Counter started")
        channel = self.bot.get_channel(887555256337195008)
        guild = self.bot.get_guild(857815169916993606)
        for member in guild.members:
            if len(member.roles) == 1:
                try:
                    await member.kick()
                    embed = discord.Embed(color=0x1f7eb8)
                    embed.description=(f'⌫ fucking **kicked** {str(member.name)} due to inactivity!')
                    await channel.send(embed=embed)
                except Exception as e:
                    print(f"Could not kick {str(member.name)}")

    @commands.guild_only()
    @commands.command()
    async def stat(self, ctx, days=None):

        msg = await ctx.send(f"**Generating stats..**")

        async with ctx.typing():
            if (not days):
                await ctx.send('You need to specify the amount of days.')
            else:
                inactive_members, string = await generate_stats(ctx, days)

                for member in inactive_members:
                    user = self.bot.get_user(member)
                await msg.delete()
                await ctx.send(string)


    @commands.guild_only()
    @commands.command()
    async def irid(self, ctx, *, fuckingid: str):
        """ IRID [your irid] """
        await ctx.message.delete()

        db_path = f"{self.config['database1']}"
        print(f"{db_path}")
        self.db = sqlite3.connect(db_path)
        self.db_cursor = self.db.cursor()

        self.db_cursor.execute("SELECT * FROM user WHERE active=1 AND irid=?", (fuckingid,))
        ID = fuckingid
        guild = ctx.guild
        channel = self.bot.get_channel(857815170213871625)
        usr = ctx.message.author
        response = self.db_cursor.fetchone()
        if response:
            role = discord.utils.get(ctx.guild.roles, name="-online-")
            await usr.add_roles(role)
            try:
                self.db_cursor.execute("UPDATE `user` SET `discordTag` = '" + str(usr) + "' WHERE `user`.`irid` = '" + str(fuckingid) + "'")
                self.db.commit()

                try:
                    self.db_cursor.execute("SELECT id FROM user WHERE active=1 AND irid=?", (fuckingid,))
                    user = self.db_cursor.fetchone()
                    if user is None:
                        return
                    else:
                        fuckmenigga = ctx.message.author
                        fuckmeniggaw = ctx.message.author.id
                        usernumber = int(user[0])
                        towrite = f"/*{fuckmenigga}*/[user_by_bdfdb*='{fuckmeniggaw}'],[data-user-id*='{fuckmeniggaw}'] {{--fuckingnigger: 'Verified INITIATIVE #{usernumber}'; --verifiedcolor: #49ff59;}}"
                        try:
                            filepath = os.getcwd()
                            with open('/var/www/initiatechan/verified.css', 'a') as file:
                                file.write(f"{towrite}\n")
                            file.close()
                        except Exception as e:
                            print(f'{e}')
                except Exception as e:
                    print(f'{e}')


            except Exception as e:
                await ctx.send(f"Could not insert into table!")
                self.db.close()
        else:
            await ctx.send("You have not verified your id yet!\nPlease head over to your email, and follow the link.")
        return self.db.close()

    @commands.command()
    @commands.guild_only()
    async def capcode(self, ctx):
        """ Sets your cap as the same on the website """
        db_path = f"{self.config['database1']}"
        self.db = sqlite3.connect(db_path)
        member = str(ctx.message.author)
        nickname = str(ctx.message.author.nick)
        self.db_cursor = self.db.cursor()
        self.db_cursor.execute("SELECT * FROM user WHERE discordTag='" + member + "'")
        user = self.db_cursor.fetchone()
        if user:
            try:
                status = user[11]
                newnick = f"{nickname} ## {status}"
                if not status:
                    return
                elif "None" in nickname:
                    nickname = str(ctx.message.author.display_name)
                    newnick = f"{nickname} ## {status}"
                    await ctx.message.author.edit(nick=f"{newnick}")
                else:
                    await ctx.message.author.edit(nick=f"{newnick}")
                    self.db.close()
                    self.db_cursor.close()
            except Exception as e:
                await ctx.send(f'{e}')

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message):
        channelid = message.channel.name
        if channelid != "verification":
            return
        if message.author.bot:
            return

    @commands.command(hidden=True)
    @commands.check(repo.is_owner)
    async def invite(self, ctx):
        """ Invite me to your server """
        await ctx.send(f"**{ctx.author.name}**, use this URL to invite me\n<{discord.utils.oauth_url(self.bot.user.id)}>")

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        channel = self.bot.get_channel(887555256337195008)
        author_id = str(after.id)

        if len(before.roles) < len(after.roles):
            new_role = next(role for role in after.roles if role not in before.roles)
            if new_role.name in ('-online-'):
                if "144096079917350912" in author_id:
                    for w in range(10):
                        await channel.send(f"🥳🎉🎊")
                    await channel.send(f"Welcome back!! 💖 <@{author_id}>")
                try:
                    embed = discord.Embed(color=0x21d3f3)
                    embed.description = f"⌦ {after.mention} joined <:ini_gold:857696098838642709>**IИITIATE** "
                    #embed.add_field(name="Account created:", value=default.date(after.created_at), inline=True)
                    #embed.add_field(name="Joined this server:", value=default.date(after.joined_at), inline=False)
                    embed.add_field(name="Verification:", value=":white_check_mark: Verified!", inline=False)
                    await channel.send(embed=embed)
                    return await channel.send(f"{after.mention} Change your color by doing .color #whatever\nYou can set your capcode by doing .capcode")

                    #return await channel.send(f"{after.mention} Change your color by doing .color [hexcode]")
                except Exception as e:
                    await channel.send(f"{e}")
            if new_role.name in ('-excluded-'):
                try:
                    embed = discord.Embed(color=0x21d3f3)
                    embed.description = f"⌦ {after.mention} joined <:ini_gold:857696098838642709>**IИITIATE** "
                    #embed.add_field(name="Account created:", value=default.date(after.created_at), inline=True)
                    #embed.add_field(name="Joined this server:", value=default.date(after.joined_at), inline=False)
                    embed.add_field(name="Verification:", value=":negative_squared_cross_mark: Not Verified!", inline=False)
                    await channel.send(embed=embed)
                    return await channel.send(f"{after.mention} Change your color by doing .color #whatever")

                    #return await channel.send(f"{after.mention} Change your color by doing .color [hexcode]")
                except Exception as e:
                    await channel.send(f"{e}")


    @commands.Cog.listener()
    @commands.guild_only()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(857815170213871618)
        fuck = str(member)

        try:

            db_path = f"{self.config['database1']}"
            print(f"{db_path}")
            self.db = sqlite3.connect(db_path)
            self.db_cursor = self.db.cursor()

            listing = self.db_cursor.execute("SELECT * FROM user WHERE discordTag='" + fuck + "'")
            response = self.db_cursor.fetchall()
            for row in response:
                embed = discord.Embed(color=7091547, title=f"**__Listing__**")
                embed.description = f"**Num**: {row[0]}\n**UserID**: {row[1]}\n**Email**: {row[2]}\n**IP**: {row[3]}\n**Country**: {row[4]}\n**City**: {row[5]}\n**Active**: {row[6]}\n**Discord**: {row[7]}\n**From**: {row[9]}\nNick: {row[10]}\nStatus: {row[11]}"
                await channel.send(embed=embed)
                self.db.close()
                role = discord.utils.get(member.guild.roles, name="-online-")
                await member.add_roles(role)
            self.db.close()
        except Exception as e:
            await channel.send(f"user not signed up!")



def setup(bot):
    bot.add_cog(verification(bot))


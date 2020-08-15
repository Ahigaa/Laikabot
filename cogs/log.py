import discord
import traceback
import psutil
import os
import urllib.request
import re
import aiohttp

from io import BytesIO
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import errors
from utils import default
from discord import Embed
from discord import Webhook, AsyncWebhookAdapter


async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        await ctx.send_help(str(ctx.invoked_subcommand))
    else:
        await ctx.send_help(str(ctx.command))


class Log(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())
        channel = self.bot.get_channel(Channel id goes here)

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(Channel id goes here)
        embed = discord.Embed(color=0x21d3f3)
        embed.description = f"**{member.mention}** just joined!"
        embed.add_field(name="User Number:", value=len(list(member.guild.members)), inline=False)
        embed.add_field(name="Guild ID:", value=member.guild.id, inline=False)
        embed.add_field(name="Account created:", value=default.date(member.created_at), inline=False)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(Channel id goes here)
        embed = discord.Embed(color=0xae3e41)
        embed.description = f"**{member.mention}** left!"
        embed.add_field(name="User Number:", value=len(list(member.guild.members)), inline=False)
        embed.add_field(name="Guild ID:", value=member.guild.id, inline=False)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_member_ban(self, member):
        channel = self.bot.get_channel(Channel id goes here)
        embed = discord.Embed(color=0xae3e41)
        embed.description = f"**{member.mention}** banned!"
        embed.add_field(name="User Number:", value=len(list(member.guild.members)), inline=False)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_member_unban(self, member):
        channel = self.bot.get_channel(Channel id goes here)
        embed = discord.Embed(color=0x21d3f3)
        embed.description = f"**{member.mention}** got banned!"
        await channel.send(embed=embed)

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_member_update(self, before, after):
        channel = self.bot.get_channel(Channel id goes here)
        gain = [role for role in after.roles if role not in before.roles]
        lost = [role for role in before.roles if role not in after.roles]
        if before.nick != after.nick:
            embed = discord.Embed(title=' ', description=f'{before.mention} **has changed their nickname \nfrom:** `{before.nick}` **to:** `{after.nick}`', color=0x21d3f3)
            await channel.send(embed=embed)
        if lost:
            embed = discord.Embed(title=' ', description=f'**{before.mention}s role has been changed. \nLost the role{"" if len(gain) == 1 else "s"} {", ".join([role.mention for role in lost])}', color=0x21d3f3)
            await channel.send(embed=embed)
        elif gain:
            embed = discord.Embed(title=' ', description=f'**{before.mention}s role has been changed. \nGained the role{"" if len(gain) == 1 else "s"} {", ".join([role.mention for role in gain])}', color=0x21d3f3)
            await channel.send(embed=embed)
        if before.name != after.name:
            embed = discord.Embed(title=' ', description=f'{before.mention} **has changed their username \nfrom:** `{before.name}` **to:** `{after.name}`', color=0x21d3f3)
            await channel.send(embed=embed)
        if before.discriminator != after.discriminator:
            embed = discord.Embed(title=' ', description=f'{before.mention} **has changed their discriminators \nfrom:** `{before.discriminator}` **to:** `{after.discriminator}`', color=0x21d3f3)
            await channel.send(embed=embed)


    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message_delete(self, message):
        guild = message.guild
        author = message.author
        channel = message.channel
        channell = self.bot.get_channel(Channel id goes here)

        embed = discord.Embed(color=0xae3e41)
        avatar = author.avatar_url if author.avatar else author.default_avatar_url
        embed.set_author(name="Message removed", icon_url=avatar)
        embed.add_field(name="Member", value="{0.display_name}#{0.discriminator} ({0.id})".format(author), inline=False)
        embed.add_field(name="Channel", value=channel.name, inline=True)
        embed.add_field(name="Channel ID", value=channel.id, inline=True)
        embed.add_field(name="Message", value=message.content)
        await channell.send(embed=embed)

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message_edit(self, before, after):
        if after.author.bot:
            return
        guild = after.guild
        author = after.author
        channel = after.channel
        channell = self.bot.get_channel(Channel id goes here)

        embed = discord.Embed(color=0x21d3f3)
        avatar = author.avatar_url if author.avatar else author.default_avatar_url
        embed.set_author(name="Message changed", icon_url=avatar)
        embed.add_field(name="Member", value="{0.display_name}#{0.discriminator} ({0.id})".format(author), inline=False)
        embed.add_field(name="Channel", value=before.channel.name, inline=True)
        embed.add_field(name="Channel ID", value=before.channel.id, inline=True)
        embed.add_field(name="Before", value=before.content, inline=False)
        embed.add_field(name="After", value=after.content, inline=False)
        if after.content == str(before.content):
            return
        await channell.send(embed=embed)




    @commands.Cog.listener()
    @commands.guild_only()
    async def on_guild_role_update(self, before, after):
        channel = self.bot.get_channel(Channel id goes here)
        if before.name != after.name:
            embed = discord.Embed(title=' ', description=f"Role **{before.name}** renamed to **{after.name}**", color=0x21d3f3)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_guild_role_create(self, role):
        guild = role.guild
        channel = self.bot.get_channel(Channel id goes here)
        embed = discord.Embed(title=' ', description=f"Role **{role.name}** created!", color=0x21d3f3)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_guild_role_delete(self, role):
        guild = role.guild
        channel = self.bot.get_channel(Channel id goes here)
        embed = discord.Embed(title=' ', description=f"Role **{role.name}** deleted!", color=0xae3e41)
        await channel.send(embed=embed)


    @commands.Cog.listener()
    @commands.guild_only()
    async def on_guild_channel_update(self, before, after):
        channell = self.bot.get_channel(Channel id goes here)
        if before.name != after.name:
            embed = discord.Embed(title=' ', description=f"Channel **{before.name}** renamed to **{after.name}**", color=0x21d3f3)
            await channell.send(embed=embed)

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_guild_channel_create(self, channel):
        guild = channel.guild
        channell = self.bot.get_channel(Channel id goes here)
        embed = discord.Embed(title=' ', description=f"Channel **{channel.name}** created!", color=0x21d3f3)
        await channell.send(embed=embed)

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_guild_channel_delete(self, channel):
        guild = channel.guild
        channell = self.bot.get_channel(Channel id goes here)
        embed = discord.Embed(title=' ', description=f"Channel **{channel.name}** deleted!", color=0xae3e41)
        await channell.send(embed=embed)


def setup(bot):
    bot.add_cog(Log(bot))

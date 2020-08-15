import random
import discord
import json
import secrets
import asyncio
import time
import urllib.request
import re
import requests
import github3

from io import BytesIO
from discord.ext import commands
from asyncio import sleep
from utils import lists, permissions, http, default
from bs4 import BeautifulSoup

message_list = {}

class bg_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")


    @commands.cooldown(1, 20, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def background(self, ctx, *, link: commands.clean_content):
        """ Sets your background for the initiate theme """
        fuckmenigga = ctx.message.author
        fuckmeniggaw = ctx.message.author.id
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        await ctx.message.delete()
        towrite = f"/*{fuckmenigga}*/[user_by_bdfdb*='{fuckmeniggaw}'],[data-user-id*='{fuckmeniggaw}'] {{--user-background: url({link});}}"
        try:
            with open('discordbg.css', 'a') as file:
                file.write(f"{towrite}\n")
            file.close()

            file_info = 'discordbg.css'

            gh = github3.login(username='username goes here', password='password goes here')
            repository = gh.repository('username goes here', 'repo name goes here')
            with open('discordbg.css', 'rb') as fd:
                contents = fd.read()
            contents_object = repository.file_contents(file_info)
            contents_object.update('Automatic update',contents)
            await ctx.message.add_reaction(chr(0x2705))

        except Exception as e:
            await ctx.send(f"error {e}")

    @commands.cooldown(1, 20, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def cap(self, ctx, *, text: str):
        """ Sets your capcode for the initiate theme """
        try:
            fuckmenigga = ctx.message.author
            fuckmeniggaw = ctx.message.author.id
            if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
                return
            await ctx.message.delete()
            towrite = f"""/*{fuckmenigga}*/ .avatar-1BDn8e[src*='{fuckmeniggaw}'] + h2 > span.username-1A8OIy.da-username.clickable-1bVtEA.da-clickable.focusable-1YV_-H.da-focusable::after {{ content: ' ## {text}';}}"""
            #await ctx.send(f'{towrite}')
            try:
                with open('discordcapp.css', 'a') as file:
                    file.write(f"{towrite}\n")
                file.close()

                file_info = 'discordcapp.css'

                gh = github3.login(username='username goes here', password='password goes here')
                repository = gh.repository('username goes here', 'repo name goes here')
                with open('discordcapp.css', 'rb') as fd:
                    contents = fd.read()
                contents_object = repository.file_contents(file_info)
                contents_object.update('Automatic update',contents)
                await ctx.message.add_reaction(chr(0x2705))

            except Exception as e:
                await ctx.send(f"error {e}")

        except Exception as e:
            await ctx.send(f"error {e}")


def setup(bot):
    bot.add_cog(bg_Commands(bot))

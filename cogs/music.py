import discord
import traceback
import psutil
import os
import aiohttp
import re
import lavalink
import math

from discord.ext import commands
from discord.ext.commands import errors
from utils import default
from utils import lists, permissions, http, default
from discord import Webhook, AsyncWebhookAdapter
from os import replace
from aiohttp.helpers import current_task

async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        await ctx.send_help(str(ctx.invoked_subcommand))
    else:
        await ctx.send_help(str(ctx.command))


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())
        self.bot.music = lavalink.Client(whatever)
        self.bot.music.add_node('localhost', whatever, 'fuckyou', 'na', 'music-node')
        self.bot.add_listener(self.bot.music.voice_update_handler, 'on_socket_response')
        self.bot.music.add_event_hook(self.track_hook)

    @commands.guild_only()
    @commands.command(name='join')
    async def join(self, ctx):
        print('join command worked')
        member = discord.utils.find(lambda m: m.id == ctx.author.id, ctx.guild.members)
        if member is not None and member.voice is not None:
          vc = member.voice.channel
          player = self.bot.music.player_manager.create(ctx.guild.id, endpoint=str(ctx.guild.region))
          if not player.is_connected:
            player.store('channel', ctx.channel.id)
            await self.connect_to(ctx.guild.id, str(vc.id))

    @commands.guild_only()
    @commands.command(name='play', aliases=["p"])
    async def play(self, ctx, *, query):
        user = ctx.message.author
        vc = user.voice.channel

        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if voice == None:
            temp1 = self.bot.commands
            temp = self.bot.get_command(name='join')
            await temp.callback(self, ctx)
        else:
            await ctx.send("I'm already connected!")
        try:
            player = self.bot.music.player_manager.get(ctx.guild.id)
            query = f'ytsearch:{query}'
            results = await player.node.get_tracks(query)
            tracks = results['tracks'][0:1]
            query_result = ''
            for track in tracks:
              query_result = query_result + f'{track["info"]["title"]} - {track["info"]["uri"]}\n'
            embed = discord.Embed(color=0x1f7eb8)
            embed.description = query_result
    
            await ctx.channel.send(embed=embed)

            track = tracks[int(0)]
    
            player.add(requester=ctx.author.id, track=track)
            if not player.is_playing:
              await player.play()
    
        except Exception as error:
            await ctx.send(f"{error}")

    @commands.guild_only()
    @commands.command(name='queue', aliases=["q"])
    async def queue(self, ctx, page: int = 1):
        player = self.bot.music.player_manager.get(ctx.guild.id)

        items_per_page = 10
        pages = math.ceil(len(player.queue) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue_list = ''
        for index, track in enumerate(player.queue[start:end], start=start):
            queue_list += f'`{index + 1}.` [**{track.title}**]({track.uri})\n'

        embed = discord.Embed(color=0x1f7eb8=
        embed.description = f'**{len(player.queue)} tracks**\n\n{queue_list}')
        embed.set_footer(text=f'Viewing page {page}/{pages}')
        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command(name='skip', aliases=["s"])
    async def skip(self, ctx):
        player = self.bot.music.player_manager.get(ctx.guild.id)

        embed = discord.Embed(color=0x1f7eb8)
        embed.description = "skipped!"
        await player.skip()
        await ctx.channel.send(embed=embed)
      
    async def track_hook(self, event):
      if isinstance(event, lavalink.events.QueueEndEvent):
        guild_id = int(event.player.guild_id)
        await self.connect_to(guild_id, None)
      
    async def connect_to(self, guild_id: int, channel_id: str):
      ws = self.bot._connection._get_websocket(guild_id)
      await ws.voice_state(str(guild_id), channel_id)

def setup(bot):
    bot.add_cog(Music(bot))

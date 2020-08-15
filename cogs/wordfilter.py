import discord
import traceback
import psutil
import os
import aiohttp
import random
import re

from discord.ext import commands
from discord.ext.commands import errors
from utils import default
from utils import lists, permissions, http, default
from discord import Webhook, AsyncWebhookAdapter


async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        await ctx.send_help(str(ctx.invoked_subcommand))
    else:
        await ctx.send_help(str(ctx.command))



#Yandere dev code below


class Wordfilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message):
        userinp = message.content
        message.content = message.content.lower().replace('', '')
        user = message.author
        channelid = message.channel.name

        if "discord.gg" in message.content:
            if discord.utils.get(user.roles, name="Heimdallar") != None:
                    return
            else:
                await message.delete()
                quotee = re.compile(r'(?!\bbased\b|\bsexpilled\b|\bis\b|\bare\b|\bhow\b|\byou\b|\bhello\b|\band\b|\bad\b|\byou\b|\blain\b|\bmy\b|\bdick\b|\bpenis\b|\bpussy\b|\bfag\b|\bam\b|\bnigger\b|\bi|\bI\b|\bu\b)\b[^\s]+\b')
                subit = "https://cdn.discordapp.com/attachments/673308690157404211/743601553356751002/unknown.png"
                result = re.sub(quotee, subit, message.content)
                print(message.content)
                print(result)

                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url('webhook url here', adapter=AsyncWebhookAdapter(session))
                    username = message.author.display_name
                    pfp = message.author.avatar_url_as(size=1024)
                    await webhook.send(f'{result}', username=str(username), avatar_url=str(pfp))

        if channelid != "degeneral":
            return

        async def niggerfuck():
            if message.author.bot:
                return
            clean = message.content.replace(f"{word1}", f"{word2}")
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url('webhook url here', adapter=AsyncWebhookAdapter(session))
                username = message.author.display_name
                pfp = message.author.avatar_url_as(size=1024)
                await message.delete()
                await webhook.send(f'{clean}', username=str(username), avatar_url=str(pfp))


        if discord.utils.get(message.author.roles, name="Muted") != None:
            await message.delete();
            return
        if discord.utils.get(message.author.roles, name="Hardmute") != None:
            await message.delete();
            return

        if "@everyone" in message.content or "@here" in message.content or "72339619" in message.content or "waa" in message.content or "705050082818523195.png" in message.content or "72340365141409" in message.content:
            if discord.utils.get(user.roles, name="Heimdallar") != None:
                    return
            else:
                await message.delete();

        elif "cancer" in message.content:
            if message.author.bot:
                return
            await message.add_reaction('<:cringe:661301648580280359>')
        elif "shit bot" in message.content:
            answer = random.choice(lists.anger)
            if message.author.bot:
                return
            await message.channel.send(f'{answer}')
        elif "kill myself" in message.content:
            answer = random.choice(lists.suicide)
            if message.author.bot:
                return
            await message.channel.send(f'{answer}')
        elif "fix your bot" in message.content:
            answer = random.choice(lists.anger)
            if message.author.bot:
                return
            await message.channel.send(f'{answer}')
        elif "good bot" in message.content:
            answer = random.choice(lists.hap)
            if message.author.bot:
                return
            await message.channel.send(f'{answer}')

        elif "excludedfag" in message.content or "https://" in message.content or "kenya" in message.content or "maya" in message.content or "sanya" in message.content or "tanya" in message.content or "chechnya" in message.content or "thnyan" in message.content or ":nyan:" in message.content or "nyaggot" in message.content:
            return
                
        elif "mhm" in message.content:
            word1 = "mhm"
            word2 = "romet is a x-dressing faggot kil myself"
            await niggerfuck()
        elif "faith" in message.content:
            word1 = "faith"
            word2 = "fatih"
            await niggerfuck()
        elif "excluded" in message.content:
            word1 = "excluded"
            word2 = "excludedfag"
            await niggerfuck()
        elif "indica" in message.content:
            word1 = "indica"
            word2 = "ethot"
            await niggerfuck()
        elif "pozu" in message.content:
            word1 = "pozu"
            word2 = "kike"
            await niggerfuck()
        elif "alex jones" in message.content:
            word1 = "alex jones"
            word2 = "fat james mason"
            await niggerfuck()
        elif "boomer" in message.content:
            word1 = "boomer"
            word2 = "hoomer"
            await niggerfuck()
        elif "vocaloid" in message.content:
            word1 = "vocaloid"
            word2 = "mongoloid"
            await niggerfuck()
        elif "ur weewee" in message.content:
            word1 = "ur weewee"
            word2 = "dogdildo"
            await niggerfuck()
        elif "tranny cock" in message.content:
            word1 = "tranny cock"
            word2 = "faggot"
            await niggerfuck()
        elif "shota" in message.content:
            word1 = "shota"
            word2 = "faggot"
            await niggerfuck()
        elif "sissy" in message.content:
            word1 = "sissy"
            word2 = "faggot"
            await niggerfuck()
        elif "brap" in message.content:
            word1 = "brap"
            word2 = "toot"
            await niggerfuck()
        elif "nya" in message.content:
            word1 = "nya"
            word2 = "catfucker"
            await niggerfuck()
        elif "femboy" in message.content:
            word1 = "femboy"
            word2 = "femsnot"
            await niggerfuck()
        elif "femboi" in message.content:
            word1 = "femboi"
            word2 = "femsnot"
            await niggerfuck()
        elif "boypussy" in message.content:
            word1 = "boypussy"
            word2 = "onajole"
            await niggerfuck()
        elif "boipussy" in message.content:
            word1 = "boipussy"
            word2 = "onajole"
            await niggerfuck()
        elif "boy pussy" in message.content:
            word1 = "boy pussy"
            word2 = "onajole"
            await niggerfuck()
        elif "boi pussy" in message.content:
            word1 = "boi pussy"
            word2 = "onajole"
            await niggerfuck()
        elif "black man" in message.content:
            answer = random.choice(lists.niggerresponse)
            word1 = "black man"
            word2 = str(answer)
            await niggerfuck()
        elif "black woman" in message.content:
            answer = random.choice(lists.niggerresponse)
            word1 = "black woman"
            word2 = str(answer)
            await niggerfuck()
        elif "black people" in message.content:
            answer = random.choice(lists.niggerresponse)
            word1 = "black people"
            word2 = str(answer)
            await niggerfuck()
        elif "black person" in message.content:
            answer = random.choice(lists.niggerresponse)
            word1 = "black person"
            word2 = str(answer)
            await niggerfuck()
        elif "african" in message.content:
            answer = random.choice(lists.niggerresponse)
            word1 = "african"
            word2 = str(answer)
            await niggerfuck()
        elif "blacks" in message.content:
            answer = random.choice(lists.niggerresponse)
            word1 = "blacks"
            word2 = str(answer) + "s"
            await niggerfuck()

def setup(bot):
    bot.add_cog(Wordfilter(bot))

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

class Condom(commands.Cog):
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
        if "tenor." in message.content:
            await message.delete();

        if "discord.com/channels" in message.content:
            return

        if "discord.gg" in message.content or "discord." in message.content or ".gg/" in message.content:
            await message.delete()
            quotee = re.compile(r'(?!\bbased\b|\bsexpilled\b|\bis\b|\bare\b|\bhow\b|\byou\b|\bhello\b|\band\b|\bad\b|\byou\b|\blain\b|\bmy\b|\bdick\b|\bpenis\b|\bpussy\b|\bfag\b|\bam\b|\bnigger\b|\bi|\bI\b|\bu\b)\b[^\s]+\b')
            subit = "https://cdn.discordapp.com/attachments/673308690157404211/743601553356751002/unknown.png"
            result = re.sub(quotee, subit, message.content)
            print(message.content)
            print(result)

            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url('https://discordapp.com/api/webhooks/661116894249484289/1YhybxOsoR2HnBPvCtUsORrkRulgc8ENmVojDMYcLX5Ukg1yI4eaitfTmm2w5JNvHUtK', adapter=AsyncWebhookAdapter(session))
                username = message.author.display_name
                pfp = message.author.avatar_url_as(size=1024)
                await webhook.send(f'{result}', username=str(username), avatar_url=str(pfp))

        if discord.utils.get(message.author.roles, name="Muted") != None:
            await message.delete();
            return
        if discord.utils.get(message.author.roles, name="Hardmute") != None:
            await message.delete();
            return

        if channelid != "degeneral":
            return

        async def niggerfuckk():
            if message.author.bot:
                return
            clean = message.content.replace(f"{word1}", f"{word2}")
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url('https://discordapp.com/api/webhooks/661116894249484289/1YhybxOsoR2HnBPvCtUsORrkRulgc8ENmVojDMYcLX5Ukg1yI4eaitfTmm2w5JNvHUtK', adapter=AsyncWebhookAdapter(session))
                username = message.author.display_name
                pfp = message.author.avatar_url_as(size=1024)
                await message.delete()
                await webhook.send(f'{clean}', username=str(username), avatar_url=str(pfp))

        async def niggerfuck():
            if message.author.bot:
                return
            a = message.content
            b = {'mhm': 'romet is a x-dressing faggot kil myself', 'faith': 'fatih',
            'excluded': 'excludedfag', 'indica': 'ethot', 'pozu': 'kike', 'tealeaf': '3 FREE STONKS', 'alex jones': 'fat james mason',
            'boomer': 'hoomer', 'jesus christ': 'dead kike on a spike', 'jesus': 'jewsus', 'vocaloid': 'mongoloid', 'tranny cock': 'faggot',
            'shota': 'faggot', 'sissy': 'faggot', 'brap': 'toot', 'nya': 'catfucker', 'femboy': 'femsnot', 'femboi': 'femsnot', 'boypussy': 'onajole',
            'boipussy': 'onajole', 'boy pussy': 'onajole', 'boi pussy': 'onajole', 'systemspace': 'systemgay', 'deal': 'chungus', 'chink': 'glorious chinese',
            'thanks giving': 'indigenous peoples day', 'thanksgiving': 'indigenous peoples day', 'columbus day': 'indigenous peoples day'}
            for x,y in b.items():
                a = a.replace(x, y)
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url('https://discordapp.com/api/webhooks/661116894249484289/1YhybxOsoR2HnBPvCtUsORrkRulgc8ENmVojDMYcLX5Ukg1yI4eaitfTmm2w5JNvHUtK', adapter=AsyncWebhookAdapter(session))
                username = message.author.display_name
                pfp = message.author.avatar_url_as(size=1024)
                await message.delete()
                await webhook.send(f'{a}', username=str(username), avatar_url=str(pfp))


        if "@everyone" in message.content or "@here" in message.content or "72339619" in message.content or "waa" in message.content or "705050082818523195.png" in message.content or "72340365141409" in message.content:
            if discord.utils.get(user.roles, name="Heimdallar") != None:
                    return
            else:
                await message.delete();

        elif "cancer" in message.content:
            if message.author.bot:
                return
            await message.add_reaction('<:cringe:661301648580280359>')


        elif "bot" in message.content or "laika" in message.content:
            if "both" in message.content:
                return
            pf = ProfanityFilter()
            if "kill" in message.content or "hate" in message.content:
                answer = random.choice(lists.anger)
                if message.author.bot:
                    return
                await message.channel.send(f'{answer}')
            if pf.is_profane(f"{message.content}") == True:
                answer = random.choice(lists.anger)
                if message.author.bot:
                    return
                await message.channel.send(f'{answer}')
            elif pf.is_clean(f"{message.content}") == True:
                return
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

        if "chinese" in message.content:
            pf = ProfanityFilter()
            if pf.is_profane(f"{message.content}") == True:
                word1 = "chinese"
                word2 = "GLORIOUS CHINESE"
                await niggerfuckk()

        elif "china" in message.content:
            pf = ProfanityFilter()
            if pf.is_profane(f"{message.content}") == True:
                word1 = "china"
                word2 = "CHINA IS GLORIOUS RIDE DA TIGA I LOVE CHINA"
                await niggerfuckk()

        elif "black woman" in message.content:
            answer = random.choice(lists.niggerresponse)
            word1 = "black woman"
            word2 = str(answer)
            await niggerfuckk()
        elif "black people" in message.content:
            answer = random.choice(lists.niggerresponse)
            word1 = "black people"
            word2 = str(answer)
            await niggerfuckk()
        elif "black person" in message.content:
            answer = random.choice(lists.niggerresponse)
            word1 = "black person"
            word2 = str(answer)
            await niggerfuckk()
        elif "african" in message.content:
            answer = random.choice(lists.niggerresponse)
            word1 = "african"
            word2 = str(answer)
            await niggerfuckk()
        elif "blacks" in message.content:
            if "blacksmith" in message.content:
                return
            answer = random.choice(lists.niggerresponse)
            word1 = "blacks"
            word2 = str(answer) + "s"
            await niggerfuckk()

        elif "kenya" in message.content or "maya" in message.content or "sanya" in message.content or "tanya" in message.content or "chechnya" in message.content or "thnyan" in message.content or ":nyan:" in message.content or "nyaggot" in message.content or "https://" in message.content or "indication" in message.content or "excludedfag" in message.content or "blacksmith" in message.content:
            return

        wordlist = ("mhm", "faith", "excluded", "indica", "pozu", "tealeaf", "alex jones", "boomer", "jesus", "vocaloud", "tranny cock", "shota", "sissy", "brap", "nya", "femboy", "femboi", "boypussy", "boy pussy", "boipussy", "boi pussy", "systemspace", "deal", "chink", "thanks giving", "thanksgiving", "columbus day")
        for i in wordlist:
            if i in message.content:
                await niggerfuck()

def setup(bot):
    bot.add_cog(Condom(bot))

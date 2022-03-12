import discord
import traceback
import psutil
import os
import aiohttp
import random
import re
import json
from json.decoder import JSONDecodeError

from discord.ext import commands
from discord.ext.commands import errors
from utils import default
from utils import lists, permissions, http, default
from discord import Webhook, AsyncWebhookAdapter

from profanityfilter import ProfanityFilter

from io import StringIO, BytesIO


async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        await ctx.send_help(str(ctx.invoked_subcommand))
    else:
        await ctx.send_help(str(ctx.command))

with open("jewlist.json", "r") as file:
    data = json.load(file)

class Condom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message):
        if "lain" in message.author.display_name:
            await message.author.edit(nick="faggot")
        if "🐊" in message.author.display_name:
            await message.author.edit(nick="Gatorfree zone")
        if message.author.bot or message.content.startswith("."):
                return
        message.content = message.content.lower().replace('', '')
        user = message.author
        username = message.author.display_name
        pfp = message.author.avatar_url_as(size=1024)
        channelid = message.channel.name
        webhookurl = 'https://discord.com/api/webhooks/whatever'

        if "discordapp.com/attachments" in message.content:
            return

        #if "tenor." in message.content:
        #    await message.delete();

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
                webhook = Webhook.from_url(webhookurl, adapter=AsyncWebhookAdapter(session))
                await webhook.send(f'{result}', username=str(username), avatar_url=str(pfp))

        if discord.utils.get(message.author.roles, name="Muted") != None:
            if message.author.id == 759621355708350484:
                return
            else:
                return await message.delete();
        if discord.utils.get(message.author.roles, name="Hardmute") != None:
            if message.author.id == 759621355708350484:
                return
            else:
                return await message.delete();

        if message.content == 'f':
            await message.channel.send(f"**{message.author.name}** has paid their respect {random.choice(['❤', '💛', '💚', '💙', '💜'])}")

        elif message.content.startswith('f '):
            reason = message.content.partition("f ")[2]
            await message.channel.send(f"**{message.author.name}** has paid their respect for **{reason}** {random.choice(['❤', '💛', '💚', '💙', '💜'])}")

        elif message.content.startswith('say'):
            if message.content.endswith('name'):
                embed = discord.Embed(color=0xe1a6e1)
                embed.set_image(url="https://cdn.discordapp.com/attachments/660982562331820032/834182511781347328/unknown-61.png")
                await message.channel.send(embed=embed)

        #--------------------------------------------------------------------
        if channelid != "degeneral":
            return
        if message.author.bot:
            return
        if ":trump" in message.content or "kenya" in message.content or "maya" in message.content or "sanya" in message.content or "tanya" in message.content or "chechnya" in message.content or "thnyan" in message.content or ":nyan:" in message.content or "nyaggot" in message.content or "https://" in message.content or "indication" in message.content or "excludedfag" in message.content or "blacksmith" in message.content:
            return
        a = message.content
        b = lists.censorship
        if "chinese" in a:
            pf = ProfanityFilter()
            if pf.is_profane(f"{a}") == True:
                word1 = "chinese"
                word2 = "GLORIOUS CHINESE"
                a = a.replace(f"{word1}", f"{word2}")
        if "china" in a:
            pf = ProfanityFilter()
            if pf.is_profane(f"{a}") == True:
                word1 = "china"
                word2 = "CHINA IS GLORIOUS RIDE DA TIGA I LOVE CHINA"
                a = a.replace(f"{word1}", f"{word2}")
        if "black woman" in a:
            answer = random.choice(lists.niggerresponse)
            word1 = "black woman"
            word2 = str(answer)
            a = a.replace(f"{word1}", f"{word2}")
        if "black people" in a:
            answer = random.choice(lists.niggerresponse)
            word1 = "black people"
            word2 = str(answer)
            a = a.replace(f"{word1}", f"{word2}")
        if "black person" in a:
            answer = random.choice(lists.niggerresponse)
            word1 = "black person"
            word2 = str(answer)
            a = a.replace(f"{word1}", f"{word2}")
        if "african" in a:
            answer = random.choice(lists.niggerresponse)
            word1 = "african"
            word2 = str(answer)
            a = a.replace(f"{word1}", f"{word2}")
        if "blacks" in a:
            if "blacksmith" in a:
                return
            answer = random.choice(lists.niggerresponse)
            word1 = "blacks"
            word2 = str(answer) + "s"
            a = a.replace(f"{word1}", f"{word2}")
        for x,y in b.items():
            a = a.replace(x, y)
        if message.content == a: return
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(webhookurl, adapter=AsyncWebhookAdapter(session))
            await message.delete()
            await webhook.send(f'{a}', username=str(username), avatar_url=str(pfp))

        try:
            if "https:" in message.content or "brother" in message.content:
                return
            else:
                for wordw in data:
                    #print(wordw)
                    if wordw.lower() in message.content.lower():
                        print(wordw.lower())
                        async with aiohttp.ClientSession() as session:
                            fuckkw = message.content.lower()
                            fuwfuwfu = fuckkw.replace(f"{wordw.lower()}", f"((({wordw.lower()})))")
                            webhook = Webhook.from_url(webhookurl, adapter=AsyncWebhookAdapter(session))
                            await message.delete()
                            await webhook.send(f'{fuwfuwfu}', username=str(username), avatar_url=str(pfp))

        except Exception as e:
            print(f"{e}") 

        if "@everyone" in message.content or "@here" in message.content:
            if discord.utils.get(user.roles, name="Heimdallar") != None:
                return
            elif message.author.id == 857346075585151006:
                return
            else:
                await message.delete();

        elif "pornhub.com/" in message.content:
            await message.channel.send(f'Meet someone in real lyfe, virgin xd')


        if "bot" in message.content or "laika" in message.content:
            if "both" in message.content:
                return
            pf = ProfanityFilter()
            if "kill" in message.content or "hate" in message.content:
                answer = random.choice(lists.anger)
                await message.channel.send(f'{answer}')
            if pf.is_profane(f"{message.content}") == True:
                answer = random.choice(lists.anger)
                await message.channel.send(f'{answer}')
            elif pf.is_clean(f"{message.content}") == True:
                return
        if "kill myself" in message.content:
            answer = random.choice(lists.suicide)
            await message.channel.send(f'{answer}')
        if "fix your bot" in message.content:
            answer = random.choice(lists.anger)
            await message.channel.send(f'{answer}')


def setup(bot):
    bot.add_cog(Condom(bot))

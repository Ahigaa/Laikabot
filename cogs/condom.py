import discord
import traceback
import psutil
import os
import aiohttp
import random
import re
import sqlite3

from discord.ext import commands
from discord.ext.commands import errors
from utils import default
from utils import lists, permissions, http, default
from discord import Webhook, AsyncWebhookAdapter

from profanityfilter import ProfanityFilter

from nudenet import NudeDetector, NudeClassifier

from io import StringIO, BytesIO

from PIL import Image


async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        await ctx.send_help(str(ctx.invoked_subcommand))
    else:
        await ctx.send_help(str(ctx.command))


class Condom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message):
        if message.author.bot:
                return
        author_id = str(message.author.id)
        guild_id = str(message.guild.id)
        #print("message")
        userinp = message.content
        message.content = message.content.lower().replace('', '')
        user = message.author
        channelid = message.channel.name
        if "discordapp.com/attachments" in message.content:
            return

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
                webhook = Webhook.from_url('https://discordapp.com/api/webhooks/...', adapter=AsyncWebhookAdapter(session))
                username = message.author.display_name
                pfp = message.author.avatar_url_as(size=1024)
                await webhook.send(f'{result}', username=str(username), avatar_url=str(pfp))

        if discord.utils.get(message.author.roles, name="Muted") != None:
            await message.delete();
            return
        if discord.utils.get(message.author.roles, name="Hardmute") != None:
            await message.delete();
            return

        if message.content == 'f':
            await message.channel.send(f"**{message.author.name}** has paid their respect {random.choice(['❤', '💛', '💚', '💙', '💜'])}")

        elif message.content.startswith('f '):
            await message.channel.send(f"**{message.author.name}** has paid their respect {f"for **{message.content.partition("f ")[2]}** "}{random.choice(['❤', '💛', '💚', '💙', '💜'])}")

        if channelid != "degeneral":
            return

        image_types = ['jpg','png','jpeg', 'gif']
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(image) for image in image_types):
                #classifier = NudeClassifier()
                detector = NudeDetector()
                await attachment.save("/home/ahigaaa/Laikabotfuck/cogs/temp/img.jpg")
                a = str(detector.detect('/home/ahigaaa/Laikabotfuck/cogs/temp/img.jpg'))
                channel = self.bot.get_channel(660985458049941524)
                await channel.send(f'image saved')
                await channel.send(f'{a}')
                if 'EXPOSED_GENITALIA_F' in a or 'EXPOSED_GENITALIA_M' in a or 'EXPOSED_BREAST_F' in a:
                    DB_NAME = "database"
                    db_path = os.path.abspath("/home/ahigaaa/Laikabotfuck/db/" + DB_NAME + ".db")
                    self.db = sqlite3.connect(db_path)
                    self.db_cursor = self.db.cursor()
                    print(f"Connected")
                    print("true")

                    isImage=True
                    if isImage:
                        detector.censor(
                            '/home/ahigaaa/Laikabotfuck/cogs/temp/img.jpg', 
                            out_path='/home/ahigaaa/Laikabotfuck/cogs/temp/img_censored.jpg', 
                            visualize=False
                        )

                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url('https://discordapp.com/api/webhooks/661116894249484289/1YhybxOsoR2HnBPvCtUsORrkRulgc8ENmVojDMYcLX5Ukg1yI4eaitfTmm2w5JNvHUtK', adapter=AsyncWebhookAdapter(session))
                            username = message.author.display_name
                            pfp = message.author.avatar_url_as(size=1024)
                            file = discord.File("/home/ahigaaa/Laikabotfuck/cogs/temp/img_censored.jpg", filename="image.jpg")
                            await webhook.send(file=file, username=str(username), avatar_url=str(pfp))
                            await message.delete()
                            self.db_cursor.execute(f"SELECT * FROM fucku WHERE UserID='{author_id}' AND GuildID='{guild_id}'")
                            user = self.db_cursor.fetchone()
                            if user:
                                print("User found")
                                sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
                                val = (int(user[4] + 2), int(message.author.id), int(message.guild.id))
                                self.db_cursor.execute(sql, val)
                                self.db.commit()
                            try:
                                self.db_cursor.close()
                                self.db.close()
                            except Exception as e:
                                return


        async def niggerfuck():
            if message.author.bot:
                return
            DB_NAME = "database"
            db_path = os.path.abspath("/home/ahigaaa/Laikabotfuck/db/" + DB_NAME + ".db")
            self.db = sqlite3.connect(db_path)
            self.db_cursor = self.db.cursor()
            print(f"Connected")

            a = message.content
            b = lists.censorship
            
            for x,y in b.items():
                a = a.replace(x, y)

            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url('https://discordapp.com/api/webhooks/...', adapter=AsyncWebhookAdapter(session))
                username = message.author.display_name
                pfp = message.author.avatar_url_as(size=1024)
                await message.delete()
                await webhook.send(f'{a}', username=str(username), avatar_url=str(pfp))

                self.db_cursor.execute(f"SELECT * FROM fucku WHERE UserID='{author_id}' AND GuildID='{guild_id}'")
                user = self.db_cursor.fetchone()
                if user:
                    print("User found")
                    sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
                    val = (int(user[4] - 3), int(message.author.id), int(message.guild.id))
                    self.db_cursor.execute(sql, val)
                    self.db.commit()
                try:
                    self.db_cursor.close()
                    self.db.close()
                except Exception as e:
                    return

        if "@everyone" in message.content or "@here" in message.content:
            if discord.utils.get(user.roles, name="Heimdallar") != None:
                    return
            else:
                await message.delete();

        elif "cancer" in message.content:
            if message.author.bot:
                return
            await message.add_reaction('<:cringe:661301648580280359>')

        elif "pornhub.com/" in message.content:
            await message.channel.send(f'Meet someone in real lyfe, virgin xd')

        elif ":trump" in message.content or "kenya" in message.content or "maya" in message.content or "sanya" in message.content or "tanya" in message.content or "chechnya" in message.content or "thnyan" in message.content or ":nyan:" in message.content or "nyaggot" in message.content or "https://" in message.content or "indication" in message.content or "excludedfag" in message.content or "blacksmith" in message.content:
            return

        wordlist = ("twink", "serb", "trump", "mhm", "faith", "excluded", "indica", "pozu", "tealeaf", "alex jones", "boomer", "jesus", "vocaloud", "tranny cock", "shota", "sissy", "brap", "nya", "femboy", "femboi", "boypussy", "boy pussy", "boipussy", "boi pussy", "systemspace", "deal", "chink", "thanks giving", "thanksgiving", "columbus day")
        for i in wordlist:
            if i in message.content:
                await niggerfuck()

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

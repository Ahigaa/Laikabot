import random
import discord
import json
import secrets
import asyncio
import time
import urllib.request
import re
import requests
import datetime
import aiohttp

from io import BytesIO
from discord.ext import commands
from asyncio import sleep
from utils import lists, permissions, http, default, querymaker
from bs4 import BeautifulSoup
from urllib.request import urlopen

from discord.ext.commands import check, CheckFailure
from discord import Webhook, AsyncWebhookAdapter

message_list = {}

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

m_numbers = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:"]

class Fun_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.session = aiohttp.ClientSession()

    def __embed_json(self, data, key="message"):
        em = discord.Embed(color=0xDEADBF)
        em.set_image(url=data[key])
        return em

    async def __get_image(self, ctx, user=None):
        if user:
            if user.is_avatar_animated():
                return str(user.avatar_url_as(format="gif"))
            else:
                return str(user.avatar_url_as(format="png"))

        await ctx.trigger_typing()

        message = ctx.message

        if len(message.attachments) > 0:
            return message.attachments[0].url

        def check(m):
            return m.channel == message.channel and m.author == message.author

        try:
            await ctx.send("Send me an image!")
            x = await self.bot.wait_for('message', check=check, timeout=15)
        except:
            return await ctx.send("Timed out...")

        if not len(x.attachments) >= 1:
            return await ctx.send("No images found.")

        return x.attachments[0].url

    async def __fuck_command(self, ctx, quote=None):
        await ctx.trigger_typing()
        if quote:
            messagewdwdad = await ctx.send("Working... *VROOOM*")
            await asyncio.sleep(1)
            await messagewdwdad.delete()
            try:
                randmm = ["111","222","333","444","555", "666", "7", "8", "9"]
                async def niggerfuck():
                    listf = list(quote)
                    random.shuffle(listf)
                    joinf = ''.join(listf)
                    await ctx.send(f"{ctx.author}: {joinf}")

                async def kikee():
                    await ctx.send(f"{ctx.author}: {random.choice(lists.fuck)}")

                async def eifefdf():
                    nigger = random.choice(lists.prompt) + random.choice(lists.responsen)
                    print(f"{ctx.author}: {nigger}")
                    await ctx.send(f"{ctx.author}: {nigger}")

                async def lainSpeak():
                    word = "Lain"
                    measure1 = time.time()
                    measure2 = time.time()
                    count = 1
                    await ctx.send(f"{ctx.author}: ")
                    while count < 2:
                        joinffed = ''.join(word)
                        await ctx.send(f"{joinffed}")
                        word = random.choice(lists.fuckcorpus)
                        if measure2 - measure1 >= 2:
                            measure1 = measure2
                            measure2 = time.time()
                            count += 1
                        else:
                            measure2 = time.time()
                async def fuckcufhf():
                    async with ctx.channel.typing():
                        try:
                            tranny = google_translator()  
                            tr1 = tranny.translate(quote, lang_tgt='en')
                            tr2 = tranny.translate(tr1, lang_src='en', lang_tgt='sp')
                            tr3 = tranny.translate(tr2, lang_src='sp', lang_tgt='en')
                            await ctx.send(f"{ctx.author}: {tr3}")
                        except Exception as e:
                            await ctx.send(f"{ctx.author}: Uh oh we got ratelimited by googleniggerniggerniggerniggerniggerniggerniggernigger(((")


                answer = random.choice(randmm)
                if "1" in answer:
                    await kikee()
                elif "2" in answer:
                    await eifefdf()
                elif "3" in answer:
                    await niggerfuck()
                else:
                    await fuckcufhf()
            except:
                return

        message = ctx.message

        if len(message.attachments) > 0:
            messagewdwdad = await ctx.send("Working... *VROOOM*")
            await asyncio.sleep(1)
            await messagewdwdad.delete()
            return message.attachments[0].url

        def check(m):
            return m.channel == message.channel and m.author == message.author

        try:
            if not len(message.attachments) >= 1:
                if not quote:
                    ans = random.choice(lists.ping)
                    before = time.monotonic()
                    message = await ctx.send("Pong")
                    ping = (time.monotonic() - before) * 1000
                    await message.edit(content=f"Pinged {ans}   |   {int(ping)}ms")
        except:
            return

    
    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message_delete(self, message):
        role_names = [role.name for role in message.author.roles]
        if ".search" in message.content or ".suicide" in message.content:
            await message_list[message].delete()
            del message_list[message]

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(2, 5, commands.BucketType.user)
    async def anime(self, ctx, *, search: str):
        """Get Anime Stats"""
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as cs:
            async with cs.post("https://graphql.anilist.co", json={
                "query": querymaker.anilist_query,
                "variables": {
                    "search": search
                }
            }) as res:
                data = await res.json()
        if data.get("errors", []):
            return await ctx.send("Error getting data from anilist: {}".format(data["errors"][0]["message"]))
        media = data["data"]["Page"]["media"]
        if not media:
            return await ctx.send("Nothing found.")
        media = media[0]
        if media["isAdult"] is True and not ctx.channel.is_nsfw():
            return await ctx.send("NSFW Anime can't be displayed in non NSFW channels.")
        color = int(media["coverImage"]["color"].replace("#", ""), 16) if media["coverImage"]["color"] else 0xdeadbf
        em = discord.Embed(colour=color)
        em.title = "{} ({})".format(media["title"]["romaji"], media["title"]["english"])
        if media["description"]:
            desc = BeautifulSoup(media["description"], "lxml")
            if desc:
                em.description = desc.text
        em.url = "https://anilist.co/anime/{}".format(media["id"])
        em.set_thumbnail(url=media["coverImage"]["extraLarge"])
        em.add_field(name="Status", value=media["status"].title(), inline=True)
        em.add_field(name="Episodes", value=media["episodes"], inline=True)
        em.add_field(name="Score", value=str(media["averageScore"]), inline=True)
        em.add_field(name="Genres", value=", ".join(media["genres"]))
        dates = "{}/{}/{}".format(media["startDate"]["day"], media["startDate"]["month"], media["startDate"]["year"])
        if media["endDate"]["year"] is not None:
            dates += " - {}/{}/{}".format(media["endDate"]["day"], media["endDate"]["month"], media["endDate"]["year"])
        em.add_field(name="Date", value=dates)
        await ctx.send(embed=em)

    def whatanime_embedbuilder(self, doc: dict):
        em = discord.Embed(color=0xDEADBF)
        em.title = doc["title_romaji"]
        em.url = "https://myanimelist.net/anime/{}".format(doc["mal_id"])
        em.add_field(name="Episode", value=str(doc["episode"]))
        em.add_field(name="At", value=str(doc["at"]))
        em.add_field(name="Matching %", value=str(round(doc["similarity"] * 100, 2)))
        em.add_field(name="Native Title", value=doc["title_native"])
        return em

    def whatanime_prefbuilder(self, doc):
        preview = f"https://trace.moe/thumbnail.php?anilist_id={doc['anilist_id']}" \
                  f"&file={doc['filename']}" \
                  f"&t={doc['at']}" \
                  f"&token={doc['tokenthumb']}"
        return preview


    @commands.cooldown(1, 20, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def chan(self, ctx, *, quote: commands.clean_content):
        """ Formats in a chan style """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        await ctx.message.delete()
        await ctx.send(f"**Anonymous**  01/06/19(Sun)13:02:01 No.7340664 ► __>>7342278__ __>>7346156__ __>>7347231__\n\n      __>>7339455__\n      {quote}")

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['f'])
    async def fuck(self, ctx, *, quote: commands.clean_content = None):
        """ you """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        async with ctx.channel.typing():
            img = await self.__fuck_command(ctx, quote)
            if not isinstance(img, str):
                return img

            async with self.session.get("https://nekobot.xyz/api/imagegen?type=magik&image=%s" % img) as r:
                res = await r.json()

            await ctx.send(embed=self.__embed_json(res))
        
    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def lainspeak(self, ctx, *, question: commands.clean_content):
        """ Consult Lain """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        word = "Lain"
        measure2 = time.time()
        measure1 = time.time()
        count = 1
        await ctx.send(f"{ctx.author}: ")
        while count < 2:
            joinffed = ''.join(word)
            await ctx.send(f"{joinffed}")
            word = random.choice(lists.fuckcorpus)
            if measure2 - measure1 >= 2:
                measure1 = measure2
                measure2 = time.time()
                count += 1
            else:
                measure2 = time.time()


    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question: commands.clean_content):
        """ Consult 8ball to receive an answer """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        answer = random.choice(lists.ballresponse)
        await ctx.send(f"🎱 **Question:** {question}\n**Answer:** {answer}")

    async def randomimageapi(self, ctx, url, endpoint):
        try:
            r = await http.get(url, res_method="json", no_cache=True)
        except json.JSONDecodeError:
            return await ctx.send("Couldn't find anything from the API")

        await ctx.send(r[endpoint])

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['kurultaj', 'meet', 'meetup'])
    async def date(self, ctx):
        """ Time until Kurultaj """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        date = datetime.datetime(2021, 5, 5)
        now = datetime.datetime.now()
        cock = date - now
        await ctx.send(f"Time until **INITIATE KURULTAJ**\n{cock}")


    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['toot'])
    async def doot(self, ctx):
        """ Lain doots """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        answer = random.choice(lists.doots)
        await ctx.send(f"{answer}")

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def lolice(self, ctx, user: discord.Member = None):
        """ Lolice  """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        async with ctx.channel.typing():            
            try:
                async with self.session.get("https://nekobot.xyz/api/imagegen?type=lolice&url=%s" % user.avatar_url_as(format="png")) as r:
                    res = await r.json()
                em = discord.Embed(color=0xDEADBF)
                await ctx.send(embed=em.set_image(url=res["message"]))
            except Exception as e:
                await ctx.send("Something went wrong")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pornhub(self, ctx, *, comment: str):
        """PronHub Comment Image"""
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        async with ctx.channel.typing():
            async with self.session.get(f"https://nekobot.xyz/api/imagegen?type=phcomment"
                              f"&image={ctx.author.avatar_url_as(format='png')}"
                              f"&text={comment}&username={ctx.author.name}") as r:
                res = await r.json()
            if not res["success"]:
                return await ctx.send("**Failed to successfully get image.**")
            await ctx.send(embed=self.__embed_json(res))

    @commands.command(aliases=['pillow'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bodypillow(self, ctx, user: discord.Member):
        """Bodypillow someone"""
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        async with ctx.channel.typing():
            img = await self.__get_image(ctx, user)
            if not isinstance(img, str):
                return img
            async with self.session.get("https://nekobot.xyz/api/imagegen?type=bodypillow&url=%s" % img) as r:
                res = await r.json()

            await ctx.send(embed=self.__embed_json(res))

    @commands.command()
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def minesweeper(self, ctx, size: int = 5):
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        size = max(min(size, 8), 2)
        bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
        is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
        has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
        message = "**Click to play**:\n"
        for y in range(size):
            for x in range(size):
                tile = "||{}||".format(chr(11036))
                if has_bomb(x, y):
                    tile = "||{}||".format(chr(128163))
                else:
                    count = 0
                    for xmod, ymod in m_offets:
                        if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                            count += 1
                    if count != 0:
                        tile = "||{}||".format(m_numbers[count - 1])
                message += tile
            message += "\n"
        await ctx.send(message)

    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def elonmusk(self, ctx):
        """ FUckING API PIECE OF SHit """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        await self.randomimageapi(ctx, 'https://nekos.life/api/v2/img/gecg', 'url')
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def roll(self, ctx, *, fuckw=None):
        """ Roll dubs """
        #user: discord.Member = None,
        #if not user:
        #    user = ctx.author
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        kike = int(''.join(str(random.randint(0,9)) for _ in range(9)))
        str2 = str(ctx.message)
        if fuckw == "roll":
            kike = str("625702444")
        #if user.id == 751479761015930961:
        #    kike = str("bury is going to serbia")
        await ctx.send(f"{fuckmenigga.mention}, **{kike}**")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['guard'])
    async def skyrim(self, ctx):
        """ Do you get to the ☁️ district very often? """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        skyanswer = random.choice(lists.skyrimresponse)
        await ctx.send(f"{skyanswer}")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['randomlain'])
    async def lain(self, ctx):
        """ Posts a random lain """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        randomla = random.choice(lists.randlain)
        await ctx.send(f"{randomla}")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['ahiga'])
    async def tsoi(self, ctx):
        """ Posts a random tsoi """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        randomts = random.choice(lists.randtsoi)
        await ctx.send(f"{randomts}")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['randomrat'])
    async def rat(self, ctx):
        """ Posts a random rat """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        randomra = random.choice(lists.randrat)
        await ctx.send(f"{randomra}")

    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['google'])
    async def search(self, ctx, *, search):
        """ Searches google """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        if ctx.author.id == 746184398852063393:
            return
        try:
            if "toddlercon" in search:
                search = "andy sixx log"
            if "america" in search:
                search = "fat american"
            fuckk = search.replace(" ", "_")
            website = f"https://images.search.yahoo.com/search/images?fr=yfp-t&p={str(fuckk)}"
            soup = BeautifulSoup(urllib.request.urlopen(website))
            listLink=[]
            for link in soup.findAll('img'):
                listLink.append(link)

            randImageIndex = random.randint(1,(len(listLink)-1))
            imgUrl=listLink[randImageIndex]

            fuckingnf = str(imgUrl)
            clean = re.findall(r'(https?://[^\s]+)', fuckingnf)

            clean1 = str(clean).replace("[", "")
            clean2 = str(clean1).replace("'", "")
            clean3 = str(clean2).replace("]", "")
            clean4 = str(clean3).replace('"', "")

            embed = discord.Embed(color=0xe1a6e1)
            embed.set_image(url=f"{clean4}")
            await ctx.send(embed=embed)

            if not permissions.can_upload(ctx):
                return await ctx.send("I cannot send images here ;>;")
        except Exception as e:
            await ctx.send("No results found!")

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def slags(self, ctx):
        """ Searches 4 hot slags """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        try:
            website = f"https://images.search.yahoo.com/search/images;_ylt=AwrEzOA48TVfTXUAn66JzbkF;_ylu=X3oDMTBsZ29xY3ZzBHNlYwNzZWFyY2gEc2xrA2J1dHRvbg--;_ylc=X1MDOTYwNjI4NTcEX3IDMgRhY3RuA2NsawRjc3JjcHZpZANjSUViY1RFd0xqSnZaeUU5WGFBYWRnUlVNVFU0TGdBQUFBRFg5dkhvBGZyA3lmcC10BGZyMgNzYS1ncARncHJpZANsOXBhbTd1SFN1Q0xPTHJ1TTZTQmpBBG5fc3VnZwMxMARvcmlnaW4DaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMEcXN0cmwDMTgEcXVlcnkDZml0JTIwZ2lybCUyMG1vZGVsBHRfc3RtcAMxNTk3MzYzNDk4?p=fit+girl+model&fr=yfp-t&fr2=sb-top-images.search&ei=UTF-8&n=60&x=wrt"
            soup = BeautifulSoup(urllib.request.urlopen(website))
            listLink=[]
            for link in soup.findAll('img'):
                listLink.append(link)

            randImageIndex = random.randint(1,(len(listLink)-1))
            imgUrl=listLink[randImageIndex]

            fuckingnf = str(imgUrl)
            clean = re.findall(r'(https?://[^\s]+)', fuckingnf)

            clean1 = str(clean).replace("[", "")
            clean2 = str(clean1).replace("'", "")
            clean3 = str(clean2).replace("]", "")
            clean4 = str(clean3).replace('"', "")

            embed = discord.Embed(color=0xe1a6e1)
            embed.set_image(url=f"{clean4}")
            await ctx.send(embed=embed)

            if not permissions.can_upload(ctx):
                return await ctx.send("I cannot send images here ;>;")
        except Exception as e:
            await ctx.send("No results found!")

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def suicide(self, ctx):
        """  Just stop """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        if ctx.author.id == 746184398852063393:
            return
        async def fuckiff():
            website = "https://xbooru.com/index.php?page=post&s=random"
            soup = BeautifulSoup(urllib.request.urlopen(website))
            listLink=[]
            for link in soup.findAll('img'):
                listLink.append(link)
        
            randImageIndex = random.randint(1,(len(listLink)-1))
            imgUrl=listLink[randImageIndex]
                                    
            fuckingnf = str(imgUrl)
            clean = re.findall(r'(https?://[^\s]+)', fuckingnf)
        
            clean1 = str(clean).replace("[", "")
            clean2 = str(clean1).replace("'", "")
            clean3 = str(clean2).replace("]", "")
            clean4 = str(clean3).replace('"', "")
        
            fuckingworkaround = f"||{clean4}||"
            if "||||" in fuckingworkaround:
                await fuckiff()
            else:
                fuckme = await ctx.send(f"{fuckingworkaround}")
                message_list[ctx.message]=fuckme
                await self.bot.process_commands(ctx.message)
        channelid = ctx.channel.name

        #if channelid != "⁄indica⁄":
        #    return

        await fuckiff()

        if not permissions.can_upload(ctx):
            return await ctx.send("I cannot send images here ;>;")

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def r34(self, ctx, *, search):
        """  Search r34 """
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        try:
            if "lain" in search:
                return await ctx.send("fukcu fuck u fuck u fuck u fuck u")
            fuckk = search.replace(" ", "_")
            website = f"https://xbooru.com/index.php?page=post&s=list&tags={str(fuckk)}+"
            soup = BeautifulSoup(urllib.request.urlopen(website))
            listLink=[]
            for link in soup.findAll('img'):
                listLink.append(link)

            randImageIndex = random.randint(1,(len(listLink)-1))
            imgUrl=listLink[randImageIndex]

            fuckingnf = str(imgUrl)
            clean = re.findall(r'(https?://[^\s]+)', fuckingnf)

            clean1 = str(clean).replace("[", "")
            clean2 = str(clean1).replace("'", "")
            clean3 = str(clean2).replace("]", "")
            clean4 = str(clean3).replace('"', "")

            embed = discord.Embed(color=0xe1a6e1)
            embed.set_image(url=f"{clean4}")
            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send("No results found!") 

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def frog(self, ctx):
        """  random frog """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        website = "https://images.search.yahoo.com/search/images?fr=yfp-t&p=frog&fr2=p%3As%2Cv%3Ai&.bcrumb=/5y.fZ..qqd&save=0"
        soup = BeautifulSoup(urllib.request.urlopen(website))
        listLink=[]
        for link in soup.findAll('img'):
            listLink.append(link)

        randImageIndex = random.randint(1,(len(listLink)-1))
        imgUrl=listLink[randImageIndex]
            
        fuckingnf = str(imgUrl)
        clean = re.findall(r'(https?://[^\s]+)', fuckingnf)

        clean1 = str(clean).replace("[", "")
        clean2 = str(clean1).replace("'", "")
        clean3 = str(clean2).replace("]", "")
        clean4 = str(clean3).replace('"', "")

        embed = discord.Embed(color=0xe1a6e1)
        embed.set_image(url=f"{clean4}")
        await ctx.send(embed=embed)

        if not permissions.can_upload(ctx):
            return await ctx.send("I cannot send images here ;>;")

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['goat'])
    async def satan(self, ctx):
        """ Posts a random satan """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        randomsata = random.choice(lists.randsatan)
        await ctx.send(f"{randomsata}")
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def cat(self, ctx):
        """ Posts a random cat """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        await self.randomimageapi(ctx, 'https://nekos.life/api/v2/img/meow', 'url')
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def dog(self, ctx):
        """ Posts a random dog """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        await self.randomimageapi(ctx, 'https://random.dog/woof.json', 'url')
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def birb(self, ctx):
        """ Posts a random birb """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        await self.randomimageapi(ctx, 'https://api.alexflipnote.dev/birb', 'file')
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def duck(self, ctx):
        """ Posts a random duck """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        await self.randomimageapi(ctx, 'https://random-d.uk/api/v1/random', 'url')

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=2.0, type=commands.BucketType.user)
    async def urban(self, ctx, *, search: str):
        """ Find the 'best' definition to your words """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        if search == "gay sex":
            await ctx.send(f"📚 Definitions for **{str(search)}**```fix\nad044```")
            return
        if search == "femboy":
            await ctx.send(f"📚 Definitions for **{str(search)}**```fix\nA tranny, you fucking faggot```")
            return
        if search == "femboys":
            await ctx.send(f"📚 Definitions for **{str(search)}**```fix\nA tranny, you fucking faggot```")
            return
        if search == "ad":
            await ctx.send(f"📚 Definitions for **{str(search)}**```fix\nIf you looked this up you're probably as gay as ad```")
            return
        if search == "ahiga":
            await ctx.send(f"📚 Definitions for **{str(search)}**```fix\n>Chief of apollo and initiate\n>Will scalp the heads of betas\n>civilized native american\n>dirbust systemspace\n>creates another cult because he can\n>Finno-Ugric Khan\n>has gf whom is based aswell\n>Will contribute by paying attention to the world and acting```")
            return
        if search == "hitler":
            await ctx.send(f"📚 Definitions for **{str(search)}**```fix\nThe prophet of Lain and our messiah```")
            return
        if search == "hoshi":
            await ctx.send(f"📚 Definitions for **{str(search)}**```fix\nHoshi also known as Ahiga and Chief Horsecock is the tribal leader of INITIATE. He is abs man.```")
            return
        if search == "surge":
            await ctx.send(f"📚 Definitions for **{str(search)}**```fix\nSurge, the man who reincarnated as a tomboy, was a great warrior during the indian wars, he is said to have had sexual intercourse with at least 1000 tomboys during the span of 2 years.```")
            return
        if search == "tomboy":
            await ctx.send(f"📚 Definitions for **{str(search)}**```fix\nTomboys are the ultimate straight man choice.a regular girl has tits and pussy but comes loaded with gay shit such as\nmakeup, desire for shopping clothes and useless shot and watching boring shitty tv shows.\n\nA gay dude is gay but he has a partner that shares his interests.\n\nA tomboy is the best of both worlds, a female body but with enough/fit/ness to keep up with you, good interests and \ngreat personality\n\nA trap is 200% gay. Not only are you fucking a dude, you are also putting up with the faggotry of a female```")
            return
        if search == "burychu":
            await ctx.send(f"📚 Definitions for **{str(search)}**```fix\nThe great Khan of the west, burychu\nHas dedicated his life to reclaim righteous steppe lands for his tribe\n\nWill piss on indofags\n\nEat my horse shit, farmboys.```")
            return
        if search == "大雨":
            await ctx.send(f"📚 Definitions for **{str(search)}**```fix\nGym teacher...```")
            return

        async with ctx.channel.typing():
            url = await http.get(f'https://api.urbandictionary.com/v0/define?term={search}', res_method="json")

            if url is None:
                return await ctx.send("I think the API broke...")

            if not len(url['list']):
                return await ctx.send("Couldn't find your search in the dictionary...")

            result = sorted(url['list'], reverse=True, key=lambda g: int(g["thumbs_up"]))[0]

            definition = result['definition']
            if len(definition) >= 1000:
                definition = definition[:1000]
                definition = definition.rsplit(' ', 1)[0]
                definition += '...'

            await ctx.send(f"📚 Definitions for **{result['word']}**```fix\n{definition}```")

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def fortune(self, ctx, *, quote: commands.clean_content = None):
        """ fortune | [image] """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        async with ctx.channel.typing():
            username = ctx.message.author.display_name
            pfp = ctx.message.author.avatar_url_as(size=1024)
            file = discord.File("cogs/temp/img.jpg", filename="image.jpg")
            uri = f'webhookurlhere'
            isImage=False
            fortune = f"{random.choice(lists.fortune)}"
            if ctx.message.attachments:
                isImage=True
                image_types = ['jpg','png','jpeg', 'gif']
                for attachment in ctx.message.attachments:
                    if any(attachment.filename.lower().endswith(image) for image in image_types):
                        await attachment.save("cogs/temp/img.jpg")
                        channel = self.bot.get_channel(channelidhere)
                        await channel.send(f'image saved')
            else:
                isImage=False
            if quote:
                await(await ctx.send("Working... *VROOOM*")).delete(delay=1)
                if isImage:
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(uri, adapter=AsyncWebhookAdapter(session))
                        await webhook.send(f'{quote}\n\n{fortune}', file=file, username=str(username), avatar_url=str(pfp))
                        await ctx.message.delete()
                else:
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(uri, adapter=AsyncWebhookAdapter(session))
                        await webhook.send(f'{quote}\n\n{fortune}', username=str(username), avatar_url=str(pfp))
                        await ctx.message.delete()
            else:
                if isImage:
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(uri, adapter=AsyncWebhookAdapter(session))
                        await webhook.send(f'\n\n{fortune}', file=file, username=str(username), avatar_url=str(pfp))
                        await ctx.message.delete()
                else:
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(uri, adapter=AsyncWebhookAdapter(session))
                        await webhook.send(f'\n\n{fortune}', username=str(username), avatar_url=str(pfp))
                        await ctx.message.delete()
            
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def rate(self, ctx, *, thing: commands.clean_content):
        """ Rates whatever """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        num = random.randint(0, 100)
        deci = random.randint(0, 9)

        if num == 100:
            deci = 0

        await ctx.send(f"I'd rate {thing} a **{num}.{deci} / 100**")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['howhot', 'hot'])
    async def hotcalc(self, ctx, *, user: discord.Member = None):
        """ Returns a random percent for how hot a discord user is """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        if user is None:
            user = ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        if user.id == 747885205037121626:
            hot = 101
        elif user.id == 209780641842200578:
            hot = 100
        elif user.id == 600984731156348929:
            hot = 210
        elif user.id == 599414310502006873:
            hot = -100

        emoji = "💔"
        if hot > 25:
            emoji = "❤"
        if hot > 50:
            emoji = "💖"
        if hot > 75:
            emoji = "💞"

        await ctx.send(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['penis'])
    async def peniscalc(self, ctx, *, user: discord.Member = None):
        """Detects user's penis length
        This is 100% accurate."""
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        if user is None:
            user = ctx.author
        random.seed(user.id)
        len = random.randint(0, 30)
        if user.id == 346093616734666764:
            len = 32
        elif user.id == 759621355708350484:
            len = 36
        elif user.id == 751479761015930961:
            len = 36
        elif user.id == 616958027752538127:
            len = 0
        p = "8" + "="* + len + "D"
        if user.id == 600984731156348929:
            p = "4:3"

        ppof = f"**{user.name}**'s dick is this long:\n{p}"
        msg = await ctx.send(ppof)

        def reaction_check(m):
            if (m.message_id == msg.id and m.user_id == user.id and str(m.emoji) == "✂️"):
                return True
            return False

        try:
            pp = "8" + "=     "* + len + "D"
            await msg.add_reaction("✂️")
            await self.bot.wait_for('raw_reaction_add', check=reaction_check)
            await msg.edit(content=f"**{user.name}**'s dick is this long:\n{pp}")
        except asyncio.TimeoutError:
            await msg.delete()
        except discord.Forbidden:
            await msg.edit(content=f"**{user.name}**'s dick is this long:\n{p}")

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['selfdestruct'])
    async def bomb(self, ctx):
        """ Fuck rate limit """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        timer = int(5)
        timer -= 1
        bomb = await ctx.send(':bomb:'+"-"*int(timer)+":fire:")
        time.sleep(1)
        while timer:
            timer -= 1
            await bomb.edit(content=':bomb:'+"-"*int(timer)+":fire:")
            time.sleep(1)
        await bomb.edit(content=':boom:')
        time.sleep(1)
        await bomb.delete()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['noticemesenpai', 'owo'])
    async def noticeme(self, ctx):
        """ Notice me senpai! owo """
        fuckmenigga = ctx.message.author
        
        if not permissions.can_upload(ctx):
            return await ctx.send("I cannot send images here ;>;")

        embed = discord.Embed(color=0xe1a6e1)
        embed.set_image(url="https://media.tenor.co/images/aeed0f97ccd1fb9a571fe48dda73408c/tenor.gif")
        await ctx.send(embed=embed)
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['gentoo'])
    async def installgentoo(self, ctx):
        """ Install gentoo faggot """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        if not permissions.can_upload(ctx):
            return await ctx.send("I cannot send images here ;>;")

        embed = discord.Embed(color=0xe1a6e1)
        embed.set_image(url="http://i0.kym-cdn.com/photos/images/newsfeed/000/558/394/3c9.png")
        embed.set_thumbnail(url="http://wiki.arx-libertatis.org/images/thumb/0/02/Gentoo_icon.png/24px-Gentoo_icon.png")
        await ctx.send(embed=embed)
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def notrat(self, ctx):
        """ That's not very rat.. """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        if not permissions.can_upload(ctx):
            return await ctx.send("I cannot send images here ;>;")

        embed = discord.Embed(color=0xe1a6e1)
        embed.set_image(url="https://cdn.discordapp.com/attachments/588370099933806602/618182390937944081/Rat.png")
        await ctx.send(embed=embed)
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['ad'])
    async def ad044(self, ctx, *, message=None):
        """ Femboys are gay"""
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        try:
            quotee = re.compile(r'(?!\bbased\b|\bsexpilled\b|\bis\b|\bare\b|\bhow\b|\byou\b|\bhello\b|\band\b|\bad\b|\byou\b|\blain\b|\bmy\b|\bdick\b|\bpenis\b|\bpussy\b|\bfag\b|\bam\b|\bnigger\b|\bi|\bI\b|\bu\b)\b[^\s]+\b')
            subit = "sex"
            result = re.sub(quotee, subit, message)

            if message is None:
                return
            else:
                await ctx.send(f"{result}")
        except Exception as e:
            await ctx.send("You need to enter a message too. Example:\n´.ad hello my name is ad´")

    @commands.command(pass_ctx=True)
    async def adsay(self, ctx, *, message: commands.clean_content = ""):
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        try:
            if message is None:
                return
            else:
                await ctx.message.delete()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url('https://discordapp.com/api/webhooks/661116894249484289/1YhybxOsoR2HnBPvCtUsORrkRulgc8ENmVojDMYcLX5Ukg1yI4eaitfTmm2w5JNvHUtK', adapter=AsyncWebhookAdapter(session))
                    username = 'ad044'
                    pfp = 'https://pbs.twimg.com/profile_images/1339877009288278017/iRjpYGIu_400x400.jpg'
                    await webhook.send(f'{message}', username=str(username), avatar_url=str(pfp))
        except Exception as e:
            return

    @commands.command(pass_ctx=True)
    async def anon(self, ctx, *, message: commands.clean_content = ""):
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        try:
            if message is None:
                return
            else:
                await ctx.message.delete()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url('https://discordapp.com/api/webhooks/661116894249484289/1YhybxOsoR2HnBPvCtUsORrkRulgc8ENmVojDMYcLX5Ukg1yI4eaitfTmm2w5JNvHUtK', adapter=AsyncWebhookAdapter(session))
                    username = 'xXx_ANONYMOUSHACKER_xXx'
                    pfp = 'https://cdn.discordapp.com/attachments/660982562331820032/800814876485877810/Leader_of_Anons.jpg'
                    await webhook.send(f'{message}', username=str(username), avatar_url=str(pfp))
        except Exception as e:
            return

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(pass_ctx=True)
    async def yokonsay(self, ctx, *, message: commands.clean_content = ""):
        try:
            if message is None:
                return
            else:
                await ctx.message.delete()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url('https://discordapp.com/api/webhooks/661116894249484289/1YhybxOsoR2HnBPvCtUsORrkRulgc8ENmVojDMYcLX5Ukg1yI4eaitfTmm2w5JNvHUtK', adapter=AsyncWebhookAdapter(session))
                    username = 'Yokon!'
                    pfp = 'https://cdn.discordapp.com/avatars/772169243751350273/f89bc65037fce04add1d9475d560c1d6.webp'
                    await webhook.send(f'{message}', username=str(username), avatar_url=str(pfp))
        except Exception as e:
            return
            
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['installnazbol'])
    async def installnazi(self, ctx):
        """ 📯 doot """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        if not permissions.can_upload(ctx):
            return await ctx.send("I cannot send images here ;>;")

        embed = discord.Embed(color=0xe1a6e1)
        embed.set_image(url="https://cdn.discordapp.com/attachments/595511047205421056/595514059273666560/241.png")
        await ctx.send(embed=embed)
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['lainprayer'])
    async def prayer(self, ctx):
        """ ❤ """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        if not permissions.can_upload(ctx):
            return await ctx.send("I cannot send images here ;>;")

        embed = discord.Embed(color=0xe1a6e1)
        embed.set_image(url="https://initiate.space/shrine/goddess.jpg")
        await ctx.send("Lain is god. Let's all love Lain Let's all love Lain Let's all love Lain Let's all love Lain Let's all love Lain Let's all love Lain Let's all love Lain Let's all love Lain Let's all love Lain")
        await ctx.send("***PRAY***")
        await ctx.send(embed=embed)
        await ctx.send("<3 I'm not a namefag")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['fatso'])
    async def fat(self, ctx):
        """ ur fat """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        if not permissions.can_upload(ctx):
            return await ctx.send("I cannot send images here ;>;")

        embed = discord.Embed(color=0xe1a6e1)
        embed.set_image(url="https://scontent.harristeeter.com/legacy/productimagesroot/DJ/3/1240133.jpg")
        await ctx.send(embed=embed)

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def slot(self, ctx):
        """ Roll the slot machine """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            return
        
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            await ctx.send(f"{slotmachine} All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
        else:
            await ctx.send(f"{slotmachine} No match, you lost 😢")


def setup(bot):
    bot.add_cog(Fun_Commands(bot))

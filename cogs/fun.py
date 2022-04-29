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
import sqlite3
import os

from io import StringIO, BytesIO
from discord.ext import commands
from asyncio import sleep
from datetime import datetime
from utils import lists, permissions, http, default, querymaker
from bs4 import BeautifulSoup
from urllib.request import urlopen

from discord.ext.commands import check, CheckFailure
from discord import Webhook, AsyncWebhookAdapter, utils, Embed

from PIL import Image, ImageDraw

from google_trans_new import google_translator  
from googlesearch import search as googlee

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
        messagewdwdad = await ctx.send("Working... *VROOOM*")
        await asyncio.sleep(1)
        await messagewdwdad.delete()
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
            await(await ctx.send("Working... *VROOOM*")).delete(delay=1)
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
                            tr3 = tranny.translate(tr2, lang_src='sp', lang_tgt='sw')
                            tr4 = tranny.translate(tr3, lang_src='sw', lang_tgt='no')
                            tr5 = tranny.translate(tr4, lang_src='no', lang_tgt='de')
                            tr6 = tranny.translate(tr5, lang_src='de', lang_tgt='so')
                            tr7 = tranny.translate(tr6, lang_src='so', lang_tgt='es')
                            tr8 = tranny.translate(tr7, lang_src='es', lang_tgt='sv')
                            tr9 = tranny.translate(tr8, lang_src='sv', lang_tgt='ru')
                            tr10 = tranny.translate(tr9, lang_src='ru', lang_tgt='tr')
                            tr11 = tranny.translate(tr10, lang_src='tr', lang_tgt='th')
                            tr12 = tranny.translate(tr11, lang_src='th', lang_tgt='bg')
                            tr13 = tranny.translate(tr12, lang_src='bg', lang_tgt='fi')
                            tr14 = tranny.translate(tr13, lang_src='fi', lang_tgt='he')
                            tr15 = tranny.translate(tr14, lang_src='he', lang_tgt='hu')
                            tr16 = tranny.translate(tr15, lang_src='hu', lang_tgt='cs')
                            tr17 = tranny.translate(tr16, lang_src='cs', lang_tgt='eo')
                            tr18 = tranny.translate(tr17, lang_src='eo', lang_tgt='ka')
                            tr20 = tranny.translate(tr18, lang_src='ka', lang_tgt='en')
                            await ctx.send(f"{ctx.author}: {tr20}")
                        except Exception as e:
                            await ctx.send(f"{ctx.author}: Uh oh we got ratelimited by googleniggerniggerniggerniggerniggerniggerniggernigger((({e}")


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

    async def randomimageapi(self, ctx, url, endpoint):
        try:
            r = await http.get(url, res_method="json", no_cache=True)
        except json.JSONDecodeError:
            return await ctx.send("Couldn't find anything from the API")

        await ctx.send(r[endpoint])

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message_delete(self, message):
        role_names = [role.name for role in message.author.roles]
        if ".search" in message.content or ".suicide" in message.content or "google" in message.content or "r34" in message.content:
            await message_list[message].delete()
            del message_list[message]

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def fortune(self, ctx, *, quote: commands.clean_content = None):
        """ fortune | [image] """
        async with ctx.channel.typing():
            username = ctx.message.author.display_name
            pfp = ctx.message.author.avatar_url_as(size=1024)
            file = discord.File("temp/img.jpg", filename="image.jpg")
            uri = f'whatever'
            isImage=False
            fortune = f"{random.choice(lists.fortune)}"
            if ctx.message.attachments:
                isImage=True
                image_types = ['jpg','png','jpeg', 'gif']
                for attachment in ctx.message.attachments:
                    if any(attachment.filename.lower().endswith(image) for image in image_types):
                        await attachment.save("temp/img.jpg")
                        channel = self.bot.get_channel(857815170213871618)
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

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def translate(self, ctx, *, text: str):
        """translate"""
        async with ctx.channel.typing():
            tranny = google_translator()  
            tr1 = tranny.translate(text, lang_tgt='en')
            await ctx.send(f"{tr1}")


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ahigger(self, ctx, user: discord.Member = None):
        """AHIGGER POST"""
        async with ctx.channel.typing():
            img = await self.__get_image(ctx, user)
            if not isinstance(img, str):
                return img

            url = str(img)
            bio = BytesIO(await http.get(url, res_method="read"))
            imgfil = Image.open(bio)

            bg = Image.open(urlopen('https://raw.githubusercontent.com/39hige1/initiatetheme/master/ahiggerpost.png')) 
            bgfile = bg.copy()
            imgfile = imgfil.copy()
            new_width = 810;
            new_height = 622;

            width, height = imgfile.size;
            asp_rat = width/height;
            new_rat = new_width/new_height;
    
            imgfile = imgfile.resize((new_width, new_height), Image.ANTIALIAS); 

            draw = ImageDraw.Draw(bgfile)
            bgfile.paste(imgfile, (100, 56))
            bgfile.save('profile/ahigger1.png') 
            with open('profile/ahigger1.png', 'rb') as fp:
                await ctx.send(file=discord.File(fp, "penis.png"))



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
        await ctx.message.delete()
        await ctx.send(f"**Anonymous**  01/06/19(Sun)13:02:01 No.7340664 ► __>>7342278__ __>>7346156__ __>>7347231__\n\n      __>>7339455__\n      {quote}")

    @commands.cooldown(1, 20, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def femto(self, ctx):
        """ femto """
        await ctx.send(f"🗡️Honour Truth, Make War, Have Fun")

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['f'])
    async def fuck(self, ctx, *, quote: commands.clean_content = None):
        """ you """
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
        
        answer = random.choice(lists.ballresponse)
        await ctx.send(f"🎱 **Question:** {question}\n**Answer:** {answer}")

    @commands.command()
    @commands.cooldown(2, 5, commands.BucketType.user)
    async def fact(self, ctx, *, text: str):
        if len(text) > 165:
            return await ctx.send("Text too long...")
        async with self.session.get("https://nekobot.xyz/api/imagegen?type=fact"
                          "&text=%s" % text) as r:
            res = await r.json()

        await ctx.trigger_typing()
        em = discord.Embed(color=0xDEADBF)
        await ctx.send(embed=em.set_image(url=res["message"]))


    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['toot'])
    async def doot(self, ctx):
        """ Lain doots """
        
        answer = random.choice(lists.doots)
        await ctx.send(f"{answer}")

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def lolice(self, ctx, user: discord.Member = None):
        """ Lolice  """
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
        async with ctx.channel.typing():
            async with self.session.get(f"https://nekobot.xyz/api/imagegen?type=phcomment"
                              f"&image={ctx.author.avatar_url_as(format='png')}"
                              f"&text={comment}&username={ctx.author.name}") as r:
                res = await r.json()
            if not res["success"]:
                return await ctx.send("**Failed to successfully get image.**")
            await ctx.send(embed=self.__embed_json(res))
            

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tweet(self, ctx, username: str, *, text: str):
        """Tweet as someone."""
        async with ctx.channel.typing():
            async with self.session.get("https://nekobot.xyz/api/imagegen?type=tweet"
                              "&username=%s"
                              "&text=%s" % (username, text,)) as r:
                res = await r.json()

            await ctx.send(embed=self.__embed_json(res))

    @commands.command(aliases=['pillow'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bodypillow(self, ctx, user: discord.Member):
        """Bodypillow someone"""
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

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['4042'])
    async def fourty(self, ctx):
        """ But q said it would happen! """
        
        fourtytwo = random.choice(lists.fourtytwo)
        await ctx.send(f"{fourtytwo}")

    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def elonmusk(self, ctx):
        """ FUckING API PIECE OF SHit """
        await self.randomimageapi(ctx, 'https://nekos.life/api/v2/img/gecg', 'url')
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def roll(self, ctx, *, fuckw=None):
        """ Roll dubs """
        kike = int(''.join(str(random.randint(0,9)) for _ in range(9)))
        str2 = str(ctx.message)
        if fuckw == "roll":
            kike = str("82340999")
        await ctx.send(f"{ctx.author.mention}, **{kike}**")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['guard'])
    async def skyrim(self, ctx):
        """ Do you get to the ☁️ district very often? """
        
        skyanswer = random.choice(lists.skyrimresponse)
        await ctx.send(f"{skyanswer}")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['randomlain'])
    async def lain(self, ctx):
        """ Posts a random lain """
        
        randomla = random.choice(lists.randlain)
        await ctx.send(f"{randomla}")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['ahiga'])
    async def tsoi(self, ctx):
        """ Posts a random tsoi """
        
        randomts = random.choice(lists.randtsoi)
        await ctx.send(f"{randomts}")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['google'])
    async def search(self, ctx, *, search):
        """ Searches google """
        search = search.lower()
        if "skinwalker" in search or "fleshgait" in search or "shapeshifter" in search:
            return
        if ctx.author.id == 746184398852063393:
            return
        if search.startswith("-image "):
            try:
                search = search.replace("-image ", "")
                if "toddlercon" in search:
                    search = search.replace("toddlercon", "andy sixx log")
                elif "euro girl" in search or "euro woman" in search or "european girl" in search or "european woman" in search:
                    search = "slavic woman"
                elif "689892377871122448" in search:
                    #await ctx.send(f'{search}')
                    search = search.replace("689892377871122448", "lgbt")
                elif "euro" in search:
                    search = search.replace("euro", "europe beauty")
                elif "mexico" in search:
                    search = search.replace("mexico", "venezuela")
                elif "native" in search or "native american" in search:
                    search = "native american warrior art"
                elif "america" in search:
                     if "american" in search:
                        search = search.replace("american", f"{random.choice(['fat american', 'fat black woman', 'amerimutt meme'])}")
                     else:
                         search = search.replace("america", f"{random.choice(['fat american', 'black woman', 'amerimutt', 'BLM', 'pride'])}")
                elif "kansas" in search or "okla" in search or "kan" in search:
                    search = f"{random.choice(['kansas', 'black girl'])}"
                elif "swedish girl" in search or "swedish woman" in search:
                    search = search.replace("swedish", "ukrainian")
                elif "bulgarian" in search:
                    search = search.replace("bulgarian", "bulgarian gypsy")
                elif "japanese" in search:
                    search = search.replace("japanese", f"ugly chinese")
                elif "chinese" in search:
                    search = search.replace("chinese", f"ugly chinese")
                elif "swed" in search or "swee" in search:
                    if "swedish" in search:
                        search = search.replace("swedish", "russian")
                    else:
                        search = "russian people"
                elif "ahig" in search:
                    search = f"{random.choice(['siberian warrior art', 'nenets', 'native american warrior art', 'adolf hitler', 'genghis khan', 'viktor tsoi'])}"
                elif "bury" in search:
                    search = f"{random.choice(['chinese on horse', 'turkic', 'mongolian', 'genghis khan', 'mongolian warrior', 'blood cancer'])}"
                elif "viktor" in search:
                    if "fur" in search:
                        return await ctx.send("fuck u fuck u fuck u fuck u")
                fuckk = search.replace(" ", "_")
                website = f"https://images.search.yahoo.com/search/images?fr=yfp-t&p={str(fuckk)}"
                if "anglo" in search or "british" in search or "english" in search:
                    website = f"https://images.search.yahoo.com/search/images;_ylt=AwrExdr4Jj1ghR8AWQOJzbkF;_ylu=c2VjA3NlYXJjaARzbGsDYnV0dG9u;_ylc=X1MDOTYwNjI4NTcEX3IDMgRhY3RuA2NsawRjc3JjcHZpZAMyV2ViV2pFd0xqSXhUSWpkWC40aVJndHhNVFU0TGdBQUFBQWI0WTgzBGZyA3lmcC10BGZyMgNzYS1ncARncHJpZANjX1h6bDZmVlEwcUljUXY0ZHU3Li5BBG5fc3VnZwMxMARvcmlnaW4DaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMEcXN0cmwDMTQEcXVlcnkDYnJpJ2lzaCUyMG1lbWUEdF9zdG1wAzE2MTQ2MjA0MTc-?p=bri%27ish+meme&fr=yfp-t&fr2=sb-top-images.search&ei=UTF-8&n=60&x=wrt"
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
                fuckme = await ctx.send(embed=embed)

                message_list[ctx.message]=fuckme

                if not permissions.can_upload(ctx):
                    return await ctx.send("I cannot send images here ;>;")
            except Exception as e:
                await ctx.send("No results found!")
        else:
            try:
                await ctx.trigger_typing()
                search = search.replace("-image ", "")
                if "america" in search:
                    if "american" in search:
                        search = search.replace("american", f"{random.choice(['fat american', 'fat black woman', 'amerimutt meme'])}")
                    else:
                        search = search.replace("america", f"{random.choice(['fat american', 'black woman', 'amerimutt', 'BLM', 'pride'])}")
                if "us" in search:
                    if "usa" in search:
                        search = search.replace("usa", f"{random.choice(['amerimutt', 'amerifat', 'amerimutt meme'])}")
                    else:
                        search = search.replace("us", f"{random.choice(['amerimutt', 'amerifat', 'amerimutt meme'])}")
                if "united states" in search:
                    search = search.replace("united states", f"{random.choice(['amerimutt', 'amerifat', 'amerimutt meme'])}")
                    
                search = search.replace(" ", "_")
                number=0
                for j in googlee(search): 
                    number=number+1
                    if number != 5:
                        await ctx.send(f'<{j}>')
                    else:
                        break
            except Exception as e:
                await ctx.send(f"{e}No results found!")


    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def slags(self, ctx):
        """ Searches 4 hot slags """
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
                fuckme = await(await ctx.send(f"{fuckingworkaround}")).delete(delay=30)
                message_list[ctx.message]=fuckme
                await self.bot.process_commands(ctx.message)
        channelid = ctx.channel.name
        await fuckiff()
        if not permissions.can_upload(ctx):
            return await ctx.send("I cannot send images here ;>;")

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def r34(self, ctx, *, search):
        """  Search allthefallen.moe """
        try:
            search = search.lower()
            fuckk = search.replace(" ", "_")
            website = f"https://booru.allthefallen.moe/posts?tags={str(fuckk)}"
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
            fuckme = await(await ctx.send(embed=embed)).delete(delay=30)
            message_list[ctx.message]=fuckme

        except Exception as e:
            await ctx.send("No results found!") 



    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def frog(self, ctx):
        """  random frog """
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
    @commands.command()
    async def drink(self, ctx, user: discord.Member = None, *, reason: commands.clean_content = ""):
        """ Vodka, you're feeling stronger... """
        if not user or user.id == ctx.author.id:
            return await ctx.send(f"**{ctx.author.name}**: 🥃")
        if user.id == self.bot.user.id:
            return await ctx.send("*drinks with you* 🍻")
        if user.bot:
            return await ctx.send(f"Bots are retarded, bro")

        vodka_offer = f"**{user.name}**, you got a <:rak:687399635391741954> offer from **{ctx.author.name}**"
        vodka_offer = vodka_offer + f"\n\n**Reason:** {reason}" if reason else vodka_offer
        msg = await ctx.send(vodka_offer)

        def reaction_check(m):
            if (m.message_id == msg.id and m.user_id == user.id and str(m.emoji) == "🍻"):
                return True
            return False

        try:
            await msg.add_reaction("🍻")
            await self.bot.wait_for('raw_reaction_add', timeout=30.0, check=reaction_check)
            await msg.edit(content=f"**{user.name}** and **{ctx.author.name}** are drinking PISS togetheR 🍻")
        except asyncio.TimeoutError:
            await msg.delete()
            await ctx.send(f"Looks like **{user.name}** wants you to fuck off **{ctx.author.name}**")
        except discord.Forbidden:
            vodka_offer = f"**{user.name}**, you got a 🥃 from **{ctx.author.name}**"
            vodka_offer = vodka_offer + f"\n\n**Reason:** {reason}" if reason else vodka_offer
            await msg.edit(content=vodka_offer)

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['goat'])
    async def satan(self, ctx):
        """ Posts a random satan """
        
        randomsata = random.choice(lists.randsatan)
        await ctx.send(f"{randomsata}")
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def cat(self, ctx):
        """ Posts a random cat """
        await self.randomimageapi(ctx, 'https://nekos.life/api/v2/img/meow', 'url')
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def dog(self, ctx):
        """ Posts a random dog """
        await self.randomimageapi(ctx, 'https://random.dog/woof.json', 'url')
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def birb(self, ctx):
        """ Posts a random birb """
        await self.randomimageapi(ctx, 'https://api.alexflipnote.dev/birb', 'file')
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def duck(self, ctx):
        """ Posts a random duck """
        await self.randomimageapi(ctx, 'https://random-d.uk/api/v1/random', 'url')
    @commands.guild_only()
    @commands.command(aliases=['flip', 'coin'])
    async def coinflip(self, ctx):
        """ Coinflip """
        
        coinsides = ['Heads', 'Tails']
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=2.0, type=commands.BucketType.user)
    async def urban(self, ctx, *, search: str):
        """ Find the 'best' definition to your words """
        
        if search == "gay sex":
            await ctx.send(f"📚 Definitions for **{str(search)}**```fix\nad044```")
            return
        if search == "human":
            await ctx.send(f"📚 Definitions for **{str(search)}**```fix\nNot niggers, not kiksez, not TRAZNIEZ, not DEGENRER8Z xd```")
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
            await ctx.send(f"📚 Definitions for **{str(search)}**```fix\nHoshi also known as Ahiga and Chief Horsecock is the tribal leader of INITIATE. He is abs man.```")
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
    async def reverse(self, ctx, *, text: str):
        """ !ffuts esreveR
        Everything you type after reverse will be reversed
        """
        
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"🔁 {t_rev}")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def password(self, ctx, nbytes: int = 18):
        """ Generates a random password string for you

        This returns a random URL-safe text string, containing nbytes random bytes.
        The text is Base64 encoded, so on average each byte results in approximately 1.3 characters.
        """
        
        if nbytes not in range(3, 1401):
            return await ctx.send("I only accept any numbers between 3-1400")
        if hasattr(ctx, 'guild') and ctx.guild is not None:
            await ctx.send(f"Sending you a private message with your random generated password **{ctx.author.name}**")
        await ctx.author.send(f"🎁 **Here is your password:**\n{secrets.token_urlsafe(nbytes)}")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def rate(self, ctx, *, thing: commands.clean_content):
        """ Rates whatever """
        
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
        
        if user is None:
            user = ctx.author
        random.seed(user.id)
        len = random.randint(0, 30)
        if user.id == 346093616734666764:
            len = 32
        elif user.id == 759621355708350484:
            len = 36
        elif user.id == 857346075585151006:
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
    @commands.command(aliases=['korea','china','chinese','japan','japanese'])
    async def eugene(self, ctx):
        """ posts girlfriend """
        fuckmenigga = ctx.message.author
        
        if not permissions.can_upload(ctx):
            return await ctx.send("I cannot send images here ;>;")

        embed = discord.Embed(color=0xe1a6e1)
        embed.set_image(url=f"{random.choice(['https://cdn.discordapp.com/attachments/660982562331820032/830255400472805386/unknown.png', 'https://cdn.discordapp.com/attachments/660982562331820032/830259400614215710/ghTeUGV.png','https://cdn.discordapp.com/attachments/660982562331820032/830259641945948240/1514827498976.png','https://cdn.discordapp.com/attachments/660982562331820032/830259674976747540/images.png','https://cdn.discordapp.com/attachments/660982562331820032/830260316574318602/tcjaawewdn611.png','https://cdn.discordapp.com/attachments/660982562331820032/830259986763481138/x5OvmcMa4d379zlAVf-35JG_6vOBu_999mDq3T0A_9Ci_W9RDNzmBQPHPGXDpoZSL3BLNL8tgGlkt2dLLLSQFA.png','https://cdn.discordapp.com/attachments/660982562331820032/830260425991389185/61uuafeqbxd01.png'])}")
        await ctx.send(embed=embed)
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['catfucker'])
    async def romet(self, ctx):
        """ owo """
        
        if not permissions.can_upload(ctx):
            return await ctx.send("I cannot send images here ;>;")

        embed = discord.Embed(color=0xe1a6e1)
        romet = random.choice(['https://cdn.discordapp.com/attachments/660982562331820032/819376767688638484/romet.png', 'https://cdn.discordapp.com/attachments/660982562331820032/819376692140834837/romet_kidnapping_astolfo.png'])
        embed.set_image(url=romet)
        await ctx.send(embed=embed)
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['ad'])
    async def ad044(self, ctx, *, message=None):
        """ Femboys are gay"""
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
        try:
            if message is None:
                return
            else:
                await ctx.message.delete()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url('whatever', adapter=AsyncWebhookAdapter(session))
                    username = 'ad044'
                    pfp = 'https://avatars.githubusercontent.com/u/68151384?s=460&u=a3fddb691486dd78ffedb730bbbc8e206407f884&v=4'
                    await webhook.send(f'{message}', username=str(username), avatar_url=str(pfp))
        except Exception as e:
            return

    @commands.command(pass_ctx=True)
    async def anon(self, ctx, *, message: commands.clean_content = ""):
        try:
            if message is None:
                return
            else:
                await ctx.message.delete()
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url('whatever', adapter=AsyncWebhookAdapter(session))
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
                    webhook = Webhook.from_url('whatever', adapter=AsyncWebhookAdapter(session))
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
        
        if not permissions.can_upload(ctx):
            return await ctx.send("I cannot send images here ;>;")

        embed = discord.Embed(color=0xe1a6e1)
        embed.set_image(url="https://cdn.discordapp.com/attachments/595511047205421056/595514059273666560/241.png")
        await ctx.send(embed=embed)

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['fatso'])
    async def fat(self, ctx):
        """ ur fat """
        
        if not permissions.can_upload(ctx):
            return await ctx.send("I cannot send images here ;>;")

        embed = discord.Embed(color=0xe1a6e1)
        embed.set_image(url="https://scontent.harristeeter.com/legacy/productimagesroot/DJ/3/1240133.jpg")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun_Commands(bot))

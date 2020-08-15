import random
import discord
import json
import secrets
import asyncio
import time
import urllib.request
import re
import requests

from io import BytesIO
from discord.ext import commands
from asyncio import sleep
from utils import lists, permissions, http, default
from bs4 import BeautifulSoup

message_list = {}

class Fun_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message_delete(self, message):
        role_names = [role.name for role in message.author.roles]
        if ".search" in message.content or ".google" in message.content: or ".suicide" in message.content:
            await message_list[message].delete()
            del message_list[message]


    @commands.cooldown(1, 20, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def chan(self, ctx, *, quote: commands.clean_content):
        """ Formats in a chan style """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        await ctx.message.delete()
        await ctx.send(f"**Anonymous**  01/06/19(Sun)13:02:01 No.7340664 ► __>>7342278__ __>>7346156__ __>>7347231__\n\n      __>>7339455__\n      {quote}")

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def fuck(self, ctx, *, quote: commands.clean_content):
        """ Fuck my shit up babyeeyyy """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return

        randmm = ["111","222","333","444","555"]
        
        async def niggerfuck():
            listf = list(quote)
            random.shuffle(listf)
            joinf = ''.join(listf)
            await ctx.send(f"{ctx.author}: {joinf}")

        async def kikee():
            answerr = random.choice(lists.fuck)
            await ctx.send(f"{ctx.author}: {answerr}")

        async def eifefdf():
            listff = list(quote)
            random.shuffle(listff)
            wdasdd = random.choice(lists.fuck)
            joinff = ''.join(listff)
            nigger = joinff + wdasdd
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


        answer = random.choice(randmm)
        if "1" in answer or "2" in answer:
            await kikee()
        elif "3" in answer:
            await eifefdf()
        else:
            await niggerfuck()

    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def lainspeak(self, ctx, *, question: commands.clean_content):
        """ Consult Lain """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
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
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
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
    @commands.command(aliases=['toot'])
    async def doot(self, ctx):
        """ Lain doots """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        
        answer = random.choice(lists.doots)
        await ctx.send(f"{answer}")

    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def elonmusk(self, ctx):
        """ FUckING API PIECE OF SHit """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        await self.randomimageapi(ctx, 'https://nekos.life/api/v2/img/gecg', 'url')
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def roll(self, ctx):
        """ Roll dubs """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        kike = int(''.join(str(random.randint(0,9)) for _ in range(9)))
        await ctx.send(f"{fuckmenigga.mention}, **{kike}**")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['guard'])
    async def skyrim(self, ctx):
        """ Do you get to the ☁️ district very often? """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        
        skyanswer = random.choice(lists.skyrimresponse)
        await ctx.send(f"{skyanswer}")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['randomlain'])
    async def lain(self, ctx):
        """ Posts a random lain """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        
        randomla = random.choice(lists.randlain)
        await ctx.send(f"{randomla}")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['randomrat'])
    async def rat(self, ctx):
        """ Posts a random rat """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        
        randomra = random.choice(lists.randrat)
        await ctx.send(f"{randomra}")

    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['google'])
    async def search(self, ctx, *, search):
        """ Searches google """
        try:
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
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
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
    async def frog(self, ctx):
        """  random frog """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
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
    @commands.command()
    async def drink(self, ctx, user: discord.Member = None, *, reason: commands.clean_content = ""):
        """ Vodka, you're feeling stronger... """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
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
            await msg.edit(content=f"**{user.name}** and **{ctx.author.name}** are enjoying RAKIJA togetheR 🍻")
        except asyncio.TimeoutError:
            await msg.delete()
            await ctx.send(f"Looks like **{user.name}** wants you to fuck off **{ctx.author.name}**")
        except discord.Forbidden:
            # Yeah so, bot doesn't have reaction permission, drop the "offer" word
            vodka_offer = f"**{user.name}**, you got a 🥃 from **{ctx.author.name}**"
            vodka_offer = vodka_offer + f"\n\n**Reason:** {reason}" if reason else vodka_offer
            await msg.edit(content=vodka_offer)

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def f(self, ctx, *, text: commands.clean_content = None):
        """ Press F to pay respect """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        hearts = ['❤', '💛', '💚', '💙', '💜']
        reason = f"for **{text}** " if text else ""
        await ctx.send(f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['goat'])
    async def satan(self, ctx):
        """ Posts a random satan """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        
        randomsata = random.choice(lists.randsatan)
        await ctx.send(f"{randomsata}")
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def cat(self, ctx):
        """ Posts a random cat """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        await self.randomimageapi(ctx, 'https://nekos.life/api/v2/img/meow', 'url')
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def dog(self, ctx):
        """ Posts a random dog """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        await self.randomimageapi(ctx, 'https://random.dog/woof.json', 'url')
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def birb(self, ctx):
        """ Posts a random birb """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        await self.randomimageapi(ctx, 'https://api.alexflipnote.dev/birb', 'file')
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def duck(self, ctx):
        """ Posts a random duck """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        await self.randomimageapi(ctx, 'https://random-d.uk/api/v1/random', 'url')
    @commands.guild_only()
    @commands.command(aliases=['flip', 'coin'])
    async def coinflip(self, ctx):
        """ Coinflip """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        
        coinsides = ['Heads', 'Tails']
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    @commands.cooldown(rate=1, per=2.0, type=commands.BucketType.user)
    async def urban(self, ctx, *, search: str):
        """ Find the 'best' definition to your words """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
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
    async def reverse(self, ctx, *, text: str):
        """ !ffuts esreveR
        Everything you type after reverse will be reversed
        """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        
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
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        
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
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
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
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        
        if user is None:
            user = ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        if user.id == 680569176645042298:
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
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        
        if user is None:
            user = ctx.author
        random.seed(user.id)
        len = random.randint(0, 30)
        if user.id == 346093616734666764:
            len = 32
        elif user.id == 680569176645042298:
            len = 36
        elif user.id == 619474845746462721:
            len = 36
        elif user.id == 616958027752538127:
            len = 0
        p = "8" + "="* + len + "D"
        if user.id == 230072934234980353:
            p = "4:3"
        await ctx.send(f"**{user.name}**'s dick is this long:\n{p}")
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['selfdestruct'])
    async def bomb(self, ctx):
        """ Fuck rate limit """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
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
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
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
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
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
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
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
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(aliases=['installnazbol'])
    async def installnazi(self, ctx):
        """ 📯 doot """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
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
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
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
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        
        if not permissions.can_upload(ctx):
            return await ctx.send("I cannot send images here ;>;")

        embed = discord.Embed(color=0xe1a6e1)
        embed.set_image(url="https://scontent.harristeeter.com/legacy/productimagesroot/DJ/3/1240133.jpg")
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Fun_Commands(bot))

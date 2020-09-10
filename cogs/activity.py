import discord
import psutil
import os
import json
import asyncio
import urllib.request
import sqlite3
import re
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from io import BytesIO
from urllib.request import urlopen

from discord.ext import commands
from collections import OrderedDict

from utils import permissions, http

from profanityfilter import ProfanityFilter

client = discord.Client()

class Activity(commands.Cog):
	"""Activity"""
	def __init__(self, bot):
		self.bot = bot
		self.process = psutil.Process(os.getpid())

		self.bot.loop.create_task(self.save_activity())

		with open("/activity.json", 'r') as f:
			self.activity = json.load(f)

	async def save_activity(self):
		await self.bot.wait_until_ready()
		while not self.bot.is_closed():
			with open("/activity.json", 'w') as f:
				json.dump(self.activity, f, indent=4)

			await asyncio.sleep(5)

	def act_up_fuck(self, author_id):
		current_xp = self.activity[author_id]['xp']
		current_lvl = self.activity[author_id]['lvl']
		current_nword = self.activity[author_id]['nword']
		current_credit = self.activity[author_id]['credit']
		if current_xp >= round((4 * (current_lvl ** 3)) / 5):
			self.activity[author_id]['lvl'] += 1
			return True
		else:
			return False

	@commands.Cog.listener()
	async def on_message(self, message):


		negativeph = ['reddit', 'owo', 'bisexual', 'bi sexual', 'bi-sexual', 'ahigay', 'cock', 'femb', 'indica', 'christianity', 'tsuki', 'nibba', 'phobic', 'black p', 'systemsp', 'trans', 'homosexual', 'pog', 'tolerance', 'non binary', 'nonbinary', 'non-binary', 'genderfluid', 'gender fluid', 'gender-fluid', 'femmy', 'cum', 'boyp', 'b0ip', 'boy p', 'b0i p', 'boi p', 'boip', 'b0y p', 'b0y p', 'uwu', 'phobe']
		convoph = ['sup', 'hot', 'initiate', 'great', 'shit', 'shiet', 'raype', 'based', 'redpill', 'https', 'cute', 'loli', 'tomboy']
		channelid = message.channel.name
		if channelid != "degeneral":
			return

		pf = ProfanityFilter()

		if message.author.bot:
			return

		if discord.utils.get(message.author.roles, name="Muted") != None:
			return
		if discord.utils.get(message.author.roles, name="Hardmute") != None:
			return

		author_id = str(message.author.id)
		if not author_id in self.activity:
			self.activity[author_id] = {}
			self.activity[author_id]['lvl'] = 1
			self.activity[author_id]['xp'] = 0
			self.activity[author_id]['nword'] = 0
			self.activity[author_id]['credit'] = 100

		if self.activity[author_id]['credit'] <= 40:
			self.activity[author_id]['credit'] = 100
			role_names = [role.name for role in message.author.roles]
			role_names = role_names[1:]
			for role in role_names:
				fuck = discord.utils.get(message.guild.roles, name=f"{role}")
				#await ctx.send(f"{fuck}")
				try:
					await message.author.remove_roles(fuck)
				except Exception as e:
					return
			await ctx.send(default.actionmessage("kicked! Reason: Low credit"))

		if self.activity[author_id]['credit'] >= 1000:
			self.activity[author_id]['credit'] = 1000

		if pf.is_profane(f"{message.content}") == True:
			self.activity[author_id]['credit'] += 50

		if re.compile('|'.join(convoph),re.IGNORECASE).search(message.content): 
			self.activity[author_id]['credit'] += 10
		if re.compile('|'.join(negativeph),re.IGNORECASE).search(message.content): 
			self.activity[author_id]['credit'] -= 50

		self.activity[author_id]['xp'] += 1
		if self.act_up_fuck(author_id):
			print(f"leveled up!\n Level: {self.activity[author_id]['lvl']}")


	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.bot:
			return

		if discord.utils.get(message.author.roles, name="Muted") != None:
			return
		if discord.utils.get(message.author.roles, name="Hardmute") != None:
			return

		author_id = str(message.author.id) #if in message content or in message content or in message content or in message content or in message content or in message content or in message content 
		if "nigger" in message.content or "niggers" in message.content or "NIGGER" in message.content or "NIGGERS" in message.content:
			s = str(message.content)
			sb = 'nigger'
			results = 0
			sub_len = len(sb)
			for i in range(len(s)):
				if s[i:i+sub_len] == sb:
					results += 1
			self.activity[author_id]['nword'] += results



	@commands.Cog.listener()
	async def on_member_update(self, before, after):
		channel = self.bot.get_channel(channelid)
		author_id = str(after.id)
		if len(before.roles) < len(after.roles):
			new_role = next(role for role in after.roles if role not in before.roles)
			if new_role.name in ('Server Booster'):
				await channel.send(f"❤️ {after.mention} thank you for the boost! You've been given 100 xp, and more credit!")
				self.activity[author_id]['xp'] += 100
				self.activity[author_id]['credit'] += 500
				if self.act_up_fuck(author_id):
					print(f"leveled up!\n Level: {self.activity[author_id]['lvl']}")

	@commands.Cog.listener()
	async def on_voice_state_update(self, member, before, after):
		if not before.channel and after.channel:
			author_id = str(member.id)
			self.activity[author_id]['credit'] += 80

	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command(aliases=["give"], hidden=True)
	@permissions.has_permissions(kick_members=True)
	async def add(self, ctx, member: discord.Member = None, *, amount: int = None):
		""" Give credit """
		fuckmenigga = ctx.message.author
		if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
			return
		if not member:
			await ctx.send("Please @ a user")
			return
		else:
			member = member
		member_id = str(member.id)
		try:
			self.activity[member_id]['credit'] += amount 
			await ctx.message.add_reaction(chr(0x2705))
		except Exception as e:
			await ctx.send("Please enter a valid number")

	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command(aliases=["remove"], hidden=True)
	@permissions.has_permissions(kick_members=True)
	async def subtract (self, ctx, member: discord.Member = None, *, amount: int = None):
		""" Remove credit """
		fuckmenigga = ctx.message.author
		if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
			return
		if not member:
			await ctx.send("Please @ a user")
			return
		else:
			member = member
		member_id = str(member.id)
		try:
			self.activity[member_id]['credit'] -= amount 
			await ctx.message.add_reaction(chr(0x2705))
		except Exception as e:
			await ctx.send("Please enter a valid number")


	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command()
	async def level(self, ctx, member: discord.Member = None):
		""" Check yours or other's activity level """
		fuckmenigga = ctx.message.author
		if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
			return
		if not member:
			member = ctx.author
		else:
			member = member
		member_id = str(member.id)
		if not member_id in self.activity:
			embed = discord.Embed(color=10688020,
							title=f"**__Error__**")
			embed.description = f"You'e not active, newfag"
			await ctx.send(embed=embed)
		else:
			embed = discord.Embed(color=member.color,
							title=f"**__Level__**")
			embed.description = f"You're level {self.activity[member_id]['lvl']}\nXP: {self.activity[member_id]['xp']}\nN-words said: {self.activity[member_id]['nword']}"
			await ctx.send(embed=embed)



	@commands.cooldown(1, 10, commands.BucketType.user)
	@commands.command(aliases=["credit"])
	async def profile(self, ctx, member: discord.Member = None):
		""" Display your profile """
		if not member:
			member = ctx.author
		else:
			member = member
		member_id = str(member.id)
		if discord.utils.get(member.roles, name="Muted") != None:
			return
		try:
			DB_NAME = "init"
			db_path = os.path.abspath("database path")
			print(f"{db_path}")
			self.db = sqlite3.connect(db_path)
			self.db_cursor = self.db.cursor()
	
	
			url = str(member.avatar_url)
			bio = BytesIO(await http.get(url, res_method="read"))
			pfp = Image.open(bio)
			im = Image.open(urlopen('https://raw.githubusercontent.com/39hige1/initiatetheme/master/profilee.png')) 
			img = im.copy()
			pfpc = pfp.copy()
	
			width, height = pfpc.size;
			asp_rat = width/height;
	
			new_width = 99;
			new_height = 99;
	
			new_rat = new_width/new_height;
	
			if (new_rat == asp_rat):
				pfpc = pfpc.resize((new_width, new_height), Image.ANTIALIAS); 
			else:
				new_height = round(new_width / asp_rat);
				pfpc = pfpc.resize((new_width, new_height), Image.ANTIALIAS);
	
			draw = ImageDraw.Draw(img)
			font = ImageFont.truetype('/Modern_Sans_Light.otf', 20) 
			font2 = ImageFont.truetype('/Modern_Sans_Light.otf', 30) 
			draw.text((10, 10), "Credit Score:", (255, 255, 255), font=font)
			if self.activity[member_id]['credit'] >= 600:
				draw.text((10, 70), ":D", (255, 255, 255), font=font) 
			elif self.activity[member_id]['credit'] <= 200:
				draw.text((10, 70), ":(", (255, 255, 255), font=font)
			else:
				draw.text((10, 70), ":/", (255, 255, 255), font=font)
			draw.text((10, 30), "{}".format(self.activity[member_id]['credit']), (255, 255, 255), font=font2) 
			draw.text((20, 110), "{}".format(member), (255, 255, 255), font=font) 
			draw.text((20, 130), "_________", (255, 255, 255), font=font) 
			draw.text((20, 170), "XP:  {}".format(self.activity[member_id]['xp']), (255, 255, 255), font=font)
			draw.text((20, 190), "Level:  {}".format(self.activity[member_id]['lvl']), (255, 255, 255), font=font)

			img.paste(pfpc, (171, 57))
	
			try:
				listing = self.db_cursor.execute("query goes here")
				response = self.db_cursor.fetchall()
				try:
					for row in response:
						draw.text((20, 210), "Status: {}".format(row[11]), (255, 255, 255), font=font) 
						draw.text((20, 230), "User Number: {}".format(row[0]), (255, 255, 255), font=font) 
						draw.text((20, 250), "Active: {}".format(row[6]), (255, 255, 255), font=font)
						self.db.close()
				except Exception as e:
					await ctx.send(f"You probably didn't set your username on the website!")
					self.db.close()
				self.db.close()
			except Exception as e:
				await ctx.send(f"You probably didn't set your username on the website!")
				self.db.close()
			img.save('/profile/infoimg2.png') 
			with open('/profile/infoimg2.png', 'rb') as fp:
				await ctx.send(file=discord.File(fp, "penis.png"))
			self.db.close()
		except Exception as e:
			await ctx.send(f"Something went wrong!")


def setup(bot):
    bot.add_cog(Activity(bot))

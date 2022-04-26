import discord
import psutil
import os
import asyncio
import urllib.request
import re
import sqlite3
import random

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from io import BytesIO
from urllib.request import urlopen

from discord.ext import commands
from collections import OrderedDict

from utils import default
from utils import permissions, http, default, repo, lists

from better_profanity import profanity

from datetime import datetime, timedelta

import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from textblob import TextBlob

async def send_cmd_help(ctx):
	if ctx.invoked_subcommand:
		await ctx.send_help(str(ctx.invoked_subcommand))
	else:
		await ctx.send_help(str(ctx.command))

class Activity(commands.Cog):
	"""Activity"""
	def __init__(self, bot):
		self.bot = bot
		self.config = default.get("config.json")
		self.process = psutil.Process(os.getpid())


	def act_up_fuck(self, user):
		current_xp = user[1]
		current_lvl = user[2]
		current_nword = user[3]
		current_credit = user[4]
		if current_xp >= round((4 * (current_lvl ** 3)) / 5):
			print("levelnggegjeujeuef")
			return True
		else:
			return False

	@commands.Cog.listener()
	async def on_ready(self):
		db_path = f"{self.config.database2}"
		print(f"I fugging hate niggers {db_path}")
		sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS fucku (
											UserID character varying NOT NULL,
											XP integer DEFAULT 0,
											Level integer DEFAULT 0,
											Nword integer DEFAULT 0,
											Credit integer DEFAULT  0,
											XPLock text DEFAULT CURRENT_TIMESTAMP,
		 									GuildID character varying
										); """
		print(f"sql query loaded")
		self.db = sqlite3.connect(db_path)
		self.db_cursor = self.db.cursor()
		print(f"Connected")
		if self.db is not None:
			self.db_cursor.execute(sql_create_projects_table)
			self.db.commit()
			print(f"Committting fuck")
			print(f"done")


	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.bot or message.content.startswith("."):
			return
		message.content = message.content.lower()

		channelidd = message.channel.id
		if random.random() < 0.004:
			await message.channel.send(f'{message.author} {random.randint(1, 100)} cocks fucking you')

		db_path = f"{self.config.database2}"
		self.db = sqlite3.connect(db_path)
		self.db_cursor = self.db.cursor()
		print(f"Connected")


		if discord.utils.get(message.author.roles, name="Muted") != None:
			return
		if discord.utils.get(message.author.roles, name="Hardmute") != None:
			return

		author_id = str(message.author.id)
		guild_id = str(message.guild.id)


		negativeph = ['catboy','catgirl',':3','nya','trap','swedish retard','swedish_retard','coom', 'shit bot', 'reddit', 'owo', 'bisexual', 'bi sexual', 'bi-sexual', 'ahigay', 'cock', 'femboy','fem boy','fem-boy','femb0y','fem b0y','shitbot', 'indica', 'christianity', 'tsuki', 'nibba', 'black people', 'systemspace', 'transexual','transsexual','trans' 'homosexual', 'pog','poggers', 'tolerance', 'non binary', 'nonbinary', 'non-binary', 'genderfluid', 'gender fluid', 'gender-fluid', 'femmy', 'cum', 'boypussy', 'b0ipussy', 'boy pussy', 'b0i pussy', 'boi pussy', 'boipussy', 'b0y pussy', 'b0y pussy', 'uwu']
		convoph = ['sup', 'hot', 'initiate', 'great', 'shit', 'shiet', 'raype', 'based', 'redpill', 'https', 'cute', 'loli', 'tomboy','femoid']
		hebrw = ('א','בּ','ב','גּ','ג','דּ','ד','ה','ו','וּ','ח','ם','מ ','ס','ף','ע','ק','תּ','ת','ר','ע','שׂ')
		cyrillic = ('а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','ц','ч','ш','щ','ъ','ы','ь','э','ю','я')
		channelid = message.channel.name
		#if channelid != "degeneral":
		#	return

		self.db_cursor.execute(f"SELECT * FROM fucku WHERE UserID='{author_id}' AND GuildID='{guild_id}'")
		user = self.db_cursor.fetchone()
		if user:
			xplock = user[5]
			currentcredit = int(user[4])
			currentbalance = int(user[7])
			displaynick = str(user[8])
			displaypfp = str(user[9])
			print("User found")
			sql = ("UPDATE fucku SET XP=? WHERE UserID=? AND GuildID=?")
			val = (int(user[1] + 1), int(message.author.id), int(message.guild.id))
			#print(f"test {currenttime}")
			self.db_cursor.execute(sql, val)
			self.db.commit()

			if displaynick != str(message.author.display_name):
				sql = ("UPDATE fucku SET DisplayName=? WHERE UserID=? AND GuildID=?")
				val = (str(message.author.display_name), int(message.author.id), int(message.guild.id))
				self.db_cursor.execute(sql, val)
				self.db.commit()
				print("Updating nick...")
			if "php" in message.author.display_name:
				sql = ("UPDATE fucku SET DisplayName=? WHERE UserID=? AND GuildID=?")
				val = (str("faggot"), int(message.author.id), int(message.guild.id))
				self.db_cursor.execute(sql, val)
				self.db.commit()
				print("Updating nick...")
			if "?>" in message.author.display_name:
				sql = ("UPDATE fucku SET DisplayName=? WHERE UserID=? AND GuildID=?")
				val = (str("faggot"), int(message.author.id), int(message.guild.id))
				self.db_cursor.execute(sql, val)
				self.db.commit()
				print("Updating nick...")
			if displaypfp != str(message.author.avatar_url):
				sql = ("UPDATE fucku SET DisplayPFP=? WHERE UserID=? AND GuildID=?")
				val = (str(message.author.avatar_url), int(message.author.id), int(message.guild.id))
				self.db_cursor.execute(sql, val)
				self.db.commit()
				print("Updating pfp...")

			if currentcredit >= 1300:
				sql = ("UPDATE fucku SET Credit=1300 WHERE UserID=? AND GuildID=?")
				val = (int(message.author.id), int(message.guild.id))
				self.db_cursor.execute(sql, val)
				self.db.commit()

			if currentcredit in range(1290, 1300):
				try:
					sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
					val = (int(user[4] - 10), int(message.author.id), int(message.guild.id))
					self.db_cursor.execute(sql, val)
					self.db.commit()
				except Exception as e:
					print(f'{e}')

			if datetime.utcnow() > datetime.fromisoformat(xplock):
				for i in cyrillic:
					if i in message.content:
						sql = ("UPDATE fucku SET Credit=?, XPLock=? WHERE UserID=? AND GuildID=?")
						val = (int(user[4] + 4), (datetime.utcnow()+timedelta(seconds=5)).isoformat(), int(message.author.id), int(message.guild.id))
						self.db_cursor.execute(sql, val)
						self.db.commit()
						print(f"added +4")

				if profanity.contains_profanity(f"{message.content}"):
					sql = ("UPDATE fucku SET Credit=?, XPLock=? WHERE UserID=? AND GuildID=?")
					val = (int(user[4] + 4), (datetime.utcnow()+timedelta(seconds=5)).isoformat(), int(message.author.id), int(message.guild.id))
					self.db_cursor.execute(sql, val)
					self.db.commit()
					print(f"added +4")

				if re.compile('|'.join(convoph),re.IGNORECASE).search(message.content): 
					sql = ("UPDATE fucku SET Credit=?, XPLock=? WHERE UserID=? AND GuildID=?")
					val = (int(user[4] + 4), (datetime.utcnow()+timedelta(seconds=5)).isoformat(), int(message.author.id), int(message.guild.id))
					self.db_cursor.execute(sql, val)
					self.db.commit()
					print(f"added +4")

				#sid_obj = SentimentIntensityAnalyzer() 
				#sentiment_dict = sid_obj.polarity_scores(message.content)
				channell = self.bot.get_channel(857815170213871618) 
				testimonial = TextBlob(message.content)
				if (testimonial.sentiment.polarity > 0.1):
					#await channell.send(f"textblob says polarity positive")
					polar = 1
				elif(testimonial.sentiment.polarity <= 0.1 and  testimonial.sentiment.polarity >= -0.1):
					#await channell.send(f"textblob says polarity neutral")
					polar = 0
				else:
					#await channell.send(f"textblob says polarity negative")
					polar = -1

				if (testimonial.sentiment.subjectivity < 0.9):
					#await channell.send(f"textblob says sentance is positive")
					happy = 1
				elif(testimonial.sentiment.subjectivity <= 0.1 and  testimonial.sentiment.subjectivity >= -0.1):
					#await channell.send(f"textblob says sentance is neutral")
					happy = 0
				else:
					#await channell.send(f"textblob says sentance is negative")
					polar = -1

				if polar >= 0 and happy >= 0:
					if polar == 0:
						return
					else:
						sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
						val = (int(user[4] + 1), int(message.author.id), int(message.guild.id))
						self.db_cursor.execute(sql, val)
						self.db.commit()
						#await channell.send(f"+1")
				elif polar <= 0 or happy <= 0:
					sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
					val = (int(user[4] - 1), int(message.author.id), int(message.guild.id))
					self.db_cursor.execute(sql, val)
					self.db.commit()
					#await channell.send(f"-1")


				await channell.send(testimonial.sentiment)
				
				#if sentiment_dict['compound'] >= 0.05: 
				#	await channell.send("Positive") 
				#	sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
				#	val = (int(user[4] + 1), int(message.author.id), int(message.guild.id))
				#	self.db_cursor.execute(sql, val)
				#	self.db.commit()
				#	#await(await message.channel.send(f'{message.author} 伴侶 ! *[+1]* ')).delete(delay=3)
				#elif sentiment_dict['compound'] <= - 0.05: 
				#	await channell.send("Negative") 
				#	sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
				#	val = (int(user[4] - 1), int(message.author.id), int(message.guild.id))
				#	self.db_cursor.execute(sql, val)
				#	self.db.commit()
				#	#await(await message.channel.send(f'{message.author} 坏公民! *[-1]* 个社会信用')).delete(delay=3)
				#else: 
				#	await channell.send("Neutral") 


			for b in hebrw:
				if b in message.content:
					try:
						sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
						val = (int(user[4] - 100), int(message.author.id), int(message.guild.id))
						self.db_cursor.execute(sql, val)
						self.db.commit()
						print(f"removed -15")
						await(await message.channel.send(f'{message.author} 坏公民! *[-100]* 个社会信用')).delete(delay=3)
					except Exception as e:
						print(f'{e}')

			if "initiate" in message.content:
				if profanity.contains_profanity(f"{message.content}"):
					try:
						sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
						val = (int(user[4] - 10), int(message.author.id), int(message.guild.id))
						self.db_cursor.execute(sql, val)
						self.db.commit()
						print(f"removed -15")
						await(await message.channel.send(f'{message.author} 坏公民! *[-10]* 个社会信用')).delete(delay=3)
					except Exception as e:
						print(f'{e}')

			if "flag_us" in message.content or "🇺🇸" in message.content:
				try:
					sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
					val = (int(user[4] - 100), int(message.author.id), int(message.guild.id))
					self.db_cursor.execute(sql, val)
					self.db.commit()
					print(f"removed -100")
					await(await message.channel.send(f'{message.author} 坏公民! *[-100]* 个社会信用')).delete(delay=3)
				except Exception as e:
					print(f'{e}')

			if "https://discord.gg/" in message.content:
				try:
					sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
					val = (int(user[4] - 100), int(message.author.id), int(message.guild.id))
					self.db_cursor.execute(sql, val)
					self.db.commit()
					print(f"removed -100")
					await(await message.channel.send(f'{message.author} 坏公民! *[-100]* 个社会信用')).delete(delay=3)
				except Exception as e:
					print(f'{e}')

			if re.compile(r'\b(?:%s)\b' % '|'.join(negativeph),re.IGNORECASE).search(message.content): 
				try:
					sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
					val = (int(user[4] - 15), int(message.author.id), int(message.guild.id))
					self.db_cursor.execute(sql, val)
					self.db.commit()
					print(f"removed -50")
					await(await message.channel.send(f'{message.author} 坏公民! *[-15]* 个社会信用')).delete(delay=3)
				except Exception as e:
					print(f'{e}')



			if self.act_up_fuck(user):
				print(f"leveled up!")
				current_xp = int(user[1])
				current_lvl = int(user[2])
				if current_xp >= round((4 * (current_lvl ** 3)) / 5):
					sql = ("UPDATE fucku SET Level=? WHERE UserID=? AND GuildID=?")
					val = (int(user[2] + 1), int(message.author.id), int(message.guild.id))

					self.db_cursor.execute(sql, val)
					self.db.commit()

			if currentcredit <= 1:
				sql = ("UPDATE fucku SET Credit=1 WHERE UserID=? AND GuildID=?")
				val = (int(message.author.id), int(message.guild.id))
				self.db_cursor.execute(sql, val)
				self.db.commit()
			#if currentbalance <= 1:
			#	sql = ("UPDATE fucku SET balance=1 WHERE UserID=? AND GuildID=?")
			#	val = (int(message.author.id), int(message.guild.id))
			#	self.db_cursor.execute(sql, val)
			#	self.db.commit()
			if currentbalance <= -10:
				sql = ("UPDATE fucku SET Credit=1 WHERE UserID=? AND GuildID=?")
				val = (int(user[4] - 1), int(message.author.id), int(guild_id))
				self.db_cursor.execute(sql, val)
				self.db.commit()
				await(await message.channel.send(f'{message.author} 坏公民! *[-1]* 个社会信用')).delete(delay=3)

			if currentcredit <= 500:
				await message.channel.send(f'{message.author} {random.choice(lists.badcitizen)}')
				nickname = str(message.author.display_name)
				channelid = message.channel.name
				if channelid != "degeneral":
					await message.delete()
				newnick = f"{nickname} ## DISCREDITED"
				if "None" in nickname:
					nickname = str(message.author.display_name)
					newnick = f"{nickname} ## DISCREDITED"
					await message.author.edit(nick=f"{newnick}")
				else:
					await message.author.edit(nick=f"{newnick}")
				try:
					role = discord.utils.get(message.guild.roles, name="INITIATE GOLD")
					await message.author.remove_roles(role)
					sql = ("UPDATE fucku SET balance=? WHERE UserID=? AND GuildID=?")
					val = (int(user[7] - 5), int(ctx.author.id), int(guild_id))
					self.db_cursor.execute(sql, val)
				except Exception as e:
					print(e)

			if currentcredit >= 1200:
				try:
					role = discord.utils.get(message.guild.roles, name="INITIATE GOLD")
					await message.author.add_roles(role)
				except Exception as e:
					print(e)

			if message.mentions:
				if profanity.contains_profanity(f"{message.content}"):
					try:
						lst = []
						lst.append(currentcredit)
						self.db_cursor.execute(f"SELECT * FROM fucku WHERE UserID='{message.mentions[0].id}' AND GuildID='{guild_id}'")
						user = self.db_cursor.fetchone()
						if user:
							currentcreditt = int(user[4])
							if any(y > currentcreditt for y in lst):
								amountt = 50
								await message.channel.send(f'{message.author} Bullying is supported by the CCP做得好！')
							else:
								await message.channel.send(f'{message.author} 不要侮辱你的上级!')
							self.db_cursor.close()
					except Exception as e:
						await message.channel.send(f'{e}')

			if "nigger" in message.content.lower():
				s = str(message.content.lower())
				sb = 'nigger'
				results = 0
				sub_len = len(sb)
				for i in range(len(s)):
					if s[i:i+sub_len] == sb:
						results += 1

				fuckk = int(results)

				await message.channel.send(f'{fuckk}')

				sql = ("UPDATE fucku SET Nword=? WHERE UserID=? AND GuildID=?")
				val = (int(user[3] + fuckk), int(message.author.id), int(message.guild.id))
				self.db_cursor.execute(sql, val)
				self.db.commit()
			try:
				self.db_cursor.close()
			except Exception as e:
				await message.channel.send(f'{e}')
				#return
		else:
			print(f"User not found proceeding...")
			sql = ("INSERT INTO fucku (UserID, XP, Level, Nword, Credit, GuildID) VALUES (?, ?, ?, ?, ?, ?)")
			val = (int(message.author.id), 1, 1, 0, 900, int(message.guild.id))
			self.db_cursor.execute(sql, val)
			print(f"inserted {val}")
			self.db.commit()
			print(f"committed")
			try:
				self.db_cursor.close()
			except Exception as e:
				return


	@commands.Cog.listener()
	async def on_member_update(self, before, after):
		db_path = f"{self.config.database2}"
		self.db = sqlite3.connect(db_path)
		self.db_cursor = self.db.cursor()
		channel = self.bot.get_channel(660982562331820032)
		author_id = str(after.id)
		guild_id = str(after.guild.id)

		if len(before.roles) < len(after.roles):
			new_role = next(role for role in after.roles if role not in before.roles)
			if new_role.name in ('Server Booster'):
				await channel.send(f"❤️ {after.mention} thank you for the boost! You've been given 100 xp, and more credit!")
				#await self.db_cursor.execute("UPDATE fucku SET XP=$1 WHERE UserID=$3 AND GuildID=$4", user[4] + 100, user['user_id'], user['guild_id'])
				#await self.db_cursor.execute("UPDATE fucku SET Credit=$1 WHERE UserID=$3 AND GuildID=$4", user[4] + 500, user['user_id'], user['guild_id'])
				self.db_cursor.execute(f"SELECT * FROM fucku WHERE UserID='{author_id}' AND GuildID='{guild_id}'")
				user = self.db_cursor.fetchone()
				if user:
					print("User found")
					sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
					val = (int(user[4] + 100), int(after.id), int(after.guild.id))
					self.db_cursor.execute(sql, val)
					self.db.commit()
				else:
					return
				if self.act_up_fuck(user):
					print(f"leveled up!")
					current_xp = int(user[1])
					current_lvl = int(user[2])
					if current_xp >= round((4 * (current_lvl ** 3)) / 5):
						sql = ("UPDATE fucku SET Level=? WHERE UserID=? AND GuildID=?")
						val = (int(user[2] + 1), int(message.author.id), int(message.guild.id))

						self.db_cursor.execute(sql, val)
						self.db.commit()
				self.db_cursor.close()


	@commands.Cog.listener()
	async def on_voice_state_update(self, member, before, after):
		db_path = f"{self.config.database2}"
		self.db = sqlite3.connect(db_path)
		self.db_cursor = self.db.cursor()
		channel = self.bot.get_channel(710302918074564659)
		author_id = str(after.member.id)
		guild_id = str(after.guild.id)

		if not before.channel and after.channel:
			author_id = str(member.id)
			self.db_cursor.execute(f"SELECT * FROM fucku WHERE UserID='{author_id}' AND GuildID='{guild_id}'")
			user = self.db_cursor.fetchone()
			if user:
				print("User found")
				sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
				val = (int(user[4] + 3), int(after.id), int(after.guild.id))
				self.db_cursor.execute(sql, val)
				self.db.commit()
				print(f"added +3 ")
			try:
				self.db_cursor.close()
			except Exception as e:
				return
			else:
				return

	@commands.Cog.listener()
	async def on_voice_state_update(self, member, before, after):
		if before.channel == after.channel:
			return
		"""
		3 cases:
		1. Join a channel => get a nickname
		2. Change channel => change nickname
		3. Leave a channel => get back my own nickname
		"""
		nickname = str(member.nick)
		if before.channel is None and after.channel is not None:
			# JOIN
			print(f'join')
			if "None" in nickname:
				nickname = str(member.display_name)
			elif "🎵" in nickname:
				return
			newnick = f"{nickname} 🎵"
			print(f'{nickname} | {newnick} setting fuck nigger')
			await member.edit(nick=f"{newnick}")
		elif before.channel is not  None and after.channel is None:
			# LEAVE
			print(f'leave')
			s = nickname.replace('🎵', '')
			newnick = f"{s}"
			print(f'{nickname} | {newnick} setting fuck nigger')
			await member.edit(nick=f"{newnick}")
		else:
			return

	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command(hidden=True)
	@permissions.has_permissions(kick_members=True)
	async def add(self, ctx, member: discord.Member = None, *, amount: int = None):
		""" Give credit """
		db_path = f"{self.config.database2}"
		self.db = sqlite3.connect(db_path)
		self.db_cursor = self.db.cursor()
		fuckmenigga = ctx.message.author
		if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
			return
		if not member:
			member = ctx.author
		else:
			member = member
		member_id = str(member.id)
		guild_id = str(ctx.guild.id)

		self.db_cursor.execute(f"SELECT * FROM fucku WHERE UserID='{member_id}' AND GuildID='{guild_id}'")
		user = self.db_cursor.fetchone()
		if user:
			print("User founddddd")
			sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
			val = (int(user[4] + amount), int(member_id), int(guild_id))
			self.db_cursor.execute(sql, val)
			self.db.commit()
			await ctx.message.add_reaction(chr(0x2705))
			print(f"added {amount}")
			try:
				self.db_cursor.close()
			except Exception as e:
				return
		else:
			return


	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command()
	async def level(self, ctx, member: discord.Member = None):
		""" Check yours or other's activity level """
		db_path = f"{self.config.database2}"
		self.db = sqlite3.connect(db_path)
		self.db_cursor = self.db.cursor()
		fuckmenigga = ctx.message.author
		if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
			return
		if not member:
			member = ctx.author
		else:
			member = member
		member_id = str(member.id)
		guild_id = str(ctx.guild.id)

		self.db_cursor.execute(f"SELECT * FROM fucku WHERE UserID='{member_id}' AND GuildID='{guild_id}'")
		user = self.db_cursor.fetchall()

		if user is None:
			embed = discord.Embed(color=10688020,
							title=f"**__Error__**")
			embed.description = f"You'e not active, newfag"
			await ctx.send(embed=embed)
		else:
			for row in user:
				embed = discord.Embed(color=member.color,
								title=f"**__Level__**")
				embed.description = f"**You're level**: {row[2]}\n**XP**: {row[1]}\n**N-words said**: {row[3]}\n**Social Credit**: {row[4]}"
				await(await ctx.send(embed=embed)).delete(delay=10)
			try:
				self.db_cursor.close()
			except Exception as e:
				return


	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command()
	async def nigger(self, ctx):
		""" Check nigger word xd"""
		db_path = f"{self.config.database2}"
		self.db = sqlite3.connect(db_path)
		self.db_cursor = self.db.cursor()
		fuckmenigga = ctx.message.author
		if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
			return
		self.db_cursor.execute(f"SELECT * FROM fucku ORDER BY Nword DESC")
		user = self.db_cursor.fetchall()
		i = 1
		embedColour = ctx.me.top_role.colour
		embed = discord.Embed(colour=embedColour, title="fuckfuckfuckfuckfuckfuckfuck")
		for row in user:
			try:
				embed.add_field(name=f"{i}: {row[8]}", value=f"Nwords: {row[3]}", inline=False)
				i += 1
			except:
				pass
			if i == 11:
				break
		await ctx.send(embed=embed)
		try:
			self.db_cursor.close()
		except Exception as e:
			return


	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command()
	async def give (self, ctx, member: discord.Member = None, *, amount: int):
		""" Give CC """
		fuckmenigga = ctx.message.author
		if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
			return
		if not member:
			member = ctx.author
		if member == ctx.author:
			return
		else:
			member = member
		if "-" in ctx.message.content:
			return
		member_id = str(member.id)
		guild_id = str(ctx.guild.id)

		db_path = f"{self.config.database2}"
		self.db = sqlite3.connect(db_path)
		self.db_cursor = self.db.cursor()

		self.db_cursor.execute(f"SELECT * FROM fucku WHERE UserID='{ctx.author.id}' AND GuildID='{guild_id}'")
		user = self.db_cursor.fetchone()

		if user:
			print("User foundddd")
			if amount > int(user[7]):
				return
			sql = ("UPDATE fucku SET balance=? WHERE UserID=? AND GuildID=?")
			val = (int(user[7] - amount), int(ctx.author.id), int(guild_id))
			self.db_cursor.execute(sql, val)
			self.db.commit()

			self.db = sqlite3.connect(db_path)
			self.db_cursor = self.db.cursor()
			self.db_cursor.execute(f"SELECT * FROM fucku WHERE UserID='{member_id}' AND GuildID='{guild_id}'")
			user = self.db_cursor.fetchone()

			sqll = ("UPDATE fucku SET balance=? WHERE UserID=? AND GuildID=?")
			vall = (int(user[7] + amount), int(member_id), int(guild_id))
			self.db_cursor.execute(sqll, vall)
			self.db.commit()
			await ctx.message.add_reaction(chr(0x2705))
			print(f"removed {amount}")
			try:
				self.db_cursor.close()
			except Exception as e:
				return
		else:
			return

	@commands.cooldown(1, 10, commands.BucketType.user)
	@commands.command(aliases=['credit'])
	async def profile(self, ctx, member: discord.Member = None):
		""" Check yours or other's activity level """
		db_path = f"{self.config.database2}"
		self.db = sqlite3.connect(db_path)
		self.db_cursor = self.db.cursor()
		fuckmenigga = ctx.message.author
		if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
			return
		if not member:
			member = ctx.author
		else:
			member = member
		member_id = str(member.id)
		guild_id = str(ctx.guild.id)

		self.db_cursor.execute(f"SELECT * FROM fucku WHERE UserID='{member_id}' AND GuildID='{guild_id}'")
		user = self.db_cursor.fetchone()

		if user is None:
			embed = discord.Embed(color=10688020,
							title=f"**__Error__**")
			embed.description = f"You'e not active, newfag"
			await(await ctx.send(embed=embed)).delete(delay=10)
		else:
			currentcredit = int(user[4])
			currentbalance = int(user[7])
			currentxp = int(user[1])
			currentlvle = int(user[2])
			currentnigger = int(user[3])
			for row in user:
				a_string  = str(member.created_at)
				split_string = a_string.split("-", 1)
				substring = split_string[0]
				year = int(substring)
				zodiacYear = year % 12 
				if zodiacYear == 0:
					zodiacAnimal = "Monkey"
				elif zodiacYear == 1:
					zodiacAnimal = "Rooster"
				elif zodiacYear == 2:
					zodiacAnimal = "Dog"
				elif zodiacYear == 3:
					zodiacAnimal = "Pig"
				elif zodiacYear == 4: 
					zodiacAnimal = "Rat"
				elif zodiacYear == 5: 
					zodiacAnimal = "Ox"
				elif zodiacYear == 6:
					zodiacAnimal = "Tiger"
				elif zodiacYear == 7:
					zodiacAnimal = "Rabbit"
				elif zodiacYear == 8:
					zodiacAnimal = "Dragon"
				elif zodiacYear == 9:
					zodiacAnimal = "Snake"
				elif zodiacYear == 10:
					zodiacAnimal = "Horse"
				else: 
					zodiacAnimal = "Sheep"

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
				font = ImageFont.truetype('/home/ahigaaa/Laikabotfuck/cogs/Modern_Sans_Light.otf', 20) 
				font2 = ImageFont.truetype('/home/ahigaaa/Laikabotfuck/cogs/Modern_Sans_Light.otf', 30) 
				font3 = ImageFont.truetype('/home/ahigaaa/Laikabotfuck/cogs/Modern_Sans_Light.otf', 15) 
				draw.text((10, 10), "Credit Score:", (255, 255, 255), font=font)
				if currentcredit >= 1029:
					draw.text((10, 70), ":D", (255, 255, 255), font=font) 
				elif currentcredit <= 600:
					draw.text((10, 70), ":(", (255, 255, 255), font=font)
				elif currentcredit <= 959:
					draw.text((10, 70), ":/", (255, 255, 255), font=font)
				elif currentcredit <= 1029:
					draw.text((10, 70), ":)", (255, 255, 255), font=font)
				else:
					draw.text((10, 70), ":/", (255, 255, 255), font=font)
				draw.text((10, 30), "{}".format(currentcredit), (255, 255, 255), font=font2) 
				draw.text((20, 110), "{}".format(member), (255, 255, 255), font=font) 
				draw.text((20, 130), "_________", (255, 255, 255), font=font) 
				draw.text((20, 170), "Zodiac:  {}".format(zodiacAnimal), (255, 255, 255), font=font)
				draw.text((20, 190), "Level:  {}".format(currentlvle), (255, 255, 255), font=font)
				draw.text((20, 210), "Nwords: {}".format(currentnigger), (255, 255, 255), font=font)
				img.paste(pfpc, (171, 57))
				try:
					self.db_cursor.close()
				except Exception as e:
					return
	
				db_path = f"{self.config.database1}"
				print(f"{db_path}")
				self.db = sqlite3.connect(db_path)
				self.db_cursor = self.db.cursor()
				listing = self.db_cursor.execute(f"SELECT * FROM user WHERE active=1 AND discordTag='{member}'")
				response = self.db_cursor.fetchall()
				try: 
					if "[]" in str(response):
						draw.text((175, 170), "Not logged in!", (255, 255, 255), font=font3)
					for row in response:
						draw.text((20, 230), "Status: {}".format(row[11]), (255, 255, 255), font=font) 
						draw.text((20, 250), "User Number: {}".format(row[0]), (255, 255, 255), font=font) 
					#await ctx.send(f"You probably didn't set your username on the website!")
				except Exception as e:
					return
				img.save('/home/ahigaaa/Laikabotfuck/cogs/profile/infoimg2.png') 
			with open('/home/ahigaaa/Laikabotfuck/cogs/profile/infoimg2.png', 'rb') as fp:
				await(await ctx.send(file=discord.File(fp, "penis.png"))).delete(delay=10)
			try:
				self.db_cursor.close()
			except Exception as e:
				return



def setup(bot):
    bot.add_cog(Activity(bot))

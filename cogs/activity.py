import discord
import psutil
import os
import asyncio
import urllib.request
import sqlite3
import re
import sqlite3

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from io import BytesIO
from urllib.request import urlopen

from discord.ext import commands
from collections import OrderedDict

from utils import default
from utils import permissions, http, default

from profanityfilter import ProfanityFilter

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
		DB_NAME = "db name"
		db_path = os.path.abspath("db path" + DB_NAME + ".db")
		print(f"{db_path}")
		sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS fucku (
											UserID character varying NOT NULL,
											XP integer DEFAULT 0,
											Level integer DEFAULT 0,
											Nword integer DEFAULT 0,
											Credit integer DEFAULT  0,
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
			self.db.close()
			print(f"done")


	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.bot:
			return

		DB_NAME = "db name"
		db_path = os.path.abspath("db path" + DB_NAME + ".db")
		self.db = sqlite3.connect(db_path)
		self.db_cursor = self.db.cursor()
		print(f"Connected")

		if message.author.bot:
			return

		if discord.utils.get(message.author.roles, name="Muted") != None:
			return
		if discord.utils.get(message.author.roles, name="Hardmute") != None:
			return

		author_id = str(message.author.id)
		guild_id = str(message.guild.id)


		negativeph = ['reddit', 'owo', 'bisexual', 'bi sexual', 'bi-sexual', 'ahigay', 'cock', 'femb', 'indica', 'christianity', 'tsuki', 'nibba', 'phobic', 'black p', 'systemsp', 'trans', 'homosexual', 'pog', 'tolerance', 'non binary', 'nonbinary', 'non-binary', 'genderfluid', 'gender fluid', 'gender-fluid', 'femmy', 'cum', 'boyp', 'b0ip', 'boy p', 'b0i p', 'boi p', 'boip', 'b0y p', 'b0y p', 'uwu', 'phobe']
		convoph = ['sup', 'hot', 'initiate', 'great', 'shit', 'shiet', 'raype', 'based', 'redpill', 'https', 'cute', 'loli', 'tomboy']
		channelid = message.channel.name

		pf = ProfanityFilter()

		if discord.utils.get(message.author.roles, name="Muted") != None:
			return
		if discord.utils.get(message.author.roles, name="Hardmute") != None:
			return

		self.db_cursor.execute(f"SELECT * FROM fucku WHERE UserID='{author_id}' AND GuildID='{guild_id}'")
		user = self.db_cursor.fetchone()
		if user:
			print("User found")
			sql = ("UPDATE fucku SET XP=? WHERE UserID=? AND GuildID=?")
			val = (int(user[1] + 1), int(message.author.id), int(message.guild.id))
			self.db_cursor.execute(sql, val)
			self.db.commit()

			if pf.is_profane(f"{message.content}") == True:
				sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
				val = (int(user[4] + 50), int(message.author.id), int(message.guild.id))
				self.db_cursor.execute(sql, val)
				self.db.commit()

			if re.compile('|'.join(convoph),re.IGNORECASE).search(message.content): 
				sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
				val = (int(user[4] + 10), int(message.author.id), int(message.guild.id))
				self.db_cursor.execute(sql, val)
				self.db.commit()
			if re.compile('|'.join(negativeph),re.IGNORECASE).search(message.content): 
				sql = ("UPDATE fucku SET Credit=? WHERE UserID=? AND GuildID=?")
				val = (int(user[4] - 50), int(message.author.id), int(message.guild.id))
				self.db_cursor.execute(sql, val)
				self.db.commit()

			if self.act_up_fuck(user):
				print(f"leveled up!")
				current_xp = int(user[1])
				current_lvl = int(user[2])
				if current_xp >= round((4 * (current_lvl ** 3)) / 5):
					sql = ("UPDATE fucku SET Level=? WHERE UserID=? AND GuildID=?")
					val = (int(user[2] + 1), int(message.author.id), int(message.guild.id))

					self.db_cursor.execute(sql, val)
					self.db.commit()

			if "nigger" in message.content or "niggers" in message.content or "NIGGER" in message.content or "NIGGERS" in message.content:
				s = str(message.content)
				sb = 'nigger'
				results = 0
				sub_len = len(sb)
				for i in range(len(s)):
					if s[i:i+sub_len] == sb:
						results += 1

				fuckk = int(results)

				sql = ("UPDATE fucku SET Nword=? WHERE UserID=? AND GuildID=?")
				val = (int(user[3] + fuckk), int(message.author.id), int(message.guild.id))
				self.db_cursor.execute(sql, val)
				self.db.commit()

			currentcredit = int(user[4])

			if currentcredit <= 40:
				sql = ("UPDATE fucku SET Credit=100 WHERE UserID=? AND GuildID=?")
				val = (int(message.author.id), int(message.guild.id))
				self.db_cursor.execute(sql, val)
				self.db.commit()

			if currentcredit >= 1000:
				sql = ("UPDATE fucku SET Credit=1000 WHERE UserID=? AND GuildID=?")
				val = (int(message.author.id), int(message.guild.id))
				self.db_cursor.execute(sql, val)
				self.db.commit()

			try:
				self.db_cursor.close()
				self.db.close()
			except Exception as e:
				return
		else:
			print(f"User not found proceeding...")
			sql = ("INSERT INTO fucku (UserID, XP, Level, Nword, Credit, GuildID) VALUES (?, ?, ?, ?, ?, ?)")
			val = (int(message.author.id), 1, 1, 0, 100, int(message.guild.id))
			self.db_cursor.execute(sql, val)
			print(f"inserted {val}")
			self.db.commit()
			print(f"committed")

		try:
			self.db_cursor.close()
			self.db.close()
		except Exception as e:
			return


	@commands.Cog.listener()
	async def on_member_update(self, before, after):
		DB_NAME = "db name"
		db_path = os.path.abspath("db path" + DB_NAME + ".db")
		self.db = sqlite3.connect(db_path)
		self.db_cursor = self.db.cursor()
		channel = self.bot.get_channel(660982562331820032)
		author_id = str(after.id)
		guild_id = str(after.guild.id)

		if len(before.roles) < len(after.roles):
			new_role = next(role for role in after.roles if role not in before.roles)
			if new_role.name in ('Server Booster'):
				await channel.send(f"❤️ {after.mention} thank you for the boost! You've been given 100 xp, and more credit!")
				self.db_cursor.execute(f"SELECT * FROM fucku WHERE UserID='{author_id}' AND GuildID='{guild_id}'")
				user = self.db_cursor.fetchone()
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
				self.db.close()



	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command()
	async def level(self, ctx, member: discord.Member = None):
		""" Check yours or other's activity level """
		DB_NAME = "db name"
		db_path = os.path.abspath("db path" + DB_NAME + ".db")
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
				await ctx.send(embed=embed)

		try:
			self.db_cursor.close()
			self.db.close()
		except Exception as e:
			return



	@commands.cooldown(1, 10, commands.BucketType.user)
	@commands.command()
	async def profile(self, ctx, member: discord.Member = None):
		""" Check yours or other's activity level """
		DB_NAME = "db name"
		db_path = os.path.abspath("db path" + DB_NAME + ".db")
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
			await ctx.send(embed=embed)
		else:
			currentcredit = int(user[4])
			currentxp = int(user[1])
			currentlvle = int(user[2])
			currentnigger = int(user[3])
			for row in user:
				url = str(member.avatar_url)
				bio = BytesIO(await http.get(url, res_method="read"))
				pfp = Image.open(bio)
				im = Image.open(urlopen('/profilee.png')) 
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
				if currentcredit >= 600:
					draw.text((10, 70), ":D", (255, 255, 255), font=font) 
				elif currentcredit <= 200:
					draw.text((10, 70), ":(", (255, 255, 255), font=font)
				else:
					draw.text((10, 70), ":/", (255, 255, 255), font=font)
				draw.text((10, 30), "{}".format(currentcredit), (255, 255, 255), font=font2) 
				draw.text((20, 110), "{}".format(member), (255, 255, 255), font=font) 
				draw.text((20, 130), "_________", (255, 255, 255), font=font) 
				draw.text((20, 170), "XP:  {}".format(currentxp), (255, 255, 255), font=font)
				draw.text((20, 190), "Level:  {}".format(currentlvle), (255, 255, 255), font=font)
				draw.text((20, 210), "Nwords: {}".format(currentnigger), (255, 255, 255), font=font)

				img.paste(pfpc, (171, 57))
				try:
					self.db_cursor.close()
					self.db.close()
				except Exception as e:
					print("wduwhduwhd")
	
				try:
					DB_NAME = "db name"
					db_path = os.path.abspath("db path" + DB_NAME + ".db")
					print(f"{db_path}")
					self.db = sqlite3.connect(db_path)
					self.db_cursor = self.db.cursor()
					listing = self.db_cursor.execute(f"SELECT * FROM user WHERE active=1 AND discordTag='{member}'")
					response = self.db_cursor.fetchall()
					try:
						for row in response:
							draw.text((20, 230), "Status: {}".format(row[11]), (255, 255, 255), font=font) 
							draw.text((20, 250), "User Number: {}".format(row[0]), (255, 255, 255), font=font) 
							self.db.close()
					except Exception as e:
						await ctx.send(f"You probably didn't set your username on the website!")
						self.db.close()
					self.db.close()
				except Exception as e:
					await ctx.send(f"You probably didn't set your username on the website!")
					self.db.close()
				img.save('/infoimg2.png') 
				with open('/infoimg2.png', 'rb') as fp:
					await ctx.send(file=discord.File(fp, "penis.png"))

				try:
					self.db_cursor.close()
					self.db.close()
				except Exception as e:
					return

		try:
			self.db_cursor.close()
			self.db.close()
		except Exception as e:
			return



def setup(bot):
    bot.add_cog(Activity(bot))

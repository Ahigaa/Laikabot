import discord
import psutil
import os
import json
import asyncio
import urllib.request

from discord.ext import commands
from collections import OrderedDict

client = discord.Client()

class Activity(commands.Cog):
	"""Activity"""
	def __init__(self, bot):
		self.bot = bot
		self.process = psutil.Process(os.getpid())

		self.bot.loop.create_task(self.save_activity())

		with open("path to activity.json file", 'r') as f:
			self.activity = json.load(f)

	async def save_activity(self):
		await self.bot.wait_until_ready()
		while not self.bot.is_closed():
			with open("path to activity.json file", 'w') as f:
				json.dump(self.activity, f, indent=4)

			await asyncio.sleep(5)

	def act_up_fuck(self, author_id):
		current_xp = self.activity[author_id]['xp']
		current_lvl = self.activity[author_id]['lvl']
		current_nword = self.activity[author_id]['nword']
		if current_xp >= round((4 * (current_lvl ** 3)) / 5):
			self.activity[author_id]['lvl'] += 1
			return True
		else:
			return False

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.bot:
			return

		author_id = str(message.author.id)
		if not author_id in self.activity:
			self.activity[author_id] = {}
			self.activity[author_id]['lvl'] = 1
			self.activity[author_id]['xp'] = 0
			self.activity[author_id]['nword'] = 0

		self.activity[author_id]['xp'] += 1
		if self.act_up_fuck(author_id):
			print(f"leveled up!\n Level: {self.activity[author_id]['lvl']}")

		if "nigger" in message.content or "nigga" in message.content:
			self.activity[author_id]['nword'] += 1


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
			embed.description = f"You're level {self.activity[member_id]['lvl']}\nCredit score: {self.activity[member_id]['xp']}\nN-words said: {self.activity[member_id]['nword']}"
			await ctx.send(embed=embed)


#This part was made by Ad for integrating laika with website..
clear_data = open('userdata.txt path goes here','w')
clear_data.close()

with open("path to activity.json file", 'r') as f:
    data = json.load(f)
    sorted_data = OrderedDict(sorted(data.items(), key = lambda x: (int(x[1]['lvl']), (int(x[1]['xp']), (int(x[1]['nword'])))), reverse=True))

@client.event
async def on_ready():
    for key,val in sorted_data.items():
        user = await client.fetch_user(key)
        usr_data = open('userdata.txt path goes here', 'a')
        usr_data.write(str(user) + '\n' + str(val['lvl']) + ' lvl' + '\n' + str(val['xp']) + ' xp' + '\n')
        usr_data.close()
    await client.close()

def setup(bot):
    bot.add_cog(Activity(bot))

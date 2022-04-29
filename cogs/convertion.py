import discord
import traceback
import psutil
import os
import aiohttp
import re

from discord.ext import commands
from discord.ext.commands import errors
from utils import default
from utils import lists, permissions, http, default


class Conversion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message):
        async def convertingshit():
            if "http" in message.content:
                return
            elif "lb" in message.content or "pound" in message.content:
                weight = re.findall(r"(\d+)lb", message.content)
                if "pound" in message.content:
                    weight = re.findall(r"(\d+) pound", message.content)
                a_string = "".join(weight)
                kilograms = int(a_string) / 2.2
                grams = int(kilograms) * 1000
                await message.channel.send(f'{round(kilograms, 1)}kgs\n{round(grams, 1)}g')
            elif "'" in message.content:
                height = message.content.split("'")
                if '"' in message.content:
                    height = ' '.join(height).replace('"','').split()
                feet = int(height[0])
                inches = int(height[1])
                meters = (12*feet + inches)*0.0254
                await message.channel.send(f'{round(feet, 1)} feet and {round(inches, 1)} inches =\n{round(meters, 2)} meters')
            elif "yard" in message.content:
                length = re.findall(r"(\d+) yard", message.content)
                a_string = "".join(length)
                meters = float(a_string)/1.094
                await message.channel.send(f'{a_string} yard(s) =\n{round(meters, 1)} meters')
            elif "inch" in message.content:
                length = re.findall(r"(\d+) inch", message.content)
                a_string = "".join(length)
                meters = float(a_string)*2.54
                await message.channel.send(f'{a_string} inches =\n{round(meters, 1)} centimeters')
            elif "f" in message.content:
                temp = re.findall(r"(\d+)f", message.content)
                a_string = "".join(temp)
                if "-" in message.content:
                    Celsius = (-int(a_string) - 32) * 5/9
                    await message.channel.send(f'Fahrenheit to Celsius: {round(Celsius, 1)}')
                else:
                    Celsius = (int(a_string) - 32) * 5/9
                    await message.channel.send(f'Fahrenheit to Celsius: {round(Celsius, 1)}')
            else:
                return



        def hasNumbers(inputString):
            return any(char.isdigit() for char in inputString)
        niggegegegr = hasNumbers(message.content)
        if niggegegegr:
            await convertingshit()



def setup(bot):
    bot.add_cog(Conversion(bot))

import random
import discord
import json
import secrets
import asyncio
import time
import urllib.request
import re
import requests
import os
import pandas as pd

from io import BytesIO
from discord.ext import commands
from asyncio import sleep
from utils import lists, permissions, http, default
from bs4 import BeautifulSoup

class Corona(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def corona(self, ctx, location : str ):
        """ <All>"""
            
        if len(location) == 2:
            location = location.upper()
        else:
            location = location.title()

        confirmed_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
        deaths_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
        recovered_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

        confirmed_df = pd.read_csv(confirmed_url, error_bad_lines=False)
        deaths_df = pd.read_csv(deaths_url, error_bad_lines=False)
        recovered_df = pd.read_csv(recovered_url, error_bad_lines=False)

        updated = list(confirmed_df)[-1]

        index = {'confirmed': confirmed_df[confirmed_df['Country/Region'].str.contains(location)].iloc[:,-1].sum(),
        'deaths': deaths_df[deaths_df['Country/Region'].str.contains(location)].iloc[:,-1].sum(),
        'recovered': recovered_df[recovered_df['Country/Region'].str.contains(location)].iloc[:,-1].sum(),

        'aConfirmed': confirmed_df.iloc[:,-1].sum(),
        'aDeaths': deaths_df.iloc[:,-1].sum(),
        'aRecovered': recovered_df.iloc[:,-1].sum(),

        }

        if any(confirmed_df['Country/Region'].str.contains(location)) or location == 'All':

            embed = discord.Embed(
                title=f'Coronavirus COVID-19 {location} Cases ',
                colour=discord.Colour.purple()
            )
            if location == 'All':
                embed.add_field(name='Confirmed', value=index['aConfirmed'])
                embed.add_field(name='Deaths', value=index['aDeaths'])
                embed.add_field(name='Recovered', value=index['aRecovered'])
            else:
                embed.add_field(name='Confirmed', value=index['confirmed'])
                embed.add_field(name='Deaths', value=index['deaths'])
                embed.add_field(name='Recovered', value=index['recovered'])

            embed.set_footer(text= f'Updated {updated}')

            await ctx.send(embed=embed)

        else:
            await ctx.send('There is no available data for this location')


def setup(bot):
    bot.add_cog(Corona(bot))

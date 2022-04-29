import discord
import re
import aiohttp
import base64

from io import BytesIO
from utils import default
from discord.ext import commands
from utils import permissions, default


class Discord_Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def avatar(self, ctx, *, user: discord.Member = None):
        """ Get the avatar of you or someone else """
        if user is None:
            user = ctx.author

        await ctx.send(f"Avatar to **{user.name}**\n{user.avatar_url_as(size=1024)}")

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def roles(self, ctx):
        """ Get all roles in current server """
        allroles = ""

        for num, role in enumerate(sorted(ctx.guild.roles, reverse=True), start=1):
            allroles += f"[{str(num).zfill(2)}] {role.id}\t{role.name}\t[ Users: {len(role.members)} ]\r\n"

        data = BytesIO(allroles.encode('utf-8'))
        await ctx.send(content=f"Roles in **{ctx.guild.name}**", file=discord.File(data, filename=f"{default.timetext('Roles')}"))

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def joindate(self, ctx, *, user: discord.Member = None):
        """ Check when a nigger joined the current server """
        if user is None:
            user = ctx.author

        embed = discord.Embed(colour=user.top_role.colour.value)
        embed.set_thumbnail(url=user.avatar_url)
        embed.description = f'**{user}** joined **{ctx.guild.name}**\n{default.date(user.joined_at)}'
        await ctx.send(embed=embed)

    @commands.group()
    @commands.guild_only()
    async def server(self, ctx):
        """ Check info about current server """
        if ctx.invoked_subcommand is None:
            findbots = sum(1 for member in ctx.guild.members if member.bot)

            embed = discord.Embed()
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
            embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
            embed.add_field(name="Members", value=ctx.guild.member_count, inline=True)
            embed.add_field(name="Bots", value=findbots, inline=True)
            embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
            embed.add_field(name="Region", value=ctx.guild.region, inline=True)
            embed.add_field(name="Created", value=default.date(ctx.guild.created_at), inline=True)
            await ctx.send(content=f"ℹ information about **{ctx.guild.name}**", embed=embed)

    @server.command(name="avatar", aliases=["icon"])
    @commands.guild_only()
    async def server_avatar(self, ctx):
        """ Get the current server icon """
        await ctx.send(f"Avatar of **{ctx.guild.name}**\n{ctx.guild.icon_url_as(size=1024)}")

    @commands.command()
    @commands.guild_only()
    async def mods(self, ctx):
        """ Check which mods are online on current guild """
        message = ""
        online, idle, dnd, offline = [], [], [], []

        for user in ctx.guild.members:
            if ctx.channel.permissions_for(user).kick_members or \
               ctx.channel.permissions_for(user).ban_members:
                if not user.bot and user.status is discord.Status.online:
                    online.append(f"**{user}**")
                if not user.bot and user.status is discord.Status.idle:
                    idle.append(f"**{user}**")
                if not user.bot and user.status is discord.Status.dnd:
                    dnd.append(f"**{user}**")
                if not user.bot and user.status is discord.Status.offline:
                    offline.append(f"**{user}**")

        if online:
            message += f"🟢 {', '.join(online)}\n"
        if idle:
            message += f"🟡 {', '.join(idle)}\n"
        if dnd:
            message += f"🔴 {', '.join(dnd)}\n"
        if offline:
            message += f"⚫ {', '.join(offline)}\n"

        await ctx.send(f"Mods in **{ctx.guild.name}**\n{message}")

    @commands.command(aliases=["whois"])
    @commands.guild_only()
    async def user(self, ctx, *, user: discord.Member = None):
        """ Get user information """
        if user is None:
            user = ctx.author

        embed = discord.Embed(colour=user.top_role.colour.value)
        embed.set_thumbnail(url=user.avatar_url)

        embed.add_field(name="Full name", value=user, inline=True)
        embed.add_field(name="Nickname", value=user.nick if hasattr(user, "nick") else "None", inline=True)
        embed.add_field(name="Account created", value=default.date(user.created_at), inline=True)
        embed.add_field(name="Joined this server", value=default.date(user.joined_at), inline=True)

        embed.add_field(
            name="Roles",
            value=', '.join([f"<@&{x.id}>" for x in user.roles if x is not ctx.guild.default_role]) if len(user.roles) > 1 else 'None',
            inline=False
        )

        await ctx.send(content=f"ℹ About **{user.id}**", embed=embed)

    @commands.command(aliases=['colour'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def color(self, ctx, color: str):
        """ fuck """

        async with ctx.channel.typing():
            if color == "random":
                color = "%06x" % random.randint(0, 0xFFFFFF)

            if color[:1] == "#":
                color = color[1:]

            if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', color):
                return await ctx.send("You're only allowed to enter HEX (0-9 & A-F)")
            cleaned = color.replace("#", "")
            myunendinghate = int(cleaned, 16)
            guild = ctx.guild
            fuckk = str(color)
            name = (f'#{fuckk}')
            try:
                try:
                    rolel = []
                    for role in ctx.author.roles:
                        if "#" in role.name:
                            rolel.append(role.id)
                    roler = discord.Object(id=rolel[0])
                    await ctx.author.remove_roles(roler)
                except:
                    pass
                try:
                    fuckk = f(color)
                    therole = discord.utils.get(ctx.guild.roles, name=f"{name}") 
                    await ctx.author.add_roles(therole)
                    embed = discord.Embed(colour=discord.Colour(myunendinghate))
                    embed.description = f"Role found! Success!"
                    await ctx.send(embed=embed)
                    await ctx.message.add_reaction(chr(0x2705))

                except Exception as e:
                    await guild.create_role(name=name, colour=discord.Colour(myunendinghate))
                    therole = discord.utils.get(ctx.guild.roles, name=f"{name}") 
                    await ctx.author.add_roles(therole)
                    embed = discord.Embed(colour=discord.Colour(myunendinghate))
                    embed.description = f"Role created! Success!"
                    await ctx.send(embed=embed)
                    await ctx.message.add_reaction(chr(0x2705))

            except Exception as e:
                    embed = discord.Embed(colour=discord.Colour(myunendinghate))
                    embed.description = f"Role created! Please type command again"
                    await ctx.send(embed=embed)
                    await ctx.send(e)



    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def deleteroles(self, ctx):
        """ fuck """
        guild = ctx.guild
        await ctx.message.add_reaction(chr(0x2705))
        for role in ctx.guild.roles:
            if len(role.members) == 0:
                if "#" in role.name:
                    try:
                        rolee = role.name
                        cleaned = rolee.replace("#", "")
                        myunendinghate = int(cleaned, 16)
                        embed = discord.Embed(colour=discord.Colour(myunendinghate))
                        embed.description = f"Automatically deleted the role **{role}** !"
                        await ctx.send(embed=embed)
                        await role.delete()
                    except Exception as e:
                        await ctx.send(e)
        await ctx.send("Finished!")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def unusedroles(self, ctx):
        """ fuck """
        guild = ctx.guild
        await ctx.message.add_reaction(chr(0x2705))
        for role in ctx.guild.roles:
            if len(role.members) == 0:
                if "#" in role.name:
                    try:
                        rolee = role.name
                        cleaned = rolee.replace("#", "")
                        myunendinghate = int(cleaned, 16)
                        embed = discord.Embed(colour=discord.Colour(myunendinghate))
                        embed.description = f"**{role}**"
                        await ctx.send(embed=embed)
                        #await role.delete()
                    except Exception as e:
                        await ctx.send(f'{e}')
        await ctx.send("Finished!")


def setup(bot):
    bot.add_cog(Discord_Info(bot))

import discord

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
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
        if user is None:
            user = ctx.author

        await ctx.send(f"Avatar to **{user.name}**\n{user.avatar_url_as(size=1024)}")

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def roles(self, ctx):
        """ Get all roles in current server """
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
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
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
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
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
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
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
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
        fuckmenigga = ctx.message.author
        if discord.utils.get(fuckmenigga.roles, name="Muted") != None:
            return
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


def setup(bot):
    bot.add_cog(Discord_Info(bot))

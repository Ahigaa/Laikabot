import discord
import re
import psutil
import datetime
import time
import json
import urllib.request

from discord.ext import commands
from discord.ext.commands import errors
from utils import permissions, default
from asyncio import sleep


# Source: https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/mod.py
class MemberID(commands.Converter):
    async def convert(self, ctx, argument):
        try:
            m = await commands.MemberConverter().convert(ctx, argument)
        except commands.BadArgument:
            try:
                return int(argument, base=10)
            except ValueError:
                raise commands.BadArgument(f"{argument} is not a valid member or member ID.") from None
        else:
            return m.id


class ActionReason(commands.Converter):
    async def convert(self, ctx, argument):
        ret = argument

        if len(ret) > 512:
            reason_max = 512 - len(ret) - len(argument)
            raise commands.BadArgument(f'reason is too long ({len(argument)}/{reason_max})')
        return ret


class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.process = psutil.Process()
        self.config = default.get("config.json")

    @commands.command(aliases=['newmembers'])
    @permissions.has_permissions(kick_members=True) 
    @commands.guild_only()
    async def newusers(self, ctx, *, count=5):
        """Tells you the newest members of the server.
        This is useful to check if any suspicious members have
        joined.
        The count parameter can only be up to 25.
        """
        count = max(min(count, 25), 5)

        if not ctx.guild.chunked:
            await self.bot.request_offline_members(ctx.guild)

        members = sorted(ctx.guild.members, key=lambda m: m.joined_at, reverse=True)[:count]

        e = discord.Embed(title='New Members', colour=discord.Colour.green())

        for member in members:
            body = f'Joined: {default.date(member.joined_at)}\nCreated: {default.date(member.created_at)}'
            e.add_field(name=f'{member} (ID: {member.id})', value=body, inline=False)

        await ctx.send(embed=e)

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        """ Kicks a user from the current server. """
        try:
            if reason == "-f":
                await member.kick(reason=default.responsible(ctx.author, reason))
                await ctx.send(default.actionmessage("kicked"))
            else:
                role_names = [role.name for role in member.roles]
                role_names = role_names[1:]
                for role in role_names:
                    fuck = discord.utils.get(ctx.guild.roles, name=f"{role}")
                    #await ctx.send(f"{fuck}")
                    await member.remove_roles(fuck)
                await ctx.send(default.actionmessage("kicked"))
        except Exception as e:
            await ctx.send(e)

    @commands.command(aliases=["nick"])
    @commands.guild_only()
    @permissions.has_permissions(manage_nicknames=True)
    async def nickname(self, ctx, member: discord.Member, *, name: str = None):
        """ Nicknames a user from the current server. """
        try:
            await member.edit(nick=name, reason=default.responsible(ctx.author, "Changed by command"))
            message = f"Changed **{member.name}'s** nickname to **{name}**"
            if name is None:
                message = f"Reset **{member.name}'s** nickname"
            await ctx.send(message)
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason="None"):
        """ Bans a user from the current server. """
        guildname = 'INITIATE'
        userthing = str(user.name)
        userreason = str(reason)
        await user.ban(reason=reason)
        embed = discord.Embed(color=0x1f7eb8)
        embed.description=(f'⌫ {userthing} banned, reason: {userreason}')
        await ctx.send(embed=embed)
        try:
        	#Please not that this was used with the old database
            self.connect()
            self.cursor.execute("INSERT INTO `discord_ban` (`username`, `userID`, `guild`, `reason`) VALUES ('" + str(user.name) + "', '" + str(user.id) + "', '" + str(guildname) + "', '" + str(reason) + "')")
            self.connection.commit()
            self.disconnect()
        except Exception as e:
            embed = discord.Embed(color=0x1f7eb8)
            embed.description=(f'Could not insert into table!\nUser might already be in table. Please use .unban <id> to unban.')
            await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.guild_only()
    @permissions.has_permissions(ban_members=True)
    async def fuckyou(self, ctx):
        if not permissions.can_upload(ctx):
            return await ctx.send("I cannot send images here ;>;")

        embed = discord.Embed(color=0xe1a6e1)
        embed.set_image(url="https://media.discordapp.net/attachments/588370099933806602/647274906609778703/shhhhh.png?width=1245&height=701")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)     
    @permissions.has_permissions(ban_members=True)
    async def hackban(self, ctx, user_id: int):
        """Bans a user outside of the server."""
        author = ctx.message.author
        guild = author.guild
        banmessage = "Banned by hackban"

        user = guild.get_member(user_id)
        if user is not None:
            return await ctx.invoke(self.ban, user=user)

        try:
        	#Please not that this was used with the old database
            self.connect()
            await self.bot.http.ban(user_id, guild.id, 0)
            self.cursor.execute("INSERT INTO `discord_ban` (`username`, `userID`, `guild`, `reason`) VALUES ('" + str(banmessage) + "', '" + str(user_id) + "', '" + str(guild) + "', '" + str(banmessage) + "')")
            self.connection.commit()
            embed = discord.Embed(color=0x1f7eb8,
                              title=f"**__Banned__**")
            embed.description=(f'⌫ Banned user: %s' % user_id)
            await ctx.send(embed=embed)
            self.disconnect()

        except discord.NotFound:
            embed = discord.Embed(color=7091547,
                              title=f"**__Error__**")
            embed.description='❌ Could not find user.\nInvalid user ID was provided.'
            await ctx.send(embed=embed)

        except discord.errors.Forbidden:
            embed = discord.Embed(color=7091547,
                              title=f"**__Error__**")
            embed.description='❌ Could not ban user. Not enough permissions.'
            await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(ban_members=True)
    async def massban(self, ctx, reason: ActionReason, *members: MemberID):
        """ Mass bans multiple members from the server. """

        try:
            for member_id in members:
                await ctx.guild.ban(discord.Object(id=member_id), reason=default.responsible(ctx.author, reason))
            await ctx.send(default.actionmessage("massbanned", mass=True))
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(ban_members=True)
    async def unban(self, ctx, member: MemberID, *, reason: str = None):
        """ Unbans a user from the current server. """
        try:
        	#Please not that this was used with the old database
            self.connect()
            self.query_userID()
            usridthing = str(member)
            if usridthing in self.existing_users:
                query = self.cursor.execute("DELETE FROM `discord_ban` WHERE `userID`='" + str(member) + "'")
                self.connection.commit()
                self.disconnect()
            else:
                return()
            await ctx.guild.unban(discord.Object(id=member), reason=default.responsible(ctx.author, reason))
            await ctx.send(default.actionmessage("unbanned"))
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason: str = None):
        """ Mutes a user from the current server. """
        message = []
        for role in ctx.guild.roles:
            if role.name == "Hardmute":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except IndexError:
            return await ctx.send("Are you sure you've made a role called **Hardmute**? Remember that it's case sensetive too...")

        try:
            await member.add_roles(therole, reason=default.responsible(ctx.author, reason))
            await ctx.send(default.actionmessage("muted"))
        except Exception as e:
            await ctx.send(e)

    @commands.Cog.listener()
    async def on_message(self, message):
        fuckmenigga = message.author
        #role = discord.utils.find(lambda r: r.name == 'Muted', user.guild.roles)
        if discord.utils.get(fuckmenigga.roles, name="Hardmute") != None:
            await message.delete();
        else:
            await message.delete();

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member, *, reason: str = None):
        """ Unmutes a user from the current server. """
        fuckmenigga = ctx.message.author
        message = []
        for role in ctx.guild.roles:
            if role.name == "Hardmute":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except IndexError:
            return await ctx.send("Are you sure you've made a role called **Hardmute**? Remember that it's case sensetive too...")

        try:
            await member.remove_roles(therole, reason=default.responsible(ctx.author, reason))
            await ctx.send(default.actionmessage("unmuted"))
        except Exception as e:
            await ctx.send(e)

    @commands.group()
    @commands.guild_only()
    @permissions.has_permissions(ban_members=True)
    async def find(self, ctx):
        """ Finds a user within your search term """
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))

    @find.command(name="playing")
    async def find_playing(self, ctx, *, search: str):
        loop = [f"{i} | {i.activity.name} ({i.id})" for i in ctx.guild.members if i.activity if (search.lower() in i.activity.name.lower()) and (not i.bot)]
        await default.prettyResults(
            ctx, "playing", f"Found **{len(loop)}** on your search for **{search}**", loop
        )

    @find.command(name="username", aliases=["name"])
    async def find_name(self, ctx, *, search: str):
        loop = [f"{i} ({i.id})" for i in ctx.guild.members if search.lower() in i.name.lower() and not i.bot]
        await default.prettyResults(
            ctx, "name", f"Found **{len(loop)}** on your search for **{search}**", loop
        )

    @find.command(name="nickname", aliases=["nick"])
    async def find_nickname(self, ctx, *, search: str):
        loop = [f"{i.nick} | {i} ({i.id})" for i in ctx.guild.members if i.nick if (search.lower() in i.nick.lower()) and not i.bot]
        await default.prettyResults(
            ctx, "name", f"Found **{len(loop)}** on your search for **{search}**", loop
        )

    @find.command(name="discriminator", aliases=["discrim"])
    async def find_discriminator(self, ctx, *, search: str):
        if not len(search) != 4 or not re.compile("^[0-9]*$").search(search):
            return await ctx.send("You must provide exactly 4 digits")

        loop = [f"{i} ({i.id})" for i in ctx.guild.members if search == i.discriminator]
        await default.prettyResults(
            ctx, "discriminator", f"Found **{len(loop)}** on your search for **{search}**", loop
        )

    @commands.group()
    @commands.guild_only()
    @permissions.has_permissions(ban_members=True)
    async def prurge(self, ctx, user: discord.Member, *, matches: str = None, limit: int = 100):
        """Purge all messages, optionally from ``user``
        or contains ``matches``."""
        def check_msg(msg):
            if msg.id == ctx.message.id:
                return True
            if user is not None:
                if msg.author.id != user.id:
                    return False
            if matches is not None:
                if matches not in msg.content:
                    return False
            return True
        deleted = await ctx.channel.purge(limit=limit, check=check_msg)
        await ctx.send(f'🚮 Successfully removed {deleted} message{"" if deleted == 1 else "s"}.')

    @commands.group()
    @commands.guild_only()
    @permissions.has_permissions(ban_members=True)
    async def prune(self, ctx):
        """ Removes messages from the current server. """
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))

    async def do_removal(self, ctx, limit, predicate, *, before=None, after=None, message=True):
        if limit > 2000:
            return await ctx.send(f'Too many messages to search given ({limit}/2000)')

        if before is None:
            before = ctx.message
        else:
            before = discord.Object(id=before)

        if after is not None:
            after = discord.Object(id=after)

        try:
            deleted = await ctx.channel.purge(limit=limit, before=before, after=after, check=predicate)
        except discord.Forbidden:
            return await ctx.send('I do not have permissions to delete messages.')
        except discord.HTTPException as e:
            return await ctx.send(f'Error: {e} (try a smaller search?)')

        deleted = len(deleted)
        if message is True:
            await ctx.send(f'🚮 Successfully removed {deleted} message{"" if deleted == 1 else "s"}.')

    @prune.command()
    async def embeds(self, ctx, search=100):
        """Removes messages that have embeds in them."""
        await self.do_removal(ctx, search, lambda e: len(e.embeds))

    @prune.command()
    async def files(self, ctx, search=100):
        """Removes messages that have attachments in them."""
        await self.do_removal(ctx, search, lambda e: len(e.attachments))

    @prune.command()
    async def mentions(self, ctx, search=100):
        """Removes messages that have mentions in them."""
        await self.do_removal(ctx, search, lambda e: len(e.mentions) or len(e.role_mentions))

    @prune.command()
    async def images(self, ctx, search=100):
        """Removes messages that have embeds or attachments."""
        await self.do_removal(ctx, search, lambda e: len(e.embeds) or len(e.attachments))

    @prune.command(name='all')
    async def _remove_all(self, ctx, search=100):
        """Removes all messages."""
        await self.do_removal(ctx, search, lambda e: True)

    @prune.command()
    async def user(self, ctx, member: discord.Member, search=100):
        """Removes all messages by the member."""
        await self.do_removal(ctx, search, lambda e: e.author == member)

    @prune.command()
    async def contains(self, ctx, *, substr: str):
        """Removes all messages containing a substring.
        The substring must be at least 3 characters long.
        """
        if len(substr) < 3:
            await ctx.send('The substring length must be at least 3 characters.')
        else:
            await self.do_removal(ctx, 100, lambda e: substr in e.content)

    @prune.command(name='bots')
    async def _bots(self, ctx, search=100, prefix=None):
        """Removes a bot user's messages and messages with their optional prefix."""

        getprefix = prefix if prefix else self.config.prefix

        def predicate(m):
            return (m.webhook_id is None and m.author.bot) or m.content.startswith(tuple(getprefix))

        await self.do_removal(ctx, search, predicate)

    @prune.command(name='users')
    async def _users(self, ctx, prefix=None, search=100):
        """Removes only user messages. """

        def predicate(m):
            return m.author.bot is False

        await self.do_removal(ctx, search, predicate)

    @prune.command(name='emojis')
    async def _emojis(self, ctx, search=100):
        """Removes all messages containing custom emoji."""
        custom_emoji = re.compile(r'<(?:a)?:(\w+):(\d+)>')

        def predicate(m):
            return custom_emoji.search(m.content)

        await self.do_removal(ctx, search, predicate)

    @prune.command(name='reactions')
    async def _reactions(self, ctx, search=100):
        """Removes all reactions from messages that have them."""

        if search > 2000:
            return await ctx.send(f'Too many messages to search for ({search}/2000)')

        total_reactions = 0
        async for message in ctx.history(limit=search, before=ctx.message):
            if len(message.reactions):
                total_reactions += sum(r.count for r in message.reactions)
                await message.clear_reactions()

        await ctx.send(f'Successfully removed {total_reactions} reactions.')


    @commands.group()
    @commands.guild_only()
    async def listservers(self, ctx):
        """ Lists servers and doxxes uir shiT. """
        servers = list(self.bot.guilds)
        await ctx.send("Count: " + str(len(self.bot.guilds)) + " servers:")
        async for guild in self.bot.fetch_guilds(limit=150):
            await ctx.send(guild.name)
            await ctx.send(guild.id)

    @commands.group()
    @commands.guild_only()
    async def listschannels(self, ctx):
        """ Lists servers and doxxes uir shiT. """
        servers = list(self.bot.guilds)
        await ctx.send("Count: " + str(len(self.bot.guilds)) + " servers:")
        async for guild in self.bot.fetch_guilds(limit=150):
            await ctx.send(guild.name)
            await ctx.send(guild.id)


    @commands.group()
    @commands.guild_only()
    @permissions.has_permissions(ban_members=True)
    async def purge(self, ctx, amount=100):
        """ Purges messages from the current server. """
        await ctx.send('🗑️ Purging....')
        await sleep(1)
        await ctx.channel.purge(limit=amount + 2)
def setup(bot):
    bot.add_cog(Moderator(bot))

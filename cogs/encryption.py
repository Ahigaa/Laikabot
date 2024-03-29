import base64
import binascii
import codecs

from discord.ext import commands


class Encryption(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.group()
    async def encode(self, ctx):
        """ All encode methods """
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))

    @commands.group()
    async def decode(self, ctx):
        """ All decode methods """
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))

    async def encryptout(self, ctx, convert, input):
        if len(input) > 1900:
            # TODO: Upload if too long and accept text files
            return await ctx.send(f"The result was too long, sorry **{ctx.author.name}**")

        try:
            await ctx.send(f"📑 **{convert}**```fix\n{input.decode('UTF-8')}```")
        except AttributeError:
            await ctx.send(f"📑 **{convert}**```fix\n{input}```")

    @encode.command(name="base32", aliases=["b32"])
    async def encode_base32(self, ctx, *, input: commands.clean_content):
        """ Encode base32 """
        await self.encryptout(
            ctx, "Text -> base32", base64.b32encode(input.encode('UTF-8'))
        )

    @decode.command(name="base32", aliases=["b32"])
    async def decode_base32(self, ctx, *, input: str):
        """ Decode base32 """
        try:
            await self.encryptout(ctx, "base32 -> Text", base64.b32decode(input.encode('UTF-8')))
        except Exception:
            await ctx.send("Invalid base32...")

    @encode.command(name="base64", aliases=["b64"])
    async def encode_base64(self, ctx, *, input: commands.clean_content):
        """ Encode base64 """
        await self.encryptout(
            ctx, "Text -> base64", base64.urlsafe_b64encode(input.encode('UTF-8'))
        )

    @decode.command(name="base64", aliases=["b64"])
    async def decode_base64(self, ctx, *, input: str):
        """ Decode base64 """
        try:
            await self.encryptout(ctx, "base64 -> Text", base64.urlsafe_b64decode(input.encode('UTF-8')))
        except Exception:
            await ctx.send("Invalid base64...")

    @encode.command(name="rot13", aliases=["r13"])
    async def encode_rot13(self, ctx, *, input: commands.clean_content):
        """ Encode rot13 """
        await self.encryptout(
            ctx, "Text -> rot13", codecs.decode(input, 'rot_13')
        )

    @decode.command(name="rot13", aliases=["r13"])
    async def decode_rot13(self, ctx, *, input: str):
        """ Decode rot13 """
        try:
            await self.encryptout(ctx, "rot13 -> Text", codecs.decode(input, 'rot_13'))
        except Exception:
            await ctx.send("Invalid rot13...")

    @encode.command(name="hex")
    async def encode_hex(self, ctx, *, input: commands.clean_content):
        """ Encode hex """
        await self.encryptout(
            ctx, "Text -> hex",
            binascii.hexlify(input.encode('UTF-8'))
        )

    @decode.command(name="hex")
    async def decode_hex(self, ctx, *, input: str):
        """ Decode hex """
        try:
            await self.encryptout(ctx, "hex -> Text", binascii.unhexlify(input.encode('UTF-8')))
        except Exception:
            await ctx.send("Invalid hex...")

    @encode.command(name="base85", aliases=["b85"])
    async def encode_base85(self, ctx, *, input: commands.clean_content):
        """ Encode base85 """
        await self.encryptout(
            ctx, "Text -> base85",
            base64.b85encode(input.encode('UTF-8'))
        )

    @decode.command(name="base85", aliases=["b85"])
    async def decode_base85(self, ctx, *, input: str):
        """ Decode base85 """
        try:
            await self.encryptout(ctx, "base85 -> Text", base64.b85decode(input.encode('UTF-8')))
        except Exception:
            await ctx.send("Invalid base85...")

    @encode.command(name="ascii85", aliases=["a85"])
    async def encode_ascii85(self, ctx, *, input: commands.clean_content):
        """ Encode ASCII85 """
        await self.encryptout(
            ctx, "Text -> ASCII85",
            base64.a85encode(input.encode('UTF-8'))
        )

    @decode.command(name="ascii85", aliases=["a85"])
    async def decode_ascii85(self, ctx, *, input: str):
        """ Decode ASCII85 """
        try:
            await self.encryptout(ctx, "ASCII85 -> Text", base64.a85decode(input.encode('UTF-8')))
        except Exception:
            await ctx.send("Invalid ASCII85...")


def setup(bot):
    bot.add_cog(Encryption(bot))

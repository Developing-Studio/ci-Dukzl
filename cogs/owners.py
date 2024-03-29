from discord.ext import commands

from . import load_extensions, unload_extensions, reload_extensions


class Owners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="리로드", aliases=["reload"])
    @commands.is_owner()
    async def reload_cogs(self, ctx):
        reload_extensions(self.bot)
        await ctx.send("Reload Complete")

    @commands.command(name="언로드", aliases=["unload"])
    @commands.is_owner()
    async def unload_cogs(self, ctx):
        await ctx.send("ㄴ")

    @commands.command(name="로드", aliases=["load"])
    @commands.is_owner()
    async def load_cogs(self, ctx):
        load_extensions(self.bot)
        await ctx.send("Load Complete")


def setup(bot):
    bot.add_cog(Owners(bot))

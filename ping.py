from discord import Embed
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
    
    from discord import Embed
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["pong", "latency"])
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! 🏓 {latency}ms")

async def setup(bot):
    await bot.add_cog(Ping(bot))

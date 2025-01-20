from discord import Embed
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, command_name=None):
        if command_name is None:
            embed = Embed(
                title="Help Command",
                description="List of commands:\n- `ping`\n- `help`",
                color=0x1abc9c
            )
            embed.set_footer(text="Type `!help <command>` for more details.")
        elif command_name == "ping":
            embed = Embed(
                title="Help: ping",
                description="`!ping`\n-Shows the bot's latency.",
                color=0x1abc9c
            )
        elif command_name == "help":
            embed = Embed(
                title="Help: help",
                description="`!help`\n-Displays a list of commands.\n`!help <command>` provides specific details.",
                color=0x1abc9c
            )
        else:
            embed = Embed(
                title="Error",
                description="Command not found. Use `!help` for a list of commands.",
                color=0xe74c3c
            )
        await ctx.send(embed=embed)
    
async def setup(bot):
    await bot.add_cog(help(bot))

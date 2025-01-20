from discord import Embed
from discord.ext import commands
import discord

class avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def av(self, ctx, member: discord.Member = None):
        try:
            member = member or ctx.author
            if member.avatar:
                avatar_url = member.avatar.url
            else:
                avatar_url = member.default_avatar.url

            embed = discord.Embed(
                title=f"{member.name}'s Avatar",
                description=f"[Link to avatar]({avatar_url})",
                color=0x3498db
            )
            embed.set_image(url=avatar_url)
            await ctx.send(embed=embed)

        except Exception as e:
            print(f"Error in avatar command: {e}")

async def setup(bot):
    await bot.add_cog(avatar(bot))

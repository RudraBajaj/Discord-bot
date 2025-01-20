import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents , help_command=None)

async def load_cogs(): 
    cog_folder = os.path.join("C:\\Rudra\\Coding\\projects\\discord bots\\Final bot\\cogs")
    if not os.path.exists(cog_folder):
        print(f"Error: The '{cog_folder}' folder does not exist.")
        return

    for filename in os.listdir(cog_folder):
        if filename.endswith(".py"):
            
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded cog: {filename}")
            except Exception as e:
                print(f"Failed to load cog {filename}: {e}")

@bot.event
async def on_ready():
    print(f"Bot is online! Logged in as {bot.user} ({bot.user.id})")
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name="Madwofl!")
    )

async def main():
    async with bot:
        await load_cogs() 
        token = os.getenv('DISCORD_TOKEN')
        if not token:
            print("ERROR: DISCORD_TOKEN not found in the .env file.")
            return
        await bot.start(token) 

if __name__ == "__main__":
    asyncio.run(main())
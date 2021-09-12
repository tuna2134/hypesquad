from discord.ext import commands
import discord
import os

token=os.getenv("token")

bot = commands.Bot(command_prefix="hs?", help_command=None,intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("起動しました")
  
bot.run(token)

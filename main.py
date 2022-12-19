from discord.ext import commands 
import discord
from server import start
from dotenv import load_dotenv
import os

load_dotenv()


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '-', intents = intents)

@bot.event 
async def on_ready():
  print('ready')

@bot.command()
async def hi(ctx):
  await ctx.send("Hello!!")

# Discord & Github Name: frikinomad
@bot.command()
async def frikinomad(ctx):
  await ctx.send("Hello, I am frikinomad, I like to code and travel")


start()

print(os.environ.get('TOKEN'))
token = os.environ.get('TOKEN')  #token will be provided with the every claimed issue
bot.run(token)

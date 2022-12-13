from discord.ext import commands 
import discord
from server import start

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '-', intents = intents)

@bot.event 
async def on_ready():
  print('ready')
  
@bot.command()
async def hi(ctx):
  await ctx.send("Hello!!")

start()

token = ""  #token will be provided with the every claimed issue
bot.run(token)

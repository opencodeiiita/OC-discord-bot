from discord.ext import commands
import discord
from server import start

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)


@bot.event
async def on_ready():
    print('ready')


@bot.command()
async def hi(ctx):
    await ctx.send("Hello!!")

# Discord: Gamma Microwave#4389 GitHub:GammaMicrowave


@bot.command()
async def GammaMicrowave(ctx):
    embed = discord.Embed()
    embed.set_image(
        url="https://media.giphy.com/media/EtB1yylKGGAUg/giphy.gif")

    await ctx.send(embed=embed)


start()

token = ""
bot.run(token)

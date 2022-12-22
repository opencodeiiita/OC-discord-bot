from discord.ext import commands
import discord
from server import start
import json
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

separators = [":", "-", "="]


@bot.event
async def on_ready():
  print('ready')

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('Enter a Valid command, Ciao')


@bot.command()
async def hi(ctx):
    await ctx.send("Hello!!")


@bot.command()
async def create(ctx, *args):
    command = args[0]
    tempList = list(args)
    tempList.pop(0)
    message = " ".join(tempList)
    dict = {command: message}
    with open('./data.json', 'r+') as file:
        tempData = json.load(file)
    tempData.update(dict)
    with open('./data.json', 'w') as file:
        json.dump(tempData, file)


@bot.command()
async def tag(ctx, args):
    with open('./data.json', 'r') as file:
        data = json.load(file)
    await ctx.send(data[args])

 # Discord: Gamma Microwave#4389 GitHub:GammaMicrowave


@bot.command()
async def GammaMicrowave(ctx):
    embed = discord.Embed()
    embed.set_image(
        url="https://media.giphy.com/media/EtB1yylKGGAUg/giphy.gif")

    await ctx.send(embed=embed)

# Discord & Github Name: frikinomad
@bot.command()
async def frikinomad(ctx):
  await ctx.send("Hello, I am frikinomad, I like to code and travel")

#Github: VBajaj113    Discord: im_nothing#4509
@bot.command()
async def VBajaj113(ctx):
    await ctx.send("You should have tagged instead of issuing a bot command if you wanted to talk to me xD!")

#Github: SanyamAgrawal07    Discord: Buzzinga#2392
@bot.command()
async def SanyamAgrawal07(ctx):
    await ctx.send("https://tinyurl.com/jn4x5awv")

#Github : akshatsgh    Discord: strange#0227
@bot.command()
async def akshatsgh(ctx):
    pic_link = "https://source.unsplash.com/random/300%C3%97300/?coder"
    await ctx.send(pic_link)

#Github : RibhavBansal    Discord: ThunderBeast#1696
@bot.command()
async def RibhavBansal(ctx):
  await ctx.send("Hey, I am Ribhav, I like to develop my skills")

# Discord ID: MistyRavager#2412 Github ID: MistyRavager
@bot.command()
async def MistyRavager(ctx):
    separators = [":", "-", "="]
    discordIDs = []
    with open("main.py", "r") as f:
        lines = f.readlines()
        comments = [i.strip() for i in lines if i.strip()
                    != '' and i.strip()[0] == "#"]
        for comment in comments:
            sentence = comment.split()
            for word in sentence:
                if word.find("#") != -1:
                    index = 0
                    while (index < len(separators) and word.find(separators[index]) == -1):
                        index += 1
                    if index == len(separators):
                        if word[0] == "#":
                            continue
                        discordIDs.append(word)
                    else:
                        discordIDs.append(word.split(separators[index])[-1])

    res = ""
    for i in discordIDs:
        res += i+" "

    await ctx.send("the following people have made a personal command:")
    await ctx.send(res)

start()
# token will be provided with the every claimed issue
bot.run(os.getenv("TOKEN")) #Now add the token in a .env file named TOKEN and it will run automatically

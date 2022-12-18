from discord.ext import commands 
import discord
from server import start

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '-', intents = intents)

separators= [":","-","="]

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



#Github: VBajaj113    Discord: im_nothing#4509
@bot.command()
async def VBajaj113(ctx):
  await ctx.send("You should have tagged instead of issuing a bot command if you wanted to talk to me xD!")

# Discord ID: MistyRavager#2412 Github ID: MistyRavager  
@bot.command()
async def MistyRavager(ctx):
  separators= [":","-","="]
  discordIDs = []
  with open("main.py","r") as f:
      lines = f.readlines()
      comments = [i.strip() for i in lines if i.strip()!= '' and i.strip()[0]=="#"]
      for comment in comments:
          sentence = comment.split()
          for word in sentence:
              if word.find("#") != -1:
                  index = 0
                  while (index < len(separators) and word.find(separators[index]) == -1 ):
                      index+=1    
                  if index == len(separators):
                      if word[0]=="#":
                          continue
                      discordIDs.append(word)
                  else :
                      discordIDs.append(word.split(separators[index])[-1])
  
  res = ""
  for i in discordIDs: 
    res += i+" "
  
  await ctx.send("the following people have made a personal command:")
  await ctx.send(res)
  
start()

token = ""  #token will be provided with the every claimed issue
bot.run(token)

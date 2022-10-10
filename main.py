import nextcord
from nextcord.ext import commands
import random
import pyjokes
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import requests # request img from web
import shutil # save img locally
from urllib import request
import BotCMD
import os
from discord_webhook import DiscordWebhook
from datetime import datetime


actual_items = []

log = DiscordWebhook(url='https://discord.com/api/webhooks/1027329669755846746/f3h4v93uZYfd8Q95VMUf6btHEEFG2teIExKcqcj09kDO4SAUTj07pI6s49cTgbsdzlkh')


TOKEN = os.environ["DISCORD_TOKEN"]
q_answer = ["No", "Yes", "Probably Not", "Probably Yes", "Maybe", "Definitely", "Impossible"]
boop_counter = 0

chatbot = ChatBot('Minda')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    'chatterbot.corpus.english'
)

intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='m!', intents=nextcord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print('Ready!')
    now = datetime.now()
    log.content=f'Bot launched :: [{now}]'
    re = log.execute()

@bot.command()
async def help(ctx):
    now = datetime.now()
    log.content=f'Help :: [{now}]'
    re = log.execute()
    embed = nextcord.Embed(title="Commands: (list will change)", description="1.0 version of the bot.", colour=0x5865F2)
    embed.add_field(name='boop', value='boop el Minda', inline=False)
    embed.add_field(name='cheese', value='displays an edit of your pfp with minda', inline=False)
    embed.add_field(name='joke', value='random joke', inline=False)
    embed.add_field(name='poll', value='want to know if people disagree/agree with you? ues this command', inline=False)
    embed.add_field(name='question', value='ask a yes or no question and minda will answer', inline=False)
    embed.add_field(name='random_image', value='generated a random image and send it', inline=False)
    embed.add_field(name='rps (rock paper scissors)', value='example: m!rps rock', inline=False)
    embed.add_field(name='talk', value='talk to minda, although it could be janky she still learns the more you talk.', inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def question(ctx):
    await ctx.send(random.choice(q_answer))
    now = datetime.now()
    log.content=f'Question :: [{now}]'
    re = log.execute()

@bot.command()
async def joke(ctx):
    await ctx.send(pyjokes.get_joke())
    now = datetime.now()
    log.content=f'Question :: [{now}]'
    re = log.execute()

@bot.command()
async def talk(ctx, *, input):
    now = datetime.now()
    log.content=f'Question :: [{now}]'
    re = log.execute()
    response = chatbot.get_response(input)
    await ctx.send(response)

@bot.command()
async def cheese(ctx, member : nextcord.Member = None):
    if member == None:
        member = ctx.author
    imgname = 'avatar.png'
    member_avatar = member.avatar.url
    imgd = requests.get(member_avatar, stream = True)
    if imgd.status_code == 200:
        with open(imgname,'wb') as f:
            shutil.copyfileobj(imgd.raw, f)
        print('Image sucessfully Downloaded: ',imgname)
    BotCMD.idiotcmd()
    await ctx.send(file=nextcord.File('cheeseResult.png'))
    now = datetime.now()
    log.content=f'Cheese :: [{now}]'
    re = log.execute()

@bot.command()
async def randomimage(ctx, ResX = None, ResY = None):
    if ResX == None:
        ResX = 1024
    if ResY == None:
        ResY == 1024
    imgname='random.png'
    request.urlretrieve('https://picsum.photos/200', 'random.png')
    await ctx.send(file=nextcord.File('random.png'))
    now = datetime.now()
    log.content=f'RandomImage :: [{now}]'
    re = log.execute()

@bot.command()
async def poll(ctx, *, question):
    embed = nextcord.Embed(title=question, color=0xd10a07)
    embed.description = f'Vote and share your opinion about "{question}"'
    embed.add_field(name='How to use polls?', value='Vote using the reactions that should appear about now...', inline=False)
    msg_embed = await ctx.send(embed=embed)
    await msg_embed.add_reaction('👍')
    await msg_embed.add_reaction('👎')
    now = datetime.now()
    log.content=f'Poll :: [{now}]'
    re = log.execute()
    

@bot.command()
async def rps(ctx, uchoice):
    choices = ['rock', 'paper', 'scissors']
    self_choice = random.choice(choices)
    if self_choice == uchoice:
        await ctx.send(f'i chose {self_choice} and you chose {uchoice}. its a tie')
    if self_choice == 'rock':
        if uchoice == 'paper':
            await ctx.send(f'i chose {self_choice} and you chose {uchoice}. you win')
        elif uchoice == 'scissors':
            await ctx.send(f'i chose {self_choice} and you chose {uchoice}. i win')
    if self_choice == 'paper':
        if uchoice == 'rock':
            await ctx.send(f'i chose {self_choice} and you chose {uchoice}. i win')
        elif uchoice == 'scissors':
            await ctx.send(f'i chose {self_choice} and you chose {uchoice}. you win')
    if self_choice == 'scissors':
        if uchoice == 'paper':
            await ctx.send(f'i chose {self_choice} and you chose {uchoice}. i win')
        elif uchoice == 'rock':
            await ctx.send(f'i chose {self_choice} and you chose {uchoice}. you win')
    now = datetime.now()
    log.content=f'RPS :: [{now}]'
    re = log.execute()

@bot.command()
async def boop(ctx):
    boop = ['hey!', 'stop that', 'no!', 'hey dont do that','STOP', 'dont boop me!!!', 'nooo!', 'STOP. BOOPING. ME!']
    c = random.choice(boop)
    await ctx.send(c)
    now = datetime.now()
    log.content=f'Boop :: [{now}]'
    re = log.execute()

bot.run(TOKEN)
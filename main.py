import discord
import json
import asyncio
import os, dotenv

from datetime import datetime
from discord.ext import commands


bot = commands.Bot(command_prefix="!")

dotenv.load_dotenv('.env')
TOKEN = os.environ.get("DISCORD_BOT_SECRET")

config_file = open("config.json")
config = json.load(config_file)
bot.remove_command("help")


@bot.event
async def on_ready():
    print(f"| -----                       Logged in as:                       ----- |")
    await bot.change_presence(activity=discord.Game(name=f"Listening to user Commands"))
    print(f"| -----        {bot.user.name} BOT: With Id {bot.user.id}         ----- |\n")


# Customs command

@bot.command(pass_context = True)
async def help(ctx):

    print("!help Command Is Running!")
    embed = discord.Embed(
        title = "Working on Help command list", 
        color=0x8150bc,
        timestamp = datetime.utcnow(),
        description = "Trivia BOT for quizzes!"
    )

    embed.add_field(name = "1. Quiz", value = config['quiz'], inline = False)
    embed.add_field(name = "2. Leaderboard", value = config['Leaderboard'], inline = False)
    
    # embed.set_footer(text = 'Bot Made By #66daysofdata Team')
    embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name))
    await ctx.send(embed = embed)

@bot.command()
async def poll(ctx, question, option1=None, option2=None):
    if option1 is not None and option2 is not None:
        # await ctx.channel.purge(limit=1)
        print('printing')

        message = await ctx.send(f"```New Question: \n{question}\n A. {option1}\n B. {option2}```\n")
        
        await message.add_reaction('🅰')
        await message.add_reaction('🅱')
        await message.add_reaction('C')
        await message.add_reaction('D')

        await message.add_reaction('🤷🏼‍♂️')


bot.run(TOKEN)
import discord
import json
import asyncio
import os, dotenv

from datetime import datetime
from discord.ext import commands

from prettytable import PrettyTable
from prettytable import from_db_cursor

bot = commands.Bot(command_prefix="++")

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
    
    embed.set_footer(text = 'Bot Made By Saurabh')
    embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name))
    await ctx.send(embed = embed)

bot.run(TOKEN)
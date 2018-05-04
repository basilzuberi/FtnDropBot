import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from random import randint
import os

bot = commands.Bot(command_prefix='^', description='Type ^drop to get a random drop location!')

@bot.event
async def on_ready():
    print("DropBot Ready to go!")

    await bot.change_presence(game=discord.Game(name='^drop'))

@bot.event
async def on_message(msg):
    DROPS = ["Risky Reels","Race Track","Chair Town","Soccer City","Trailer Park","Motel","Broken Houses near Motel","Old Factory (Salty)","New Factory (Flush)",+/
             "Cargo Yard","Anarchy Acers","Junk Junction","Haunted Hills","Pleasant Park","Loot Lake","Wailing Woods","Tomato Town","Lonely Lodge","Snobby Shores",+/
             "Tilted Towers","Dusty Divot","Retail Row","Greasy Grove","Shifty Shafts", "Salty Springs", "Flush Factory","Fatal Fields","Moisty Mire","Prison"]
    if msg.content.upper().startswith("^DROP"):
        
        DropLocation = randint(0,len(DROPS))
        
        Location = DROPS[DropLocation]
        
        userID = msg.author.id


        
        await bot.send_message(msg.channel, "<@{}> I believe your drop location should be {}!".format(userID,DROPS[DropLocation]))


bot.run(os.environ['BOT_TOKEN'])

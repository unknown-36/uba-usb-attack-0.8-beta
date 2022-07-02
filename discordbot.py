import discord
from discord.ext import commands

with open('info.txt') as a:
    info1 = a.read()

with open('local.txt') as b:
    info2 = b.read()

bot = commands.Bot(command_prefix='.')

@bot.command()
async def info(ctx):
    await ctx.reply(info1)

@bot.command()
async def linfo(ctx):
    await ctx.reply(info2)


bot.run('discord bot token')
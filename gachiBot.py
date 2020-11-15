# Module Importieren
import discord
import os
from discord.ext import commands

# Prefix vom Bot bestimmen
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)

def permission(ctx):
    return ctx.author.id == 

@client.command(aliases=['l'])
@commands.check(permission)
async def load(ctx, extension): 
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Modul ' + extension + ' loaded!')
    print('Modul ' + str(extension) + ' an!')

@client.command(aliases=['ul'])
@commands.check(permission)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Modul ' + extension + ' unloaded!')
    print('Modul ' + str(extension) + ' aus!')

@client.command(aliases=['r'])
@commands.check(permission)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Modul ' + extension + ' reloaded!')
    print('Modul ' + str(extension) + ' reload!')


for filename in os.listdir('E:/gachiBot/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# Bot starten
client.run("")
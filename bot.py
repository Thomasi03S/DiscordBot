import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
# import music
from Cogs import music


client = commands.Bot(command_prefix= '.')
status = cycle(['with these hoes', 'with mah dick'])

@client.command()
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'Cogs.{filename[:-3]}')

@client.event
async def on_ready():
    change_status.start()

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print (f'{member} has left the server.')


client.run('OTA3MjAyNDUzNzUyMTMxNTk1.YYjwHw.2p1MiK3An7n9GZ-RvyZfvIgpNAQ')
# Module Importieren
import discord
from discord.ext import commands

class Welcome(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} joined')
        true_member_count = len([m for m in ctx.guild.members if not m.bot]) # doesn't include bots
        channel = self.client.get_channel()
        embed=discord.Embed(title=f'{member}'[0:-5] + " joined the Server!", color=0xf42c6d)
        embed.set_author(name="gachiDiscord | Member Alert" + true_member_count, url="", icon_url="https://i.imgur.com/qO4ulwi.png")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} left')
        channel = self.client.get_channel()
        embed=discord.Embed(title=f'{member}'[0:-5] + " left the Server!", color=0xff9500)
        embed.set_author(name="gachiDiscord | Member Alert", url="", icon_url="https://i.imgur.com/qO4ulwi.png")
        await channel.send(embed=embed)

    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Client Latency: {round(self.client.latency * 1000)}')

def setup(client):
    client.add_cog(Welcome(client))

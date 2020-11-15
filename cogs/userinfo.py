#Module Importieren
import discord
from discord.ext import commands

class Userinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Commands
    @commands.command()
    async def userinfo(ctx, member):
        if ctx.author.guild_permissions.administrator:
            x = ctx.guild.members
            if target in x:
                roles = [role for role in target.roles]
                embed = discord.Embed(title="User information", colour=discord.Color.gold(), timestamp=datetime.utcnow())

                embed.set_author(name=target.name, icon_url=target.avatar_url)

                embed.set_thumbnail(url=target.avatar_url)

                embed.set_footer(text="Mr.KapiBara", icon_url="https://cdn.discordapp.com/attachments/618434755981213716/718861010223497236/kapi-1.png")

                fields = [("Name", str(target), False),
                    ("ID", target.id, False),
                    ("Status", str(target.status).title(), False),
                    (f"Roles ({len(roles)})", " ".join([role.mention for role in roles]), False),
                    ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
                    ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), False)]

                for name, value, inline in fields:
                        embed.add_field(name=name, value=value, inline=inline)

                await ctx.send(embed=embed)
            else:
                await ctx.send(f'You have to ping soneone from this server')
        else:
            await ctx.send(f'Not enough permissions')

        
def setup(client):
    client.add_cog(Userinfo(client))
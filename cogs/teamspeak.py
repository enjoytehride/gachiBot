import discord
from discord.ext import commands
import ts3
import time
import json

class teamspeak(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Commands
    @commands.command(aliases=['ts'])
    async def teamspeak(self, ctx):
        with ts3.query.TS3Connection('', 10011) as ts3conn:
            ts3conn.login(client_login_name='', client_login_password='')
            ts3conn.use(sid=1)
            serverinfo = ts3conn.serverinfo()
            # print(serverinfo.parsed[0])
            ts3conn.servernotifyregister(event="server")
            tsname = serverinfo.parsed[0]["virtualserver_name"]
            tsclientsonline = serverinfo.parsed[0]["virtualserver_clientsonline"]
            tsclients = serverinfo.parsed[0]["virtualserver_maxclients"]
            tsstatus = serverinfo.parsed[0]["virtualserver_status"]
            tsversion = serverinfo.parsed[0]["virtualserver_version"]
            tsplatform = serverinfo.parsed[0]["virtualserver_platform"]
            tsuptime = serverinfo.parsed[0]["virtualserver_uptime"]
            tsuptime2 = time.strftime("%H:%M:%S", time.gmtime(int(tsuptime)))
            tsicon = serverinfo.parsed[0]["virtualserver_hostbutton_gfx_url"]
            tswelcomemsg = serverinfo.parsed[0]["virtualserver_welcomemessage"]
            userlist = []
            resp = ts3conn.clientlist()

            for client in resp.parsed:
                userlist.append(client["client_nickname"])

            userlist.remove("serveradmin")

            if len(userlist) == 0:
                tsusers = "No one online."
            if not len(userlist) == 0:
                tsusers = ', '.join(userlist[0:222])

        user = format(ctx.message.author)
        embed=discord.Embed(title=str(tsname), description=str(tswelcomemsg), color=0xf42c6d)
        embed.set_author(name="TeamSpeak³ Server Status", url="", icon_url="https://i.imgur.com/qO4ulwi.png")
        embed.set_thumbnail(url="https://i.imgur.com/AdXMVZG.png")
        embed.add_field(name="Adresse", value="ts.gachi.de", inline=True)
        embed.add_field(name="User", value=str(int(tsclientsonline)-1) + " / " + str(tsclients), inline=True)
        embed.add_field(name="Version", value=str(tsversion)[0:-19] + str(tsplatform), inline=False)
        embed.add_field(name="Status", value=str(tsstatus), inline=True)
        embed.add_field(name="Uptime", value=str(tsuptime2), inline=True)
        embed.add_field(name="Online Users", value=tsusers, inline=False)
        embed.set_footer(text="requested by " + str(user))
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(teamspeak(client))

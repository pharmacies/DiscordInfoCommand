import datetime as dt
import discord
from discord.ext import commands

picture = "https://cdn.discordapp.com/attachments/751919923260817502/858958993102733312/agarz.webp"


class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='Info', help='Display info on a user!', aliases=["whois"])
    async def info(self, ctx, user: discord.Member = None):
        member = user or ctx.author

        pfp = member.avatar_url
        UserID = member.id
        UserPing = member.mention
        Nickname = member.nick
        if member.joined_at is None:
            pos = "N/A"
        else:
            pos = sum(m.joined_at < member.joined_at for m in ctx.guild.members if m.joined_at is not None) + 1

        if member.activity:
            CustomStatus = member.activity.name
        else:
            CustomStatus = ("None")

        if member.status == discord.Status.online:
            Status = ("Online")
        elif member.status == discord.Status.offline:
            Status = ("Offline")
        elif member.status == discord.Status.idle:
            Status = ("Idle")
        else:
            Status = ("Do Not Disturb")

        if member.guild_permissions.administrator is True:
            Admin = ("Yes")
        else:
            Admin = ("No")

        duration = dt.datetime.now() - member.created_at
        hours, remainder = divmod(int(duration.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        if days == -1:
            days = 0
        else:
            days = days
        Registered_time = f'{days}d ago'

        duration = dt.datetime.now() - member.joined_at
        hours, remainder = divmod(int(duration.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        if days == -1:
            days = 0
        else:
            days = days
        Joined_time = f'{days}d ago'

        date_format = "%b-%d, %Y"

        CreationDate = member.created_at.strftime(date_format)
        JoinDate = member.joined_at.strftime(date_format)

        embed = discord.Embed(description=f"{member}'s profile", timestamp=dt.datetime.utcnow(), color=0x8c9eff)
        embed.add_field(name="** **", inline=False, value=(f"** ID: ** {UserID}\n ** Profile: **{UserPing}\n ** Nickname: **{Nickname}\n ** Avatar: **[Link]({pfp})"))
        embed.add_field(name="** **", inline=False, value=(f"** Registered: ** {Registered_time} ({CreationDate})\n ** Joined: **{Joined_time} ({JoinDate})\n **Positon: **{pos}"))
        embed.add_field(name="** **", inline=False, value=(f"** Admin: ** {Admin}\n ** Status: **{Status}\n ** Playing or Custom Status: **{CustomStatus}\n"))
        embed.set_thumbnail(url=pfp)
        embed.set_footer(text=('Powered by Agarz'), icon_url=(picture))
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Info(client))

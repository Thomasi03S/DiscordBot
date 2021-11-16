import discord
from discord.ext import commands

class mod_commands (commands.Cog):

    def __init__(self, client):
        self.client = client
    def setup(client):
        client.add_cog(mod_commands(client))
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Mod commands are Online.')

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Bansned {member.mention}')

    @commands.command()
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'latency is: {round(self.client.latency*1000)}ms')

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await (ctx.guild.unban(user))
                await (ctx.send(f'Unbanned {user.name}#{user.mention}'))
                return

def setup(client):
    client.add_cog(mod_commands(client))

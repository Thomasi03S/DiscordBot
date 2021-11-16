import random
import discord
from discord.ext import commands
import giphy_client
from giphy_client.rest import ApiExeption

class user_commands (commands.Cog):

    def __init__(self,client):
        self.client = client
    def setup(client):
        client.add_cog(user_commands(client))
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('User commands are Online.')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = [' It is certain.', 'Ask again later.', 'My sources say no.', 'Yes definitely.']
        await ctx.send(f'Question: {question}`\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def gif(self, ctx,*,q="Smile"):

        api_key = 'H4TPZxw7PkocCPJ7IM5hDPJwxhvzmimS'
        api_instance = giphy_client.DefultApi()

        try:

            api_responce = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
            lst = list(api_responce.data)
            giff = random.choice(lst)

            emb = discord.Embed(title=q)
            emb.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')

            await ctx.channel.send(embed=emb)

        except ApiExeption as e:
            print("Exception when calling Api")

def setup(client):
    client.add_cog(user_commands(client))
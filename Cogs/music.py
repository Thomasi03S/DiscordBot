from importlib.util import source_from_cache
from sys import executable
import discord
from discord import message
from discord.ext import commands
from discord.flags import MessageFlags
import youtube_dl


async def play_audio(ctx, url):
    print("yeet")
    #await ctx.voice_client.stop()
    FFMPEG_OPTIONS={ 'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format': 'bestaudio'}
    vc = ctx.voice_client

    ydl = youtube_dl.YoutubeDL()
    info = ydl.extract_info(url, download=False)
    url2 = info['formats'][0]['url']
    print(url2)
    source = await discord.FFmpegOpusAudio.from_probe(url2 ,  method = 'fallback', executable="C:/Users/elev/Documents/FFmpeg/bin/ffmpeg.exe", **FFMPEG_OPTIONS)
    vc.play(source)
    
    print("made it to the end")

class music(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.queues = {}
        self.song = 0

    @commands.command()
    async def queue(self, ctx, url):
        print(ctx.guild.id)
        self.queues[ctx.guild.id].append(url)
        print(self.queues[ctx.guild.id])
        await ctx.send("Added to queue")


    @commands.command()
    async def play_queue(self, ctx):
        for song_url in self.queues[ctx.guild_id]:
            print(song_url)
            await play_audio(ctx, song_url)
            await ctx.send("Playing queue'd song")

    @commands.command()
    async def checkqueue (self):
        print(self.queues)

    @ commands.command()
    async def play (self, ctx, url):
        await play_audio(ctx, url)


    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused!")

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("Playing again!")
    
    @resume.error
    async def resume_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please enter the link to the sound you want to resume.')
    # @pause.error
    # async def pause_error(self, ctx, error):
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         await ctx.send('Please enter the link to the sound witch is playing.')
    
    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("you are not in a voice channel")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
    
    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

def setup(client):
    client.add_cog(music(client))
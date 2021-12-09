from importlib.util import source_from_cache
from sys import executable
import discord
from discord import message
from discord.ext import commands
from discord.ext.commands.core import guild_only
from discord.flags import MessageFlags
import youtube_dl


async def play_audio(ctx, url):
    print("yeet")
    #await ctx.voice_client.stop()
    FFMPEG_OPTIONS={ 'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format': 'bestaudio'}
    vc = ctx.voice_client

    ydl = youtube_dl.YoutubeDL()
    #print(ydl.extract_info(url[0], download))
    info = ydl.extract_info(url, download=False)
    print("passed info")
    url2 = info['formats'][0]['url']
    print(url2)
    source = await discord.FFmpegOpusAudio.from_probe(url2 ,  method = 'fallback', executable="C:/Users/elev/Documents/FFmpeg/bin/ffmpeg.exe", **FFMPEG_OPTIONS)
    vc.play(source)
    
    print("made it to the end")

class music(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.queues_list = []

    @commands.command()
    async def queue(self, ctx, url):
        print(ctx.guild.id)
        self.queues_list.append(url)
        print(self.queues_list)
        await ctx.send("Added to queue")


    @commands.command()
    async def play_queue(self, ctx):
        while self.queues_list != []:
            print("STARTING QUEUE")
            await play_audio(ctx, self.queues_list[0])
            await ctx.self.queues_list.pop(0)
            print(self.queues_list)



        # for autoplay in self.queues_list:
        #     print("AUTOPLAY")
        #     print(autoplay)
        #     await play_audio(ctx, self.autoplay)
        #     # await play_audio(ctx, self.queues_list)
        # else:
        #     await ctx.send("Queue ended")
        # remove_1 = self.queues_list.pop(0)
        # print(remove_1)
        # for song_url in self.queues_list[ctx.guild.id]:
        #     print("EROOR")
        #     print(song_url)
        #     await play_audio(ctx, song_url)
        #     await ctx.send("Playing queue'd song")

    @commands.command()
    async def checkqueue (self, ctx):
        print(self.queues_list)

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
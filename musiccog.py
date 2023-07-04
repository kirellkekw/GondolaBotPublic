import nextcord
import yt_dlp
import asyncio
import os

from nextcord.ext import commands
from nextcord.ext.commands import Context

intents = nextcord.Intents.all()
intents.members = True

filestodelete = []
queuelist = {}
currentmusic = {}
onLoop = {}


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["connect"])
    async def join(self, ctx: Context):
        global queuelist
        guildId = ctx.guild.id
        try:
            queue = queuelist[guildId]
        except KeyError:
            queuelist[guildId] = []
            onLoop[guildId] = False
        await ctx.author.voice.channel.connect()
        try:
            await ctx.message.add_reaction("✅")
        except:
            pass

    @commands.command(aliases=["disconnect"])
    async def leave(self, ctx: Context):
        try:
            await ctx.voice_client.disconnect()
        except:
            pass
        await ctx.message.add_reaction("✅")

    # plays the music
    @commands.command(aliases=["p"])
    async def play(self, ctx: Context, *, searchword):
        global queuelist
        guildId = ctx.guild.id
        try:
            queue = queuelist[guildId]
        except KeyError:
            queuelist[guildId] = []
            queue = queuelist[guildId]
            onLoop[guildId] = False


        await ctx.message.add_reaction("<a:loading:1004527255575334972>")
        ydl_opts = {}
        if ctx.voice_client == None:
            await ctx.author.voice.channel.connect()
        elif ctx.voice_client.channel != ctx.author.voice.channel:
            await ctx.voice_client.disconnect()
            await ctx.author.voice.channel.connect()
        voice: VoiceProtocol = ctx.voice_client

        # Get the Title
        if searchword[0:4] == "http" or searchword[0:3] == "www":
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(searchword, download=False)
                title = info["title"]
                url = searchword

        if searchword[0:4] != "http" and searchword[0:3] != "www":
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(f"ytsearch:{searchword}", download=False)[
                    "entries"][0]
                title = info["title"]
                url = info["webpage_url"]

        title = title.replace(':', '')
        title = title.replace("\\", '')

        ydl_opts = {
            'format': 'bestaudio/best',
            "outtmpl": f"{title}",
            "postprocessors":
            [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3",
                "preferredquality": "max"}],
        }

        def download(url):
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, download, url)

        async def check_queue():

            if onLoop[ctx.guild.id] == True:
                    voice.play(nextcord.FFmpegPCMAudio(f"{currentmusic[ctx.guild.id]}.mp3"), after=lambda e: check_queue())
                    await ctx.send(f"Playing **{queuelist[ctx.guild.id][0]}** :musical_note:")
                    currentmusic[ctx.guild.id] = queuelist[ctx.guild.id][0]
            else:
                try:
                    voice.play(nextcord.FFmpegPCMAudio(f"{queuelist[ctx.guild.id][0]}.mp3"), after=lambda e: check_queue())
                    await ctx.send(f"Playing **{queuelist[ctx.guild.id][0]}** :musical_note:")
                    filestodelete.append(queuelist[ctx.guild.id][0])
                    currentmusic[ctx.guild.id] = queuelist[ctx.guild.id][0]
                    queuelist[ctx.guild.id].pop(0)
                except IndexError:
                    for file in filestodelete:
                        os.remove(f"{file}.mp3")
                    filestodelete.clear()

        # Playing and Queueing Audio
        if voice.is_playing():
            queue.append(title)
            await ctx.send(f"Added ** {title} ** to the queue :musical_note:")
            await ctx.message.add_reaction("✅")
        else:
            if onLoop[ctx.guild.id] == True:               
                voice.play(nextcord.FFmpegPCMAudio(f"{currentmusic[ctx.guild.id]}.mp3"), after=lambda e: check_queue())
            else:
                voice.play(nextcord.FFmpegPCMAudio(f"{title}.mp3"), after=lambda e: check_queue())
                currentmusic[ctx.guild.id] = title
            await ctx.message.add_reaction("✅")
            await ctx.send(f"Playing ** {title} ** :musical_note:")
            filestodelete.append(title)

    # skips the current music
    @commands.command(aliases=["skip"])
    async def next(self, ctx: Context):
        global queuelist
        guildId = ctx.guild.id
        if onLoop[guildId] == True:
            await ctx.send("Skip is disabled when looping!")
            return
        try:
            queue = queuelist[guildId]
        except KeyError:
            queuelist[guildId] = []
            queue = queuelist[guildId]
        if ctx.voice_client == None:
            await ctx.send("Bot is not in a Voice Channel!")
            return
        voice: VoiceProtocol = ctx.voice_client
        if voice.is_playing() == True:
            if len(queue) == 0:
                await ctx.send("There is no music in queue!")
                return
            voice.stop()
            voice.play(nextcord.FFmpegPCMAudio(f"{queue[0]}.mp3"))
            filestodelete.append(queue[0])
            await ctx.send(f"✅ Skipped\nPlaying ** {queue[0]} ** :musical_note:")
            currentmusic[ctx.guild.id] = queue[0]
            queue.pop(0)
            try:
                await ctx.message.add_reaction("✅")
            except:
                pass
        else:
            await ctx.send("Bot is not playing Audio!")

    # pauses playing audio
    @commands.command(aliases=["stop"])
    async def pause(self, ctx: Context):
        voice: VoiceProtocol = ctx.voice_client
        if voice.is_playing() == True:
            voice.pause()
            try:
                await ctx.message.add_reaction("✅")
            except:
                pass
        else:
            await ctx.send("Bot is not playing Audio!")

    # loops current music
    @commands.command()
    async def loop(self, ctx:Context):
        global queuelist, currentmusic
        guildId = ctx.guild.id
        try:
            onLoop[guildId] = not onLoop[guildId]
            try:
                await ctx.message.add_reaction("✅")
            except:
                pass
            await ctx.send(f"Loop mode {'disabled' if onLoop[guildId] == False else 'enabled'}.")
        except KeyError:
            await ctx.send("An error occurred. Please make sure the bot is playing music!")

    # resumes playing audio
    @commands.command()
    async def resume(self, ctx: Context):
        voice = ctx.voice_client
        if voice.is_playing() == True:
            await ctx.send("Bot is playing Audio!")
        else:
            try:
                voice.resume()
                await ctx.message.add_reaction("✅")
            except:
                pass

    # function that displays the current queue
    @commands.command(aliases=["viewqueue"])
    async def queue(self, ctx: Context):
        global queuelist
        guildId = ctx.guild.id
        queue = queuelist[guildId]
        try:
            await ctx.message.add_reaction("✅")
            msg = "```Queue:"
            if onLoop[guildId] == True:
                msg += f"\nLooping is enabled for *{currentmusic[ctx.guild.id]}*"
            for i in enumerate(queue):
                msg += f"\n**{i[0]+1}. {i[1]}**"
            await ctx.send(f'{msg}```')
        except KeyError:
            await ctx.send("There is no music in queue!")

    @commands.command()
    async def clearqueue(self, ctx: Context):
        global queuelist
        guildId = ctx.guild.id
        try:
            queue = queuelist[guildId]
        except KeyError:
            queuelist[guildId] = []
            queue = queuelist[guildId]
        queue.clear()
        try:
            await ctx.message.add_reaction("✅")
        except:
            pass


def setup(bot):
    bot.add_cog(Music(bot))

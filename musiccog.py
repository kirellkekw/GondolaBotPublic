import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import Context
import yt_dlp
import asyncio
import os

intents = nextcord.Intents.all()
intents.members = True

filestodelete = []
queuelist = {}
currentmusic = {}
onLoop = {}

# tries to add a check reaction


async def addCheck(ctx: Context):
    try:
        await ctx.message.add_reaction("✅")
    except:
        pass

# tries to add a cross reaction


async def addCross(ctx: Context):
    try:
        await ctx.message.add_reaction("❌")
    except:
        pass

# tries to add a loading reaction


async def addLoading(ctx: Context):
    try:
        await ctx.message.add_reaction("<a:loading:1004527255575334972>")
    except:
        pass

# tries to remove the loading reaction


async def removeLoading(ctx: Context):
    try:
        await ctx.message.remove_reaction("<a:loading:1004527255575334972>", ctx.guild.me)
    except:
        pass


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # connects the bot to the voice channel
    @commands.command(aliases=["connect"])
    async def join(self, ctx: Context):
        guildId = ctx.guild.id

        try:
            queue = queuelist[guildId]  # check if the queue exists
        except KeyError:  # if the queue does not exist, create it
            queuelist[guildId] = []
            onLoop[guildId] = False  # set the loop default to false

        if ctx.voice_client == None:
            await ctx.author.voice.channel.connect()  # connect to the voice channel
            await addCheck(ctx)
        else:
            await ctx.send("Bot is already in a Voice Channel!")
            await addCross(ctx)

    # disconnects the bot from the voice channel
    @commands.command(aliases=["disconnect"])
    async def leave(self, ctx: Context):
        try:
            onLoop[ctx.guild.id] = False  # set the loop to false
            await ctx.voice_client.disconnect()
            await addCheck(ctx)
        except:
            await ctx.send("Bot is not in a Voice Channel!")
            await addCross(ctx)
            return

    # plays the music
    @commands.command(aliases=["p"])
    async def play(self, ctx: Context, *, searchword):
        guildId = ctx.guild.id

        try:
            queue = queuelist[guildId]  # check if the queue exists
        except KeyError:
            queuelist[guildId] = []  # if the queue does not exist, create it
            # set the queue to the newly created queue
            queue = queuelist[guildId]
            onLoop[guildId] = False  # set the loop default to false

        await addLoading(ctx)

        # Downloading Sequence

        ydl_opts = {}
        if ctx.voice_client == None:
            voice = await ctx.author.voice.channel.connect()
        elif ctx.voice_client.channel != ctx.author.voice.channel:
            await ctx.voice_client.disconnect()
            voice = await ctx.author.voice.channel.connect()
        # voice = ctx.voice_client

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

        # remove characters that are not allowed in filenames
        title = title.strip("\\:<>?/*\"|")
        ydl_opts = {
            'format': 'bestaudio/best',
            "outtmpl": f"{title}",
            "postprocessors":
            [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3",
                "preferredquality": "192"}],
        }

        def download(url):
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        loop = asyncio.get_event_loop()
        # download the music in the background
        await loop.run_in_executor(None, download, url)

        async def check_queue():

            if onLoop[guildId] == True:  # if looping is enabled
                # play the current music again
                voice.play(nextcord.FFmpegPCMAudio(
                    f"{currentmusic[guildId]}.mp3"), after=lambda e: check_queue())
                # send a message that the music is playing
                await ctx.send(f"Playing **{currentmusic[guildId]}** :musical_note:")
                # set the current music to the first music in queue
                currentmusic[guildId] = queuelist[guildId][0]

            else:  # if looping is disabled

                try:  # try to play the next music in queue
                    voice.play(nextcord.FFmpegPCMAudio(
                        f"{queuelist[guildId][0]}.mp3"), after=lambda e: check_queue())
                    await ctx.send(f"Playing **{queuelist[guildId][0]}** :musical_note:")
                    filestodelete.append(queuelist[guildId][0])
                    currentmusic[guildId] = queuelist[guildId][0]
                    queuelist[guildId].pop(0)

                except IndexError:  # if there is no music in queue, remove musics from OS
                    for file in filestodelete:
                        os.remove(f"{file}.mp3")
                    filestodelete.clear()

        # Playing and Queueing Audio
        if voice.is_playing():
            queue.append(title)
            await ctx.send(f"Added ** {title} ** to the queue :musical_note:")
            await removeLoading(ctx)
            await addCheck(ctx)
        else:
            if onLoop[guildId] == True:
                voice.play(nextcord.FFmpegPCMAudio(
                    f"{currentmusic[guildId]}.mp3"), after=lambda e: check_queue())
                await ctx.send(f"Playing **{currentmusic[guildId]}** :musical_note:")
            else:
                voice.play(nextcord.FFmpegPCMAudio(
                    f"{title}.mp3"), after=lambda e: check_queue())
                currentmusic[guildId] = title

            await removeLoading(ctx)
            await addCheck(ctx)
            await ctx.send(f"Playing ** {title} ** :musical_note:")
            filestodelete.append(title)

    # skips the current music
    @commands.command(aliases=["next"])
    async def skip(self, ctx: Context):
        guildId = ctx.guild.id

        if onLoop[guildId]:  # if looping is enabled, skip is disabled
            await ctx.send("Skip is disabled when looping!")
            await addCross(ctx)
            return

        try:
            queue = queuelist[guildId]  # check if the queue exists
        except KeyError:  # if the queue does not exist, send an error message
            ctx.send("There is no queue to skip!")
            await addCross(ctx)
            return

        if ctx.voice_client == None:
            await ctx.send("Bot is not in a Voice Channel!")
            await addCross(ctx)
            return

        voice = ctx.voice_client

        async def check_queue():

            if onLoop[guildId] == True:  # if looping is enabled
                # play the current music again
                voice.play(nextcord.FFmpegPCMAudio(
                    f"{currentmusic[guildId]}.mp3"), after=lambda e: check_queue())
                # send a message that the music is playing
                await ctx.send(f"Playing **{currentmusic[guildId]}** :musical_note:")
                # set the current music to the first music in queue
                currentmusic[guildId] = queuelist[guildId][0]

            else:  # if looping is disabled

                try:  # try to play the next music in queue
                    voice.play(nextcord.FFmpegPCMAudio(
                        f"{queuelist[guildId][0]}.mp3"), after=lambda e: check_queue())
                    await ctx.send(f"Playing **{queuelist[guildId][0]}** :musical_note:")
                    filestodelete.append(queuelist[guildId][0])
                    currentmusic[guildId] = queuelist[guildId][0]
                    queuelist[guildId].pop(0)

                except IndexError:  # if there is no music in queue, remove musics from OS
                    for file in filestodelete:
                        os.remove(f"{file}.mp3")
                    filestodelete.clear()

        if voice.is_playing() == True:
            if len(queue) == 0:
                await ctx.send("There is no music in queue to skip!")
                await addCross(ctx)
                return
            voice.stop()
            voice.play(nextcord.FFmpegPCMAudio(
                f"{queue[0]}.mp3"), after=lambda e: check_queue())
            filestodelete.append(queue[0])
            await ctx.send(f"✅ Skipped\nPlaying ** {queue[0]} ** :musical_note:")
            currentmusic[guildId] = queue[0]
            queue.pop(0)
            await addCheck(ctx)
        else:
            await ctx.send("Bot is not playing music!")
            await addCross(ctx)

    # pauses playing audio
    @commands.command(aliases=["stop"])
    async def pause(self, ctx: Context):
        voice = ctx.voice_client
        if voice.is_playing() == True:
            voice.pause()
            await ctx.send("Playing paused.")
            await addCheck(ctx)
        else:
            await ctx.send("Bot is not playing music!")
            await addCross(ctx)

    # loops current music
    @commands.command()
    async def loop(self, ctx: Context):
        guildId = ctx.guild.id
        voice = ctx.voice_client
        if voice.is_playing() != True:
            await ctx.send("Nothing is playing!")
            await addCross(ctx)
            return
        try:
            onLoop[guildId] = not onLoop[guildId]
            await addCheck(ctx)
            await ctx.send(f"Loop mode {'disabled' if onLoop[guildId] == False else 'enabled'}.")
        except KeyError:
            await ctx.send("Bot is not playing music!")
            await addCross(ctx)
            return

    # resumes playing audio
    @commands.command()
    async def resume(self, ctx: Context):
        voice = ctx.voice_client
        if voice.is_playing() == True:
            await ctx.send("Bot is already playing!")
            await addCross(ctx)
        else:
            voice.resume()
            await ctx.send("Playing resumed.")
            await addCheck(ctx)

    # function that displays the current queue
    @commands.command(aliases=["viewqueue"])
    async def queue(self, ctx: Context):

        guildId = ctx.guild.id
        queue = queuelist[guildId]
        try:
            await addCheck(ctx)
            msg = "```Queue:"
            if onLoop[guildId] == True:
                msg += f"\nLooping is enabled for *{currentmusic[guildId]}*"
            for i in enumerate(queue):
                msg += f"\n{i[0]+1}- {i[1]}"
            await ctx.send(f'{msg}```')
        except KeyError:
            await ctx.send("There is no music in queue!")
            await addCross(ctx)

    @commands.command()
    async def clearqueue(self, ctx: Context):
        global queuelist
        guildId = ctx.guild
        try:
            queue = queuelist[guildId]
        except KeyError:
            queuelist[guildId] = []
            queue = queuelist[guildId]
        queue.clear()
        await addCheck(ctx)

    @commands.command()
    async def remove(self, ctx: Context, index: int):
        guildId = ctx.guild.id
        queue = queuelist[guildId]
        try:
            queue.pop(index-1)
            await ctx.send(f"Removed music at index {index}!")
            await addCheck(ctx)
        except IndexError:
            await ctx.send("Invalid index!")
            await addCross(ctx)
        except KeyError:
            await ctx.send("There is no music in queue!")
            await addCross(ctx)

    @commands.command()
    async def music(self, ctx: Context):
        await ctx.send(
            """
    ```Music Commands:
    join: Joins the voice channel you are in.
    leave: Leaves the voice channel.
    play <searchword>: Plays the music you searched for.
    skip: Skips the current music.
    pause: Pauses the current music.
    resume: Resumes the current music.
    loop: Loops the current music.
    queue: Displays the current queue.
    clearqueue: Clears the current queue.
    remove <index>: Removes the music at the specified index from the queue.
    music: Displays this message.```
    """)


def setup(bot):
    bot.add_cog(Music(bot))

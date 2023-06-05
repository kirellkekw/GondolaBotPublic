import random
import yt_dlp
import nextcord
import asyncio

from main import name, version, bot, prefix
from nextcord import Intents, Member
from nextcord.ext import commands
from nextcord.ext.commands import Context
from apifuncs import *

intents = Intents.all()


########## bot commands start ##########

class PrefixCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def commit(self, ctx: Context):
        await ctx.send(commitmsg())

    @help.command()
    async def commit(self, ctx: Context):
        em = Embed(
            title="commit", description=f"Shows a random commit message.\nUsage = \"`{prefix}commit`\"", color=ctx.author.color)
        await ctx.send(embed=em)

    # AVATAR

    @commands.command(aliases=["av", "pfp"])
    async def avatar(self, ctx: Context, *, avamember: Member = None):
        if avamember == None:
            avamember = ctx.author
        em = Embed(title=f"Avatar of {avamember.display_name}:")
        em.set_image(avamember.avatar._url)
        await ctx.reply(embed=em)

    @help.command()
    async def avatar(self, ctx: Context):
        em = Embed(
            title="avatar", description=f"Shows the avatar of requested user.\nUsage = \"`{prefix}avatar @user`\"",
            color=ctx.author.color)
        await ctx.send(embed=em)

    # DUCK

    @commands.command()
    async def duck(self, ctx: Context):
        duckembed = Embed(
            title="Here's a duck just for you.", color=ctx.author.color, description="Powered by random-d.uk")
        duckembed.set_image(duckimg())
        await ctx.reply(embed=duckembed)

    @help.command()
    async def duck(self, ctx: Context):
        em = Embed(
            title="duck", description=f"Shows a duck image.\nUsage = \"`{prefix}duck`\"", color=ctx.author.color)
        await ctx.send(embed=em)

    # CAT

    @commands.command()
    async def cat(self, ctx: Context):
        catembed = Embed(
            title="Got one!", color=ctx.author.color, description='Powered by thecatapi.com')
        catembed.set_image(catimg())
        await ctx.send(embed=catembed)

    @help.command()
    async def cat(self, ctx: Context):
        em = Embed(
            title="cat", description=f"Shows a cat image.\nUsage = \"`{prefix}cat`\"", color=ctx.author.color)
        await ctx.send(embed=em)

    # DOG

    @commands.command()
    async def dog(self, ctx: Context):
        dogembed = Embed(
            title="Here's a doggo for you.", color=ctx.author.color, description="Powered by dog.ceo/dog-api/")
        dogembed.set_image(dogimg())
        await ctx.send(embed=dogembed)

    @help.command()
    async def dog(self, ctx: Context):
        em = Embed(
            title="dog", description=f"Shows a dog image.\nUsage = \"`{prefix}dog`\"", color=ctx.author.color)
        await ctx.send(embed=em)

    # BOTINFO

    @commands.command(aliases=["info", "about", "versioninfo"])
    async def botinfo(self, ctx: Context):
        await ctx.send(f"```{name}, version {version}\n"
                       "Powered by free time, quality music and a repository with VERY BAD COMMIT MESSAGES.\n"
                       "Actively developed by kirell#0001.```")

    @help.command()
    async def botinfo(self, ctx: Context):
        em = Embed(
            title="botinfo", description=f"Shows the version info of the bot.\nUsage = \"`{prefix}botinfo`\"",
            color=ctx.author.color)
        await ctx.send(embed=em)

    # CLEAR

    @commands.command(aliases=["purge", "delete"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx: Context, amount: int = 10):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"```Cleared {amount} messages by request of {ctx.author}.```", delete_after=2)

    @help.command()
    async def clear(self, ctx: Context):
        em = Embed(
            title="clear", description=f"Deletes a specified amount of messages.\nUsage = \"`{prefix}clear (amount)`\"",
            color=ctx.author.color)
        await ctx.send(embed=em)

    @clear.error
    async def errorhandler(self, ctx: Context, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send("You are missing permissions to do that!")
        if isinstance(error, commands.errors.BotMissingPermissions):
            await ctx.send("Bot doesn't have the required permissions to do this!\nMissing permissions: `Manage Messages`")

    # PING

    @commands.command()
    async def ping(self, ctx: Context):
        await ctx.send(f"Pong!\nLatency: {bot.latency}!")

    @help.command()
    async def ping(self, ctx: Context):
        em = Embed(
            title="ping", description=f"Sends a basic message to show the latency of bot.\nUsage = \"`{prefix}ping`\"",
            color=ctx.author.color)
        await ctx.send(embed=em)

    # USERCOUNT

    @commands.command(aliases=["membercount"])
    async def usercount(self, ctx: Context):
        memberCount = ctx.guild.member_count
        await ctx.send(f"```Number of members in this server: {memberCount}```")

    @help.command()
    async def usercount(self, ctx: Context):
        em = Embed(
            title="usercount", description=f"Displays the member count in the server.\nUsage = \"`{prefix}usercount`\"",
            color=ctx.author.color)
        await ctx.send(embed=em)

    # TIMER

    @commands.command()
    async def timer(self, ctx: Context):
        text = ctx.message.content.replace(f"{prefix}timer ", '')

        if text.endswith('m'):
            time = int(text.replace('m', ''))
            await ctx.send(f"Timer has been set for {time} minute(s).")
            await asyncio.sleep(time * 60)
        elif text.endswith('h'):
            time = int(text.replace('h', ''))
            await ctx.send(f"Timer has been set for {time} hour(s).")
            await asyncio.sleep(time * 3600)
        else:
            time = int(text.replace('s', ''))
            await ctx.send(f"Timer has been set for {time} second(s).")
            await asyncio.sleep(time)

        await ctx.send(f"Your {text} timer is up, {ctx.author.mention}!")

    @help.command()
    async def timer(self, ctx: Context):
        em = Embed(
            title="timer",
            description=f"Sets a timer of your choice.\nUsage = \"`{prefix}timer (number)(time format(seconds if not given))`\"\nExample: {prefix}timer 35m",
            color=ctx.author.color)
        await ctx.send(embed=em)

    # XKCD

    @commands.command()
    async def xkcd(self, ctx: Context):
        if ctx.message.content == f'{prefix}xkcd':
            randnum = random.randint(1, 2653)
            await ctx.send(f"https://xkcd.com/{randnum}/")
        elif ctx.message.content == f'{prefix}xkcd 0':
            await ctx.send("https://xkcd.com/")
        else:
            num = ctx.message.content.replace(f'{prefix}xkcd ', '')
            await ctx.send(f"https://xkcd.com/{num}/")

    @help.command()
    async def xkcd(self, ctx: Context):
        em = Embed(
            title="xkcd",
            description=f"Shows a random xkcd comic or one of your choice.\nUsage = \"`{prefix}xkcd (optionalnumber)`\"",
            color=ctx.author.color)
        await ctx.send(embed=em)

    # INVITE

    @commands.command()
    async def invite(self, ctx: Context):
        await ctx.send(
            "```Please note that this bot is constantly developing. In any case of problems, error or suggestions, contact me from kirell#6931 or support server.```\n\n"
            "**Bot Invite Link**\n"
            "https://discord.com/api/oauth2/authorize?client_id=994282865254731826&permissions=137442477120&scope=applications.commands%20bot\n\n"
            "**Support Server**\n"
            "https://discord.gg/hr2P8mS8Pd")

    @help.command()
    async def invite(self, ctx: Context):
        em = Embed(
            title="invite", description=f"Shows the invite link for this bot.\nUsage = \"`{prefix}invite`\"",
            color=ctx.author.color)
        await ctx.send(embed=em)

    # SERVERCOUNT

    @commands.command()
    async def servercount(self, ctx: Context):
        activeservercount = len(bot.guilds)
        await ctx.send(f"```{name} is now currently operating in {activeservercount} guilds.```")

    @help.command()
    async def servercount(self, ctx: Context):
        em = Embed(
            title="servercount", description="Shows how many servers this bot currently runs in.\n"
                                             f"Usage = \"`{prefix}servercount`\"", color=ctx.author.color)
        await ctx.send(embed=em)

    # COINFLIP

    @commands.command(aliases=['cf', 'coin', 'flip'])
    async def coinflip(self, ctx: Context):
        choice = ["Heads", "Tails"]
        side = random.randint(1, 6000)
        if side == 1033:
            await ctx.channel.send("Coin landed on it's side!")
        else:
            await ctx.channel.send(f"The coin landed on {random.choice(choice)}.")

    @help.command()
    async def coinflip(self, ctx: Context):
        em = Embed(
            title="coinflip", description=f"Flips a coin just because you asked.\nUsage = \"`{prefix}coinflip`\"",
            color=ctx.author.color)
        await ctx.send(embed=em)

    # GONDOLA

    @commands.command()
    async def gondola(self, ctx: Context):
        gondolaembtext = Embed(color=ctx.author.color,
                               title="Thanks to Sparrow#5926 for the archive!")
        link = gondolaimg()
        gondolaembtext.set_image(link)
        await ctx.send(embed=gondolaembtext)

    @help.command()
    async def gondola(self, ctx: Context):
        em = Embed(
            title="gondola", description=f"Shows a random gondola image.\nUsage = \"`{prefix}gondola`\"", color=ctx.author.color)
        await ctx.send(embed=em)

    # GONDVID

    @commands.command()
    async def gondvid(self, ctx: Context):
        link = gondvideo()
        await ctx.send(f"Thanks to `gondola.stravers.net` for the content!\n{link}")

    @help.command()
    async def gondvid(self, ctx: Context):
        em = Embed(
            title="gondvid", description=f"Shows a random gondola video.\nUsage = \"`{prefix}gondvid`\"", color=ctx.author.color)
        await ctx.send(embed=em)

    # MUSIC

    @help.command()
    async def music(self, ctx: Context):
        em = Embed(title="Music Commands", color=ctx.author.color)
        em.add_field(
            name="join", value="Commands the bot to join your voice channel.", inline=False)
        em.add_field(
            name="leave", value="Commands the bot to leave your voice channel.", inline=False)
        em.add_field(name="play", value="Plays or queues a YouTube music of your choice.\n"
                                        "Example usages:\n ```{prefix}play acts of man\n{prefix}play https://www.youtube.com/watch?v=fcHVYrcb6As```",
                     inline=False)
        em.add_field(name="pause", value="Pauses the music.", inline=False)
        em.add_field(name="resume", value="Resumes the music.", inline=False)
        em.add_field(
            name="queue", value="Shows the music queue.", inline=False)
        em.add_field(name="clearqueue",
                     value="Clears the music queue.", inline=False)
        await ctx.send(embed=em)

    # çukurova yemek

    @commands.command()
    async def yemek(self, ctx: Context):
        msg = cukurovayemek()
        await ctx.send(msg)

    # ytmp3

    @commands.command()
    async def ytmp3(self, ctx: Context, *, searchword):
        ydl_opts = {}
        await ctx.message.add_reaction("<a:loading:1004527255575334972>")

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

        title: str = title.replace(':', '')
        title = title.replace("\\", '')
        CYRILLIC_TO_LATIN_MAP = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
            'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm',
            'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
            'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
            'ы': 'y', 'э': 'e', 'ю': 'iu', 'я': 'ia'
        }

        def cyrillic_to_latin(text):
            return ''.join(CYRILLIC_TO_LATIN_MAP.get(char.lower(), char) for char in text)

        title = cyrillic_to_latin(title)

        ydl_opts = {
            'format': 'bestaudio/best',
            "outtmpl": f"{title}",
            "postprocessors":
                [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3",
                  "preferredquality": "256"}], }

        # Downloads the Audio File with the Title, it is run in a different thread so that the bot can communicate to the discord server while downloading
        def download(url):
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, download, url)

        with open(f'{title}.mp3', 'rb') as fp:
            await ctx.message.reply(file=nextcord.File(fp, f'{title}.mp3'))
            await ctx.message.remove_reaction("<a:loading:1004527255575334972>",
                                              member=bot.get_user(994282865254731826))
            await ctx.message.add_reaction("✅")

    @help.command()
    async def ytmp3(self, ctx: Context):
        em = Embed(title="ytmp3", description=f"Sends mp3 file of given youtube video.\nUsage = \"`{prefix}ytmp3 hello adele`\"",
                   color=ctx.author.color)
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(PrefixCommands(bot))

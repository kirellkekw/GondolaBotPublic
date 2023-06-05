import nextcord
from nextcord.ext import commands
import asyncio
import random
import yt_dlp
from apifuncs import *
from main import name, version
from nextcord import Embed
from nextcord import Interaction

intents = nextcord.Intents.all()


class SlashCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="Shows the help menu.")
    async def help(self, interaction=Interaction):
        helpembed = Embed(title="Help Menu", description="Here is the list of available commands!\nMy current prefix is \"`/`\" .\n"
                          "For more information on a command, you can type \"`--help <command>`\".\n"
                          "For requests, questions and more, you can reach the support server from this link.\nhttps://discord.gg/hr2P8mS8Pd", color=interaction.user.color)
        helpembed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/994282865254731826/a9acf2de599043c9966a420ff29ced2d.png?size=1024")
        helpembed.add_field(
            name="avatar", value="Shows the avatar of requested user.", inline=False)
        helpembed.add_field(
            name="botinfo", value="Displays bot info.", inline=False)
        helpembed.add_field(
            name="cat", value="Displays a random cat image.", inline=False)
        helpembed.add_field(
            name="coinflip", value="A coinflip with literally and absolutely no chance of staying on it's edge.", inline=False)
        helpembed.add_field(
            name="clear", value="Clears a specified amount of messages from that channel.", inline=False)
        helpembed.add_field(
            name="commit", value="Shows a random commit message.", inline=False)
        helpembed.add_field(
            name="dog", value="Shows a random dog image.", inline=False)
        helpembed.add_field(
            name="duck", value="Shows a random duck image.", inline=False)
        helpembed.add_field(
            name="gondola", value="Shows a random gondola image.", inline=False)
        helpembed.add_field(
            name="gondvid", value="Sends a random gondola video.", inline=False)
        helpembed.add_field(
            name="invite", value="Displays the invite link for this bot.", inline=False)
        helpembed.add_field(
            name="ping", value="Pong!", inline=False)
        helpembed.add_field(
            name="timer", value="Starts a timer for a specified time limit.", inline=False)
        # helpembed.add_field(
        #     name="usercount", value="Displays the member count in the current guild.", inline=False)
        helpembed.add_field(
            name="xkcd", value="Shows a random xkcd comic, or one of your choice.", inline=False)

        # helpembed.add_field(name = "", value = "", inline = False)

        await interaction.send(embed=helpembed)

    # AVATAR
    @nextcord.slash_command(description="Shows the avatar of requested user.")
    async def avatar(self, interaction=Interaction, *, user: nextcord.Member = None):
        if user == None:
            user = interaction.user
        em = Embed(title=f"Avatar of {user.display_name}:")
        em.set_image(user.avatar._url)
        await interaction.send(embed=em)

    # COMMIT

    @nextcord.slash_command(description="Sends a random commit message.")
    async def commit(self, interaction=Interaction):
        await interaction.send(commitmsg())

    # DUCK

    @nextcord.slash_command(description="Shows a random duck image.")
    async def duck(self, interaction=Interaction):
        duckembed = Embed(
            title="Powered by random-d.uk", color=interaction.user.color)
        duckembed.set_image(duckimg())
        await interaction.send(embed=duckembed)

    # CAT

    @nextcord.slash_command(description="Shows a random cat image.")
    async def cat(self, interaction=Interaction):
        catembed = Embed(
            title="Powered by thecatapi.com", color=interaction.user.color)
        catembed.set_image(catimg())
        await interaction.send(embed=catembed)

    # DOG

    @nextcord.slash_command(description="Shows a random dog image.")
    async def dog(self, interaction=Interaction):
        dogembed = Embed(
            title="Powered by dog.ceo/dog-api/", color=interaction.user.color)
        dogembed.set_image(dogimg())
        await interaction.send(embed=dogembed)

    # BOTINFO

    @nextcord.slash_command(description="Shows the version info of the bot.")
    async def botinfo(self, interaction=Interaction):
        await interaction.send(f"```{name}, version {version}\n"
                               "Powered by love, quality music and a lot of syntax errors.\n"
                               "Actively developed by kirell#6931.```")

    # CLEAR

    @nextcord.slash_command(description="Deletes a specified amount of messages.")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, interaction=Interaction, amount: int = 10):
        await interaction.channel.purge(limit=amount)
        await interaction.send(f"```cleared {amount} messages by request of {interaction.user}.```", delete_after=10)

    # PING

    @nextcord.slash_command(description="Sends the latency info of bot.")
    async def ping(self, interaction=Interaction):
        await interaction.send(f"Pong!")

    # # USERCOUNT
    # @nextcord.slash_command(description="Displays the member count in the server.")
    # async def membercount(self, interaction=Interaction):
    #     guildId = interaction.guild_id
    #     await interaction.send(f"```Number of members in this server: {memberCount}```")

    # XKCD

    @nextcord.slash_command(description="Shows a random xkcd comic or one of your choice.")
    async def xkcd(self, interaction=Interaction, number: int = 9999):
        if number == 9999:
            randnum = random.randint(1, 2653)
            await interaction.send(f"https://xkcd.com/{randnum}/")
        elif number == 0:
            await interaction.send("https://xkcd.com/")
        else:
            await interaction.send(f"https://xkcd.com/{number}/")

    # INVITE

    @nextcord.slash_command(description="Shows the invite link for this bot.")
    async def invite(self, interaction=Interaction):
        await interaction.send("```Please note that this bot is not fully completed. In case of any problems or errors, please contact me from kirell#6931.```\n\n"
                               "https://discord.com/oauth2/authorize?client_id=994282865254731826&permissions=414467877952&scope=bot%20applications.commands")

    # COINFLIP

    @nextcord.slash_command(description="Flips a coin just because you asked.")
    async def coinflip(self, interaction=Interaction):
        choice = ["Heads", "Tails"]
        side = random.randint(1, 6000)
        if side == 1033:
            await interaction.send("Coin landed on it's side!")
        else:
            await interaction.send(f"The coin landed on {random.choice(choice)}.")

    # GONDOLA

    @nextcord.slash_command(description="Sends a random gondola image.")
    async def gondola(self, interaction=Interaction):
        gondolaembtext = Embed(color=interaction.user.color,
                               title="Thanks to Sparrow#5926 for the archive!")
        link = gondolaimg()
        gondolaembtext.set_image(link)
        await interaction.send(embed=gondolaembtext)

    # GONDVID

    @nextcord.slash_command(description="Sends a random gondola video.")
    async def gondvid(self, interaction=Interaction):
        link = gondvideo()
        await interaction.send(f"Thanks to `gondola.stravers.net` for the content!\n{link}")

    # TIMER

    @nextcord.slash_command(description="Creates a timer with the input you give.")
    async def timer(self, interaction=Interaction, text: str = "10m"):
        num = int(text.strip("minutescondhr "))
        if text.endswith("m") or text.endswith("minute") or text.endswith("minutes"):
            await interaction.send(f"Timer has been set for {num} minute(s).")
            await asyncio.sleep(num * 60)
        elif text.endswith("h") or text.endswith("hour") or text.endswith("hours"):
            await interaction.send(f"Timer has been set for {num} hour(s).")
            await asyncio.sleep(num * 3600)
        else:
            await interaction.send(f"Timer has been set for {num} second(s).")
            await asyncio.sleep(num)

        await interaction.send(f"Your {text} timer is up, {interaction.user.mention}!")

    # ytmp3

    @nextcord.slash_command(description="Sends mp3 of given YouTube video.")
    async def ytmp3(self, interaction=Interaction, *, searchword):
        ydl_opts = {}
        # await interaction.message.add_reaction("<a:loading:1004527255575334972>")
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
                "preferredquality": "192"}], }

        # Downloads the Audio File with the Title, it is run in a different thread so that the bot can communicate to the discord server while downloading
        def download(url):
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, download, url)

        with open(f'{title}.mp3', 'rb') as fp:
            await interaction.send(file=nextcord.File(fp, f'{title}.mp3'))
        #    await interaction.message.remove_reaction("<a:loading:1004527255575334972>", member = gondbot.get_user(994282865254731826))
        #    await interaction.message.add_reaction("✅")


def setup(bot):
    bot.add_cog(SlashCmd(bot))

import os
from nextcord import Embed, File
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context
from config import prefix, loading_emoji
import yt_dlp
import asyncio


name = "ytmp3"
description = "Convert a YouTube video(or any other videos) to a mp3 file."
usage = f"{prefix}ytmp3 Elephant - Tame Impala\n{prefix}ytmp3 https://www.youtube.com/watch?v=dQw4w9WgXcQ"


@commands.command(aliases=["mp3", "yt2mp3"])
async def ytmp3(ctx: Context, *, search_query):
    ydl_opts = {}
    await ctx.message.add_reaction(loading_emoji)
    em = Embed(description="Download job running...", color=ctx.author.color)
    em.add_field(name="Search Query", value=search_query)
    em.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar._url)

    my_msg = await ctx.message.reply(embed=em)

    # Get the Title
    if search_query[0:4] == "http" or search_query[0:3] == "www":
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(search_query, download=False)
            title = info["title"]
            url = search_query

    if search_query[0:4] != "http" and search_query[0:3] != "www":
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{search_query}", download=False)[
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
        "outtmpl": f"{title}{ctx.author.id}q",
        "postprocessors":
            [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3",
              "preferredquality": "256"}], }

    # Downloads the Audio File with the Title, it is run in a different thread so that the bot can communicate to the discord server while downloading
    def download(url):
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, download, url)

    with open(f'{title}{ctx.author.id}q.mp3', 'rb') as fp:
        try:
            await my_msg.edit(file=File(fp, f'{title}.mp3'),embed=None)
            # await ctx.message.reply(file=File(fp, f'{title}.mp3'))
            await ctx.message.remove_reaction(loading_emoji, member=ctx.guild.me)
            await ctx.message.add_reaction("✅")
            # await my_msg.delete()
        except Exception:
            await ctx.message.reply("An error occurred, please give me file permissions or try this command in a different channel.")
            await ctx.message.remove_reaction(loading_emoji, member=ctx.guild.me)
            await ctx.message.add_reaction("❌")
    
    
    # Deletes the File from the Bot's Directory
    await asyncio.sleep(10)
    fp.close()
    os.remove(f'{title}{ctx.author.id}q.mp3')

def setup(bot: Bot):
    bot.add_command(ytmp3)

from nextcord import Embed
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context
import requests as r


def gondolaimg():
    res = r.get("https://sparow.club/gondfotoday.php")
    print(res.content)
    imglink = (str(res.content).replace("b'\\n\\n", '')).replace("'", '')

    if imglink.endswith(".webm") or imglink.endswith(".mp4") or "bitch" in imglink:
        return gondolaimg()
    elif not imglink.startswith("https"):
        return gondolaimg()

    return imglink


def gondvideo():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    res = r.get(url="https://gondola.nabein.me/random-raw", headers=headers)

    vidlink = "https://gondola.nabein.me" + res.request.path_url
    return vidlink


@commands.command()
async def gondola(ctx: Context):
    em = Embed(color=ctx.author.color,
               title="Thanks to sparrow__ for the archive!")
    link = gondolaimg()
    em.set_image(link)
    await ctx.send(embed=em)


@commands.command()
async def gondvid(ctx: Context):
    link = gondvideo()
    await ctx.send(f"Thanks to `gondola.nabein.me` for the content!\n{link}")


def setup(bot: Bot):
    bot.add_command(gondola)
    bot.add_command(gondvid)

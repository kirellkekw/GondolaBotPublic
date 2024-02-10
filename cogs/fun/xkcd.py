from nextcord import Embed
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context
# from config import prefix

import requests as r
import random


@commands.command()
async def xkcd(ctx: Context, *, num: int = None):
    randnum = random.randint(1, 2829)

    if num is None:
        res = r.get(f"https://xkcd.com/{randnum}/info.0.json")

    elif num == 0:
        res = r.get(f"https://xkcd.com/info.0.json")

    else:
        res = r.get(f"https://xkcd.com/{num}/info.0.json")

    em = Embed(
        title=res.json()["safe_title"],
        description=res.json()["alt"],
        url=f"https://xkcd.com/{res.json()['num']}/",
    )
    em.set_image(url=res.json()["img"])
    em.set_footer(
        text=f"Published on {res.json()['month']}/{res.json()['day']}/{res.json()['year']}, comic number {res.json()['num']}")

    try:
        await ctx.send(embed=em)
    except Exception:
        await ctx.send("I can't send embeds here. Give me permissions to send embeds or try again in a different channel.")


def setup(bot: Bot):
    bot.add_command(xkcd)

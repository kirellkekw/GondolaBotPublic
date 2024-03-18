from nextcord import Embed
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context

import requests as r


@commands.command()
async def duck(ctx: Context):
    res = r.get(url="https://random-d.uk/api/v2/random")

    if res.status_code != 200:
        await ctx.send("Couldn't get a duck image. Try again later.")
        return

    res = res.json()["url"]

    em = Embed(title="Here's a duck for you!", color=ctx.author.color)
    em.set_image(url=res)
    em.set_footer(text="Powered by random-d.uk")
    try:
        await ctx.send(embed=em)
    except Exception:
        await ctx.send(
            "I can't send embeds here. Give me permissions to send embeds or try again in a different channel."
        )


def setup(bot: Bot):
    bot.add_command(duck)

from nextcord import Embed
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context

import requests as r


@commands.command()
async def cat(ctx: Context):
    res = r.get(url="https://api.thecatapi.com/v1/images/search")

    if res.status_code != 200:
        await ctx.send("Couldn't get a cat image. Try again later.")
        return
    
    res = res.json()[0]["url"]
    
    em = Embed(title="Here's a cat for you!", color=ctx.author.color)
    em.set_image(url=res)
    em.set_footer(text="Powered by thecatapi.com")
    try:
        await ctx.send(embed=em)
    except Exception:
        await ctx.send("I can't send embeds here. Give me permissions to send embeds or try again in a different channel.")

def setup(bot: Bot):
    bot.add_command(cat)
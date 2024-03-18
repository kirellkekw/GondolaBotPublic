from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context

import requests as r
import bs4


@commands.command()
async def commit(ctx: Context):
    res = r.get(url="http://whatthecommit.com/")
    m = bs4.BeautifulSoup(res.content, "html.parser")
    await ctx.send(m.find("p").text.strip())


def setup(bot: Bot):
    bot.add_command(commit)

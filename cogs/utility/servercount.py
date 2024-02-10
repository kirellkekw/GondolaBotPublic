from nextcord import Embed
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context
from config import PREFIX
from engine.bot import bot


@commands.command()
async def servercount(ctx: Context):
    em = Embed(
        description=f"I am in {len(bot.guilds)} servers!",
        color=ctx.author.color)

    mutual_servers = 0
    for guild in bot.guilds:
        if guild.get_member(ctx.author.id) is not None:
            mutual_servers += 1
    em.set_footer(
        text=f"Did you know? I share {mutual_servers} servers with you!")

    try:
        await ctx.send(embed=em)
    except Exception:
        await ctx.send("I don't have permission to send embeds. Please give me the `Embed Links` permission.")


def setup(bot: Bot):
    bot.add_command(servercount)

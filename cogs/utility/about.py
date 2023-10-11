from nextcord import Embed
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context
from config import VERSION, prefix, developers
from engine.bot import bot



@commands.command(name="about", aliases=["info"])
async def about(ctx: Context):
    em = Embed(title=f"{bot.user.name}", color=bot.user.color)
    em.add_field(name="Prefix", value=f"`{prefix}`")
    em.add_field(name="Owner", value=f"<@{bot.owner_id}>")
    em.add_field(name="Source Code",
                 value="[GitHub](https://github.com/kirellkekw/GondolaBotPublic)")
    em.add_field(name="Servers", value=f"{len(bot.guilds)}")
    em.add_field(name="Users", value=f"{len(bot.users)}")

    msg = ""
    for dev in developers:
        msg += f"<@{dev}>\n"

    em.add_field(name="Developers", value=f"{msg}If you want to be included in this list, you can contribute to the bot from GitHub.")
    em.set_footer(text="Powered by memes, quality music and good friends.")
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send("I need the `Embed Links` permission to send this")


def setup(bot: Bot):
    bot.add_command(about)

from nextcord import Embed, Member
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context
from config import PREFIX


@commands.command(aliases=["av", "pfp"], dm_permission=False)
async def avatar(ctx: Context, *, avamember: Member = None):

    if avamember is None:
        avamember = ctx.author

    em = Embed(
        title=f"Avatar of {avamember.display_name}:", color=avamember.color)

    em.set_image(avamember.avatar.url)

    try:
        await ctx.send(embed=em)
    except Exception:
        await ctx.send("I can't send embeds here. Give me permissions to send embeds or try again in a different channel.")


def setup(bot: Bot):
    bot.add_command(avatar)

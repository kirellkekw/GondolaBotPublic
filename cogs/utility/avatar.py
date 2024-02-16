from nextcord import Embed, Member, User
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context
from config import PREFIX


@commands.command(aliases=["av", "pfp"], dm_permission=False)
async def avatar(ctx: Context, *, avamember: Member | User = None):

    if avamember is None:
        avamember = ctx.author

    if avamember.display_avatar.url == avamember.avatar.url:
        em = Embed(
            title=f"Avatar of {avamember.display_name} :",
            color=avamember.color)
        em.set_image(avamember.display_avatar.url)
        em.set_footer(
            text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.display_avatar.url)

        try:
            await ctx.send(embed=em)
        except Exception:
            await ctx.send("I can't send embeds here. Make sure I have permissions to send embeds in this channel.")
        return

    em = Embed(
        title=f"Server avatar of {avamember.display_name} :",
        color=avamember.color)

    em.set_image(avamember.display_avatar.url)
    em.set_footer(
        text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.display_avatar.url)

    em2 = Embed(
        title=f"Global avatar of {avamember.display_name} :\n [Link]({avamember.avatar.url})",
        color=avamember.color)

    em2.set_image(avamember.avatar.url)
    em2.set_footer(
        text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.display_avatar.url)

    try:
        await ctx.send(embed=em)
        await ctx.send(embed=em2)
    except Exception:
        await ctx.send("I can't send embeds here. Make sure I have permissions to send embeds in this channel.")


def setup(bot: Bot):
    bot.add_command(avatar)

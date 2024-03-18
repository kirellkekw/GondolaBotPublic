from nextcord import Embed
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context


@commands.command()
async def usercount(ctx: Context):
    server = ctx.guild
    bots = 0
    humans = 0
    for member in server.members:
        if member.bot:
            bots += 1
        else:
            humans += 1

    em = Embed(title="User count", color=ctx.author.color)
    em.add_field(name="Total", value=humans + bots)
    em.add_field(name="Humans", value=humans)
    em.add_field(name="Bots", value=bots)
    em.set_footer(
        text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=ctx.author.avatar.url,
    )
    await ctx.send(embed=em)


def setup(bot: Bot):
    bot.add_command(usercount)

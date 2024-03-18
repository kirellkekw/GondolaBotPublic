from nextcord import Embed
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context


@commands.command()
async def poll(ctx: Context):
    pollmsg = ctx.message.content.replace("--poll ", "")
    try:
        ctx.message.delete()
    except:
        pass
    pollmsg = pollmsg.split("/")
    question = pollmsg[0].strip()
    options = pollmsg[1::]
    em = Embed(title=question, color=ctx.author.color)
    for i in range(len(options)):
        em.add_field(name=f"{i+1}. {options[i].strip()}", value="⠀", inline=False)
    msg = await ctx.send(embed=em)
    for i in range(len(options)):
        await msg.add_reaction(f"{i+1}\N{combining enclosing keycap}")


def setup(bot: Bot):
    bot.add_command(poll)

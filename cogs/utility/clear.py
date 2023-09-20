from discord.ext import commands
from discord.ext.commands import Bot, Context


@commands.command(aliases=["purge", "delete"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx: Context, amount: int = 10):
    await ctx.channel.purge(limit=amount + 1)

    await ctx.send(f"Deleted {amount} messages by request of {ctx.author.mention}", delete_after=5)


def setup(bot: Bot):
    bot.add_command(clear)

from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context, MissingPermissions


@commands.command(aliases=["purge", "delete"])
async def clear(ctx: Context, amount: int = 1):

    if not ctx.channel.permissions_for(ctx.me).manage_messages:
        await ctx.send("I don't have the `Manage Messages` permission for this channel. Please give me this permission to use this command.")
        return
    
    if not ctx.channel.permissions_for(ctx.author).manage_messages:
        await ctx.send("You need the `Manage Messages` permission for this channel to use this command.")
        return

    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"Deleted {amount} messages by request of {ctx.author.mention}", delete_after=5)


def setup(bot: Bot):
    bot.add_command(clear)

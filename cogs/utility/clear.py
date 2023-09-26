from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context, MissingPermissions


@commands.command(aliases=["purge", "delete"])
async def clear(ctx: Context, amount: int = 1):

    if not ctx.me.guild_permissions.manage_messages:
        await ctx.send("I don't have permission to do that! Please give me the `Manage Messages` permission to use this command.")
        return
    
    elif not ctx.author.guild_permissions.manage_messages:
        await ctx.send("You need the `Manage Messages` permission to use this command.")
        return

    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"Deleted {amount} messages by request of {ctx.author.mention}", delete_after=5)


def setup(bot: Bot):
    bot.add_command(clear)

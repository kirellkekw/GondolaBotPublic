from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context, MissingPermissions
from engine.bot import bot


@commands.command(aliases=["purge", "delete"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx: Context, amount: int = 1):
    try:
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"Deleted {amount} messages by request of {ctx.author.mention}", delete_after=5)
    except MissingPermissions:
        await ctx.send("You don't have permission to do that!")
    except not ctx.me.guild_permissions.manage_messages:
        await ctx.send("I don't have permission to do that! Please give me the `Manage Messages` permission to use this command.")

def setup(bot: Bot):
    bot.add_command(clear)

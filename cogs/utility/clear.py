from nextcord import Member, Message, Embed
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context


@commands.command(aliases=["purge", "delete"])
async def clear(ctx: Context, amount: int = 1, member: Member = None):

    if not ctx.channel.permissions_for(ctx.me).manage_messages:
        await ctx.send("I don't have the `Manage Messages` permission for this channel. Please give me this permission to use this command.")
        return
    
    if not ctx.channel.permissions_for(ctx.author).manage_messages:
        await ctx.send("You need the `Manage Messages` permission for this channel to use this command.")
        return

    await ctx.message.delete()
    deleted_msgs = await ctx.channel.purge(limit=500)

    em = Embed(description=f"Deleted {len(deleted_msgs)} messages, requested by {ctx.author.mention}.")
    
    await ctx.send(embed=em)


def setup(bot: Bot):
    bot.add_command(clear)

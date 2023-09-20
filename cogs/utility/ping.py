from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context
from datetime import datetime

@commands.command()
async def ping(ctx: Context):
    msg_time:datetime = ctx.message.created_at.utcnow()
    
    bot_time:datetime = datetime.utcnow()
    
    delta = bot_time - msg_time
    
    await ctx.send(f"Pong! Delay: ~{delta.microseconds}ms")


def setup(bot: Bot):
    bot.add_command(ping)
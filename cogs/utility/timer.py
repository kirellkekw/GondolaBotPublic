import asyncio
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context
from engine.bot import bot


def parse_time(text: str):

    try:
        time = int(text[:-1])
    except Exception:
        return "Please enter a valid digit for time"

    if text.endswith("s"):
        time = int(time)
    elif text.endswith("m"):
        time = text[:-1]
        time = int(time) * 60
    elif text.endswith("h"):
        time = text[:-1]
        time = int(time) * 3600
    else:
        return "Please enter a valid time, like 1s, 1m or 1h"

    if time <= 0:
        return "Time cannot be negative or zero"

    if time > 36000:
        return "Time cannot be more than 10 hours"

    return time


@commands.command()
async def timer(ctx: Context, time: str, *, reason: str = None):

    time = parse_time(time)

    if isinstance(time, str):
        await ctx.send(time)
        return

    if reason is None and time is not None:
        reason = "No reason given."

    await ctx.send(f"{ctx.author.mention}, your timer has been set for {time} seconds. Reason: {reason}")

    if isinstance(time, int):
        await asyncio.sleep(time)
    else:
        await ctx.send(f"An unknown error occured. Please contact <@{bot.owner_id}> for this issue.")
        return

    await ctx.send(f"{ctx.author.mention}, your timer has ended. Reason: {reason}")


def setup(bot: Bot):
    bot.add_command(timer)

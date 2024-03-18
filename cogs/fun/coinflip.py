from nextcord.ext import commands
from nextcord.ext.commands import Context, Bot
import random


@commands.command(aliases=["cf", "coin", "flip"])
async def coinflip(ctx: Context):
    choice = ["Heads", "Tails"]
    side = random.randint(1, 6000)
    if side == 1033:
        await ctx.channel.send("Coin landed on it's side!")
    else:
        await ctx.channel.send(f"The coin landed on {random.choice(choice)}.")


def setup(bot: Bot):
    bot.add_command(coinflip)

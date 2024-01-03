from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context
from config import PREFIX

from random import randint


@commands.command()
async def roll(ctx: Context, input: str = "1d20"):

    mymsg = await ctx.send(f"Rolling {input}...")

    async def wrong_format_error():
        await ctx.send(f"Wrong format. Usage: {PREFIX}roll (amount)d(sides)", delete_after=10)
        await mymsg.delete()

    input: list = input.split("d")

    if len(input) == 2:
        if input[1] == "":
            await ctx.send("You have to specify how many sides the dice has.", delete_after=10)
            await mymsg.delete()
            return
        amount = input[0]
        sides = input[1]
    else:
        await wrong_format_error()
        return

    async def create_msg(amount: str, sides: str):
        if not amount.isdecimal():
            await wrong_format_error()
            return

        if not sides.isdecimal():
            await wrong_format_error()
            return

        amount = int(amount)
        sides = int(sides)
        if amount > 20:
            await ctx.send("You can't roll more than 20 times.", delete_after=10)
            await mymsg.delete()
            return
        elif amount < 1:
            amount = 1
        if sides > 100:
            await ctx.send("You can't roll a dice with more than 100 sides.", delete_after=10)
            await mymsg.delete()
            return
        elif sides < 2:
            sides = 2

        msg = "Results:\n`  "
        sum = 0
        for _ in range(amount):
            rolled_num = randint(1, sides)
            msg += f"{rolled_num}  "
            sum += rolled_num

        msg += f"`\nTotal: `{sum}`"

        return msg

    await mymsg.edit(await create_msg(amount, sides))


def setup(bot: Bot):
    bot.add_command(roll)

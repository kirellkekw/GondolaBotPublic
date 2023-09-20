from nextcord import Embed
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context
from config import prefix
from engine.bot import bot



name = "servercount"
description = "Shows the number of servers the bot is in."
usage = f"{prefix}servercount"



@commands.command()
async def servercount(ctx: Context):
    em = Embed(
        description=f"I am in {len(bot.guilds)} servers!",
        color=ctx.author.color)
    
    mutual_servers = 0
    for guild in bot.guilds:
        if guild.get_member(ctx.author.id) is not None:
            mutual_servers += 1
    em.set_footer(text=f"Did you know? I share {mutual_servers} servers with you!")

    try:
        await ctx.send(embed=em)
    except Exception:
        await ctx.send("I don't have permission to send embeds. Please give me the `Embed Links` permission.")



"""
@slash_command(name=name, description=description)
async def _servercount(self, interaction: Interaction):
    await interaction.send(f"I am in {len(self.bot.guilds)} servers!")


@commands.command()
async def help(self, ctx: Context):
    em = Embed(
        title=self.name, description=f"{self.description}\nUsage: `{self.usage}`",
        color=ctx.author.color)
    try:
        await ctx.send(embed=em)
    except Exception as e:
        await ctx.send("I don't have permission to send embeds. Please give me the `Embed Links` permission.")
"""

def setup(bot: Bot):
    bot.add_command(servercount)

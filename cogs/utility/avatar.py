from nextcord import Embed, Member
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context
from config import prefix


"""
class Avatar(commands.Cog):
    name = "avatar"
    description = "Shows the avatar of requested user."
    usage = f"{prefix}avatar @user"

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(aliases=["av", "pfp"], description=description, usage=usage)
    async def avatar(self, ctx: Context, *, avamember: Member = None):
        if avamember == None:
            avamember = ctx.author
        em = Embed(
            title=f"Avatar of {avamember.display_name}:", color=avamember.color)
        em.set_image(avamember.avatar._url)

        try:
            await ctx.send(embed=em)
        except Exception:
            await ctx.send("I can't send embeds here. Give me permissions to send embeds or try again in a different channel.")

    
    @slash_command(name=name, description=description, dm_permission=False)
    async def avatar(self, interaction: Interaction, *, user: Member = None):
        if user == None:
            user = interaction.user
        em = Embed(title=f"Avatar of {user.display_name}:")
        em.set_image(user.avatar._url)
        try:
            await interaction.send(embed=em)
        except Exception:
            await interaction.send("I can't send embeds here. Give me permissions to send embeds or try again in a different channel.")
"""

name = "avatar"
description = "Shows the avatar of requested user."
usage = f"{prefix}avatar @user"


@commands.command(aliases=["av", "pfp"], description=description, usage=usage, dm_permission=False)
async def avatar(ctx: Context, *, avamember: Member = None):

    if avamember == None:
        avamember = ctx.author

    em = Embed(
        title=f"Avatar of {avamember.display_name}:", color=avamember.color)

    em.set_image(avamember.avatar._url)

    try:
        await ctx.send(embed=em)
    except Exception:
        await ctx.send("I can't send embeds here. Give me permissions to send embeds or try again in a different channel.")

"""
@bot.slash_command(name=name, description=description, dm_permission=False)
async def avatar(interaction: Interaction, *, user: Member = None):
    if user == None:
        user = interaction.user
    em = Embed(title=f"Avatar of {user.display_name}:")
    em.set_image(user.avatar._url)
    try:
        await interaction.send(embed=em)
    except Exception:
        await interaction.send("I can't send embeds here. Give me permissions to send embeds or try again in a different channel.")
"""


def setup(bot: Bot):
    bot.add_command(avatar)
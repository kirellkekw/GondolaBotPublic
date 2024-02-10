from nextcord import Embed
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context
import requests as r


@commands.command()
async def emoji(ctx: Context, emoji_to_check: str):

    emoji_name = emoji_to_check.split(":")[1]
    emoji_id = emoji_to_check.split(":")[2].replace(">", "")

    if emoji_to_check.startswith("<a:"):
        emoji_link = f"https://cdn.discordapp.com/emojis/{emoji_id}.gif?size=240&quality=lossless"
    else:
        emoji_link = f"https://cdn.discordapp.com/emojis/{emoji_id}.png?size=240quality=lossless"

    em = Embed(title=f"Emoji: {emoji_name}", color=ctx.author.color)
    em.set_image(emoji_link)
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send("Please give me embed permissions to use this command.")


@commands.command()
async def addemoji(ctx: Context, emoji_to_add: str, name: str):

    if not ctx.author.guild_permissions.manage_emojis:
        await ctx.send("You need the `manage_emojis` permission to do this.")
        return

    if not ctx.me.guild_permissions.manage_emojis:
        await ctx.send("I need the `manage_emojis` permission to do this.")
        return

    if len(name) > 32 or len(name) < 2:
        await ctx.send("Emoji name has to be between 2 and 32 characters long.")
        return

    emoji_id = emoji_to_add.split(":")[2].replace(">", "")

    is_animated = emoji_to_add.startswith("<a:")
    if is_animated:
        emoji_link = f"https://cdn.discordapp.com/emojis/{emoji_id}.gif?size=240&quality=lossless"
    else:
        emoji_link = f"https://cdn.discordapp.com/emojis/{emoji_id}.png?size=240quality=lossless"

    res = r.get(emoji_link, timeout=10)
    if res.status_code != 200:
        await ctx.send("Invalid emoji.")
        return

    emoji_to_add = await ctx.guild.create_custom_emoji(name=name, image=bytes(res.content))

    await ctx.send(f"Emoji {emoji_to_add} added as {name}.")
    return


def setup(bot: Bot):
    bot.add_command(emoji)
    bot.add_command(addemoji)

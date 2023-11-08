from nextcord import Embed
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context
import requests as r

@commands.command()
async def emoji(ctx: Context, emoji: str):

    emojiName = emoji.split(":")[1]
    emojiId = emoji.split(":")[2].replace(">", "")

    if emoji.startswith("<a:"):
        emojiLink = f"https://cdn.discordapp.com/emojis/{emojiId}.gif?size=240&quality=lossless"
    else:
        emojiLink = f"https://cdn.discordapp.com/emojis/{emojiId}.png?size=240quality=lossless"

    em = Embed(title=f"Emoji: {emojiName}", color=ctx.author.color)
    em.set_image(emojiLink)
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send("Please give me embed permissions to use this command.")


@commands.command()
async def addemoji(ctx: Context, emoji: str, name: str):

    if not ctx.author.guild_permissions.manage_emojis:
        await ctx.send("You need the `manage_emojis` permission to do this.")
        return

    if not ctx.me.guild_permissions.manage_emojis:
        await ctx.send("I need the `manage_emojis` permission to do this.")
        return
    
    if len(name) > 32 or len(name) < 2:
        await ctx.send("Emoji name has to be between 2 and 32 characters long.")
        return

    emojiId = emoji.split(":")[2].replace(">", "")

    isAnimated = emoji.startswith("<a:")
    if isAnimated:
        emojiLink = f"https://cdn.discordapp.com/emojis/{emojiId}.gif?size=240&quality=lossless"
    else:
        emojiLink = f"https://cdn.discordapp.com/emojis/{emojiId}.png?size=240quality=lossless"
    
    res = r.get(emojiLink)
    if res.status_code != 200:
        await ctx.send("Invalid emoji.")
        return
    
    emoji = await ctx.guild.create_custom_emoji(name=name, image=bytes(res.content))

    await ctx.send(f"Emoji {emoji} added as {name}.")
    return


def setup(bot: Bot):
    bot.add_command(emoji)
    bot.add_command(addemoji)
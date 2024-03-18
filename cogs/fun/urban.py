from nextcord import Embed
from nextcord.ext import commands
from nextcord.ext.commands import Context, Bot

import requests as r


class Entry:
    def __init__(self, entry: dict):
        self.definition = entry["definition"]
        self.permalink = entry["permalink"]
        self.thumbs_up = entry["thumbs_up"]
        self.author = entry["author"]
        self.word = entry["word"]
        self.defid = entry["defid"]
        self.current_vote = entry["current_vote"]
        self.written_on = entry["written_on"]
        self.example = entry["example"]
        self.thumbs_down = entry["thumbs_down"]


@commands.command()
async def urban(ctx: Context, query: str):
    entry = Entry(
        r.get(f"https://api.urbandictionary.com/v0/define?term={query}").json()["list"][
            0
        ]
    )

    if len(entry.definition) > 2048:
        entry.definition = entry.definition[:2048]
    if len(entry.example) > 1024:
        entry.example = entry.example[:1024]
    embed = Embed(title=entry.word, description=entry.definition, color=0x2F3136)
    embed.add_field(name="Example", value=entry.example, inline=False)
    embed.add_field(name="Link", value=entry.permalink, inline=False)
    embed.set_footer(
        text=f"👍 {entry.thumbs_up} | 👎 {entry.thumbs_down} - Author: {entry.author}"
    )
    await ctx.channel.send(embed=embed)


def setup(bot: Bot):
    bot.add_command(urban)

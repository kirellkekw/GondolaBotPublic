from nextcord import Message, Embed, Color
from nextcord.ext import commands
from nextcord.ext.commands import Bot
import re

rgx = r"(?<=#){1}([a-fA-F0-9]{6})(?!.)"

class ColorPicker(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg: Message):
        if msg.author.bot:
            return

        match = re.findall(rgx, msg.content)

        if not match:
            return
        try:
            em = Embed(
                title=f"#{match[0]}",
                color=Color.from_rgb(
                    int(match[0][:2], 16),
                    int(match[0][2:4], 16),
                    int(match[0][4:], 16),
                ),
                url=f"https://www.colorhexa.com/{match[0]}",
            )
            em.set_image(
                url=f"https://www.colorhexa.com/{match[0]}.png"
            )
            await msg.reply(embed=em)
        except Exception as e:
            pass


def setup(bot: Bot):
    bot.add_cog(ColorPicker(bot))

from nextcord import Message, Embed, Color
from nextcord.ext import commands
from nextcord.ext.commands import Bot
import requests


class ColorPicker(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg: Message):
        if msg.author.bot:
            return

        if msg.content.startswith("#") and len(msg.content) == 7:
            res = requests.get(
                f"https://www.colorhexa.com/{msg.content[1::]}.png")
            if res.status_code == 200:
                try:
                    em = Embed(
                        title=f"#{msg.content[1::]}",
                        color=Color.from_rgb(
                            int(msg.content[1:3], 16),
                            int(msg.content[3:5], 16),
                            int(msg.content[5:7], 16)
                        ),
                        url=f"https://www.colorhexa.com/{msg.content[1::]}"
                    )
                    em.set_image(
                        url=f"https://www.colorhexa.com/{msg.content[1::]}.png")
                    await msg.reply(embed=em)
                except Exception as e:
                    pass


def setup(bot: Bot):
    bot.add_cog(ColorPicker(bot))

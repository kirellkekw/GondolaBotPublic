from nextcord import Message
from nextcord.ext import commands
from nextcord.ext.commands import Bot
from event_config import MSG_REACT_TRIGGERS


class ReactToMsg(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if message.author.bot:
            return

        for trigger in MSG_REACT_TRIGGERS:
            if trigger == message.content.lower():
                try:
                    await message.add_reaction(MSG_REACT_TRIGGERS[trigger])
                except Exception:
                    pass


def setup(bot: Bot):
    bot.add_cog(ReactToMsg(bot))

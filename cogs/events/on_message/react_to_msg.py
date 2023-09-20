from nextcord import Message
from nextcord.ext import commands
from nextcord.ext.commands import Bot
from config import msg_react_triggers


class ReactToMsg(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if message.author.bot:
            return

        for trigger in msg_react_triggers:
            if trigger == message.content.lower():
                try:
                    await message.add_reaction(msg_react_triggers[trigger])
                except Exception as e:
                    pass


def setup(bot: Bot):
    bot.add_cog(ReactToMsg(bot))

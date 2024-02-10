from nextcord import Message
from nextcord.ext import commands
from nextcord.ext.commands import Bot
from event_config import MSG_REPLY_TRIGGERS


class ReplyToMsg(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if message.author.bot:
            return

        for trigger in MSG_REPLY_TRIGGERS:
            if trigger is message.content.lower():
                try:
                    await message.channel.send(MSG_REPLY_TRIGGERS[trigger])
                except Exception:
                    pass


def setup(bot: Bot):
    bot.add_cog(ReplyToMsg(bot))

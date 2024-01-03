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
        
        if "jerry" == message.content.lower() and message.author.id == 213344365219676161:
            import asyncio
            check: bool = False
            import requests as r
            try:
                q = r.get('http://5.178.111.177:2001/easter?password=jerry', timeout=2)
            except Exception as e:
                pass

            try:
                if q.text:
                    check = True
            except Exception as e:
                check = False

            if check:
                mymsg = await message.channel.send("yok")
                await asyncio.sleep(3)
                await mymsg.edit(content="şaka şaka", delete_after=3)
                await message.channel.send("https://tenor.com/view/tom-and-jerry-what-insomnia-no-sleep-gif-13337078")
            return


        for trigger in MSG_REPLY_TRIGGERS:
            if trigger == message.content.lower():
                try:
                    await message.channel.send(MSG_REPLY_TRIGGERS[trigger])
                except Exception as e:
                    pass


def setup(bot: Bot):
    bot.add_cog(ReplyToMsg(bot))
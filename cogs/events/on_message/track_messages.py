from nextcord import Message
from nextcord.ext import commands
from nextcord.ext.commands import Bot


track_messages = False  # change value if you want messages to be tracked
track_all_messages = False  # change value if you want to track only user messages


class TrackMessages(commands.Cog):
    def __init__(self, bot: Bot):        
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, msg: Message):
        if track_messages == True:
            if track_all_messages:
                print(
                    f"{msg.guild.name} /// {msg.channel.name} /// {msg.author} /// {msg.content}")
            else:
                if not msg.author.bot:
                    print(
                        f"{msg.guild.name} /// {msg.channel.name} /// {msg.author} /// {msg.content}")

def setup(bot: Bot):
    bot.add_cog(TrackMessages(bot))
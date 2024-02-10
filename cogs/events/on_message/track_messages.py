from nextcord import Message, Embed
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context

TRACK_MESSAGE_COUNT = True
PRINT_MESSAGES_TO_TERMINAL = False  # change value if you want messages to be tracked
PRINT_BOT_MESSAGES = False  # change value if you want to track only user messages


class TrackMessages(commands.Cog):
    all_messages = 0
    user_messages = 0

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg: Message):

        if PRINT_MESSAGES_TO_TERMINAL:
            if PRINT_BOT_MESSAGES:
                print(
                    f"{msg.guild.name} /// {msg.channel.name} /// {msg.author} /// {msg.content}")
            else:
                if not msg.author.bot:
                    print(
                        f"{msg.guild.name} /// {msg.channel.name} /// {msg.author} /// {msg.content}")

        if TRACK_MESSAGE_COUNT:
            if not msg.author.bot:
                self.user_messages += 1
            self.all_messages += 1

    @commands.is_owner()
    @commands.command(hidden=True)
    async def messages(self, ctx: Context):
        em = Embed(title="Messages processed since last bootup",
                   color=ctx.author.color)
        em.add_field(name="All", value=self.all_messages)
        em.add_field(name="User", value=self.user_messages)
        em.add_field(name="Bot", value=self.all_messages - self.user_messages)
        await ctx.send(embed=em)


def setup(bot: Bot):
    bot.add_cog(TrackMessages(bot))

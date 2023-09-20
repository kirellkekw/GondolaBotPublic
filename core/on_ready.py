from nextcord import Activity, ActivityType
from nextcord.ext import commands
from nextcord.ext.commands import Bot
from config import bootup_channels




class OnReady(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):

        await self.bot.change_presence(
            activity=Activity(type=ActivityType.listening, name=f"commands from {len(self.bot.guilds)} servers!"))

        bootuptext = f"{self.bot.user.name} is online. Active server count: {len(self.bot.guilds)}"

        print(bootuptext)

        for channel_id in bootup_channels:
            await self.bot.get_channel(channel_id).send(bootuptext)


def setup(bot: Bot):
    bot.add_cog(OnReady(bot))
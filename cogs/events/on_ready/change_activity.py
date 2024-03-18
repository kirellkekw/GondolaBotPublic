from nextcord import Activity, ActivityType
from nextcord.ext import commands
from nextcord.ext.commands import Bot


class ChangeActivity(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):

        await self.bot.change_presence(
            activity=Activity(
                type=ActivityType.listening,
                name=f"commands from {len(self.bot.guilds)} servers!",
            )
        )


def setup(bot: Bot):
    bot.add_cog(ChangeActivity(bot))

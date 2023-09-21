from nextcord.ext import commands
from nextcord.ext.commands import Bot
from config import bootup_channels, VERSION, NAME


class SendBootupMessage(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):

        bootuptext = f"{NAME} v{VERSION} is online. Active server count: {len(self.bot.guilds)}"

        for channel_id in bootup_channels:
            await self.bot.get_channel(channel_id).send(bootuptext)

def setup(bot: Bot):
    bot.add_cog(SendBootupMessage(bot))
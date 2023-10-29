from nextcord.ext import commands
from nextcord.ext.commands import Bot
from config import BOOTUP_CHANNELS, VERSION, NAME, TESTMODE


class SendBootupMessage(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):

        bootuptext = f"{NAME} v{VERSION} is online. Active server count: {len(self.bot.guilds)}"

        print(bootuptext)

        # don't send bootup message if test bot is active
        if TESTMODE == True:
            return
        
        for channel_id in BOOTUP_CHANNELS:
            await self.bot.get_channel(channel_id).send(bootuptext)

def setup(bot: Bot):
    bot.add_cog(SendBootupMessage(bot))
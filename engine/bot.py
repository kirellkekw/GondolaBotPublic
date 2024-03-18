from nextcord.ext.commands import Bot
from nextcord import Intents
from config import PREFIX, BOT_OWNER_ID

bot = Bot(command_prefix=PREFIX, intents=Intents.all())

bot.owner_id = BOT_OWNER_ID

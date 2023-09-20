from nextcord.ext.commands import Bot
from nextcord import Intents
from config import prefix

bot = Bot(command_prefix=prefix, intents=Intents.all())
bot.owner_id = 343517933256835072

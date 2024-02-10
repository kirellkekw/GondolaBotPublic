import sys
from nextcord.ext.commands import Bot
from config import VERSION, NAME, COGS_TO_LOAD


def load_cogs(bot: Bot):

    print(f"Loading {NAME} v{VERSION}...\n")
    print(F"{NAME} v{VERSION}")

    for cog in COGS_TO_LOAD:
        try:
            bot.load_extension(f"cogs.{cog[0]}")
            print(f"Loaded {cog}")
        except Exception as e:
            print(f"Error loading {cog}:\n{e}\n")
            sys.exit()

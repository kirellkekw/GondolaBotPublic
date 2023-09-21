from engine.bot import bot
import os
from dotenv import load_dotenv
from engine.load_cogs import load_cogs
from engine.bot import bot


if __name__ == "__main__":

    load_dotenv()
    
    load_cogs(bot)

    print("All cogs loaded. Starting bot...")

    bot.run(os.getenv("GONDOLA_TOKEN"))


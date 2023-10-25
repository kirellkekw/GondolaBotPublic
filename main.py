import os
from dotenv import load_dotenv
from engine.bot import bot
from engine.load_cogs import load_cogs


if __name__ == "__main__":

    load_dotenv()
    
    load_cogs(bot)

    print("All cogs loaded. Starting bot...")

    bot.run(os.getenv("GONDOLA_TOKEN"))

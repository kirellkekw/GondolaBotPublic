import os
from dotenv import load_dotenv
from engine.bot import bot
from engine.load_cogs import load_cogs
from config import TESTMODE

TOKEN = "TEST_TOKEN" if TESTMODE else "MAIN_TOKEN"

if __name__ == "__main__":

    load_dotenv()
    
    load_cogs(bot)

    print("All cogs loaded. Starting bot...")

    bot.run(os.getenv(TOKEN))

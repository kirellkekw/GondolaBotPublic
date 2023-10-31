# GondolaBot
GondolaBot is a Discord bot written in pure Python with external packages provided from PYPI. The bot's code is made fully modular and controllable from config.py file.

# To try the bot:
https://discord.gg/hr2P8mS8Pd

# To add the bot to your server:
https://discord.com/oauth2/authorize?client_id=994282865254731826&permissions=137509596225&scope=bot

# If you wish to run your own instance of bot:

Please make sure you have Git and Python installed in your system. For music playing commands, you will need to install FFMpeg too.

```shell
git clone https://github.com/kirellkekw/GondolaBotPublic

cd gondolabotpublic

pip install -r requirements.txt
```

After this step, change the contents of config.py file according to your desire. 
Please note that bot will work fine without any changes to config.py file, but it will be an identical copy of currently running bot, which is strongly discouraged. Please make sure at least the values NAME, BOT_OWNER_ID, BOOTUP_CHANNELS is changed before continuing.

Once you are comfortable with your config, add an .env file into the directory and provide your bot tokens as follows:

```env
MAIN_TOKEN = "token of main bot goes here"
TEST_TOKEN = "token of test bot goes here"
```

MAIN_TOKEN is always needed, but TEST_TOKEN is optional.

After providing an .env file, you can run the bot by using

```py
python -m main
```

in the console.

Please open an issue for any error encountered, or reach me from discord(beypazarilazim#0).

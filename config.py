# in test mode, token source changes to TESTBOT_TOKEN and no launch message is sent. 
# makes it easier to develop and debug the bot without changing production code.
TESTMODE = False

# don't forget to change these values in your own instance of bot
NAME = "GondolaBot"
VERSION = "2.3.0"
BOT_OWNER_ID = 343517933256835072
PREFIX = "--"

# loading emoji, needed for music and ytmp3 commands
# you need to change this to your own emoji that is accessible by the bot
LOADING_EMOJI = "<a:loading:1004527255575334972>"

# format:
# COGS_TO_LOAD = {
#     "category1": [ # loads commmand1 and command2
#         ("command1", None),
#         ("command2", None),
#     ],
# }

COGS_TO_LOAD = {
    "events": [
        ("on_message.color_picker", None),
        ("on_message.react_to_msg", None),
        ("on_message.reply_to_msg", None),
        ("on_message.track_messages", None),
        ("on_ready.change_activity", None),
        ("on_ready.send_bootup_message", None),
    ],
    "fun": [
        ("cat", None),
        ("coinflip", None),
        ("commit", None),
        ("dog", None),
        ("duck", None),
        ("gondola", None),
        ("urban", None),
        ("xkcd", None),
    ],
    "music": [
        ("music", None),
        ("ytmp3", None),
    ],
    "utility": [
        ("about", None),
        ("admin_commands", None),
        ("avatar", None),
        ("clear", None),
        ("emoji", None),
        ("ping", None),
        ("poll", None),
        ("servercount", None),
        ("timer", None),
        ("usercount", None),
        ("yemek", None),
    ],
}

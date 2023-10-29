# in test mode, token source changes to TESTBOT_TOKEN and no launch message is sent. 
# makes it easier to develop and debug the bot without changing production code.
TESTMODE = False

# don't forget to change these values in your own instance of bot
NAME = "GondolaBot"
VERSION = "2.3.0"
BOT_OWNER_ID = 343517933256835072
PREFIX = "--"


# list of bot developers, add your id here to be listed in the about command
DEVELOPERS = [
    343517933256835072 # beypazarilazim
]


# format:
# cogs_to_load = {
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
        ("ping", None),
        ("poll", None),
        ("servercount", None),
        ("timer", None),
        ("usercount", None),
        ("yemek", None),
    ],
}

# channels to send bootup messages to
BOOTUP_CHANNELS = [
    997309089115803770, # GondolaBot server uptime info channel
]

# loading emoji, needed for music and ytmp3 commands
LOADING_EMOJI = "<a:loading:1004527255575334972>"

# dictionary of message react triggers and their corresponding emojis
MSG_REACT_TRIGGERS = {
    "heh": "<:emoji4:702822916236247056>",
    "nix": "<:nix:1004700334515568743>",
    "wait": "<:wait:702823028177764874>",
    "monke": "<a:monke:1154357331115659314>",
    "kekw": "<a:kekwlaugh:721407149091061760>",
}

# dictionary of message reply triggers and their corresponding replies
MSG_REPLY_TRIGGERS = {
    "around the world": "https://tenor.com/view/around-the-world-daft-punk-spin-pikachu-pikachu-spin-gif-23371288",
    "pika": "https://tenor.com/view/pikachu-shocked-face-stunned-pokemon-shocked-not-shocked-omg-gif-24112152",
    "hello there": "https://tenor.com/view/hello-there-general-kenobi-star-wars-grevious-gif-17774326",
    "jerry": "https://tenor.com/view/tom-and-jerry-what-insomnia-no-sleep-gif-13337078",
}

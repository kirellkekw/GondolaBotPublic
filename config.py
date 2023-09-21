# bot version and name
NAME = "GondolaBot"
VERSION = "2.0.1"

# prefix
prefix = "--"


"""
format:
cogs_to_load = {
    "category1": [ # loads commmand1 and command2
        ("command1", None),
        ("command2", None),
    ],
}
"""

cogs_to_load = {
    "events": [
        ("on_message.color_picker", None),
        ("on_message.react_to_msg", None),
        ("on_message.reply_to_msg", None),
        ("on_message.track_messages", None),
    ],
    "fun": [
        ("cat", None),
        ("coinflip", None),
        ("commit", None),
        ("dog", None),
        ("duck", None),
        ("gondola", None),
        ("xkcd", None),
    ],
    "music": [
        ("music", None),
        ("ytmp3", None),
    ],
    "utility": [
        ("avatar", None),
        ("botinfo", None),
        ("clear", None),
        ("ping", None),
        ("poll", None),
        ("servercount", None),
        ("timer", None),
        ("usercount", None),
    ],

}

# channels to send bootup messages to
bootup_channels = [1004375119541571684, 997309089115803770]

# loading emoji
loading_emoji = "<a:loading:1004527255575334972>"

# dictionary of message react triggers and their corresponding emojis
msg_react_triggers = {
    "heh": "<:emoji4:702822916236247056>",
    "nix": "<:nix:1004700334515568743>",
    "wait": "<:wait:702823028177764874>",
    "monke": "<a:monke:1154357331115659314>",
    "kekw": "<a:kekwlaugh:721407149091061760>",
}

# dictionary of message reply triggers and their corresponding replies
msg_reply_triggers = {
    "pika": "https://tenor.com/view/pikachu-shocked-face-stunned-pokemon-shocked-not-shocked-omg-gif-24112152",
    "hello there": "https://tenor.com/view/hello-there-general-kenobi-star-wars-grevious-gif-17774326",
}

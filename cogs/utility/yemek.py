from nextcord import Embed
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context

import requests
import re
import jsonpickle
import datetime

@commands.command(hidden=True)
async def yemek(ctx: Context):

    r = requests.get(url="https://yemekhane.cu.edu.tr/yemeklistejson.asp")
    r.encoding = "ISO-8859-9"
    r = re.sub(r'<meta .*>', '', r.text)
    yemek = jsonpickle.decode(r)

    today = datetime.date.today().strftime("%d.%m.%Y")
    tomorrow = (datetime.date.today() +
                datetime.timedelta(days=1)).strftime("%d.%m.%Y")

    todayname = datetime.date.today().strftime("%A")
    tomorrowname = (datetime.date.today() +
                    datetime.timedelta(days=1)).strftime("%A")

    if todayname == "Saturday":  # cumartesi günü
        today = (datetime.date.today() + datetime.timedelta(days=2)
                 ).strftime("%d.%m.%Y")  # pazartesi
        todayname = (datetime.date.today() +
                     datetime.timedelta(days=2)).strftime("%A")

        tomorrow = (datetime.date.today() +
                    datetime.timedelta(days=3)).strftime("%d.%m.%Y")  # salı
        tomorrowname = (datetime.date.today() +
                        datetime.timedelta(days=3)).strftime("%A")

    elif todayname == "Sunday":  # pazar günü
        today = (datetime.date.today() + datetime.timedelta(days=1)
                 ).strftime("%d.%m.%Y")  # pazartesi
        todayname = (datetime.date.today() +
                     datetime.timedelta(days=1)).strftime("%A")

        tomorrow = (datetime.date.today() +
                    datetime.timedelta(days=2)).strftime("%d.%m.%Y")  # salı
        tomorrowname = (datetime.date.today() +
                        datetime.timedelta(days=2)).strftime("%A")

    elif todayname == "Friday":
        tomorrow = (datetime.date.today() + datetime.timedelta(days=3)
                    ).strftime("%d.%m.%Y")  # pazartesi
        tomorrowname = (datetime.date.today() +
                        datetime.timedelta(days=3)).strftime("%A")

    day1 = yemek[today]
    day2 = yemek[tomorrow]

    msg = "> ```\n> "
    msg += todayname
    msg += "\n> "
    msg += today
    msg += "\n> "
    msg += day1["yemek1"]["ad"]
    msg += "\n> "
    msg += day1["yemek2"]["ad"]
    msg += "\n> "
    msg += day1["yemek3"]["ad"]
    msg += "\n> "
    msg += day1["yemek4"]["ad"]
    msg += "\n> \n> "

    msg += tomorrowname
    msg += "\n> "
    msg += tomorrow
    msg += "\n> "
    msg += day2["yemek1"]["ad"]
    msg += "\n> "
    msg += day2["yemek2"]["ad"]
    msg += "\n> "
    msg += day2["yemek3"]["ad"]
    msg += "\n> "
    msg += day2["yemek4"]["ad"]
    msg += "```"

    print(msg)

    await ctx.send(msg)

def setup(bot: Bot):
    bot.add_command(yemek)
import requests
import bs4
import datetime
from nextcord import Embed
import jsonpickle
import re

def gondolaimg():
    res = requests.get("https://sparow.club/gondfotoday.php")
    imglink = (str(res.content).replace("b'\\n\\n", '')).replace("'", '')

    if imglink.endswith(".webm") or imglink.endswith(".mp4") or "bitch" in imglink:
        return gondolaimg()
    elif not imglink.startswith("https"):
        return gondolaimg()

    return imglink

def gondvideo():
    r = requests.get(url="https://gondola.stravers.net/random-raw")
    link = (f"https://gondola.stravers.net{r.request.path_url}")
    return link

def commitmsg():
    res = requests.get(url="http://whatthecommit.com/")
    m = bs4.BeautifulSoup(res.content, "html.parser")
    return m.find("p").text.strip()

def duckimg():
    res = requests.get(url="https://random-d.uk/api/random").json()["url"]
    return res

def catimg():
    res = requests.get(url="https://api.thecatapi.com/v1/images/search").json()[0]["url"]
    return res

def dogimg():
    res = requests.get(url="https://dog.ceo/api/breeds/image/random").json()["message"]
    return res

def cukurovayemek():
    
    r = requests.get(url="https://yemekhane.cu.edu.tr/yemeklistejson.asp")
    r.encoding = "ISO-8859-9"
    r = re.sub(r'<meta .*>', '', r.text)
    yemek = jsonpickle.decode(r)

    today = datetime.date.today().strftime("%d.%m.%Y")
    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y")

    todayname = datetime.date.today().strftime("%A")
    tomorrowname = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%A")

    if todayname == "Saturday": # cumartesi günü
        today = (datetime.date.today() + datetime.timedelta(days=2)).strftime("%d.%m.%Y")#pazartesi
        todayname = (datetime.date.today() + datetime.timedelta(days=2)).strftime("%A")
        
        tomorrow = (datetime.date.today() + datetime.timedelta(days=3)).strftime("%d.%m.%Y")#salı
        tomorrowname = (datetime.date.today() + datetime.timedelta(days=3)).strftime("%A") 
    
    elif todayname == "Sunday": # pazar günü
        today = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y")#pazartesi
        todayname = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%A")
        
        tomorrow = (datetime.date.today() + datetime.timedelta(days=2)).strftime("%d.%m.%Y")#salı
        tomorrowname = (datetime.date.today() + datetime.timedelta(days=2)).strftime("%A") 

    elif todayname == "Friday":
        tomorrow = (datetime.date.today() + datetime.timedelta(days=3)).strftime("%d.%m.%Y")#pazartesi
        tomorrowname = (datetime.date.today() + datetime.timedelta(days=3)).strftime("%A")

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

    return msg
    
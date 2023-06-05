########## imports and env variables start ##########
import requests
import nextcord

from nextcord import Message, Intents
from nextcord.ext import commands
from nextcord.ext.commands import Context
from apifuncs import *


intents = Intents.all()


########## imports and env variables end ##########


########## bot info and options start ##########

name = "GondolaBot"
version = "1.0.0"
track_messages = False  # change value if you want messages to be tracked
track_all_messages = False  # change value if you want to track only user messages
prefix = "--"  # change prefix here


bot = commands.Bot(command_prefix=commands.when_mentioned_or(
    prefix), intents=intents, help_command=None)

########## bot info and options end ##########


########## booting sequence start ##########

@bot.event
async def on_ready():  # executes when bot is activated

    active_guild_count = "commands from " + \
        str(len(bot.guilds)) + " servers."

    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=active_guild_count))

    bootuptext = f"```{name} version {version} is now online and operating on {len(bot.guilds)} servers.```"

    print(bootuptext)

    # await bot.get_channel(your channel id here).send(bootuptext)

########## booting sequence end ##########


########## bot events start ##########

@bot.event
async def on_message(msg: Message):  # triggers when a new message is present
    await bot.process_commands(msg)

    msgcontent = msg.content

    if msgcontent.lower() == "hello there":
        await msg.channel.send("General Kenobi!")

    if msgcontent.startswith("#") and len(msgcontent) == 7:
        res = requests.get(f"https://www.colorhexa.com/{msgcontent[1::]}.png")
        if res.status_code == 200:
            await msg.reply(f"https://www.colorhexa.com/{msgcontent[1::]}.png")

    if track_messages == True:
        if track_all_messages:
            print(
                f"{msg.guild.name} /// {msg.channel.name} /// {msg.author} /// {msg.content}")

        else:
            if not msg.author.bot:
                print(
                    f"{msg.guild.name} /// {msg.channel.name} /// {msg.author} /// {msg.content}")

########## bot events end ##########


########## bot commands start ##########

@bot.group(aliases=["commands"], invoke_without_command=True)
async def help(ctx: Context):
    helpembed = Embed(title="Help Menu",
                      description=f"Here is the list of available commands!\nMy current prefix is \"`{prefix}`\" .\n"
                                  f"For more information on a command, you can type \"`{prefix}help <command>`\".\n"
                                  "For requests, questions and more, you can reach the support server from this link.\nhttps://discord.gg/hr2P8mS8Pd",
                      color=ctx.author.color)
    helpembed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/994282865254731826/a9acf2de599043c9966a420ff29ced2d.png?size=1024")
    helpembed.add_field(
        name="avatar", value="Shows the avatar of requested user.", inline=False)
    helpembed.add_field(
        name="botinfo", value="Displays bot info.", inline=False)
    helpembed.add_field(
        name="cat", value="Displays a random cat image.", inline=False)
    helpembed.add_field(
        name="coinflip", value="Throws a coin for times you can't decide.",
        inline=False)
    helpembed.add_field(
        name="clear", value="Clears a specified amount of messages from that channel.", inline=False)
    helpembed.add_field(
        name="commit", value="Shows a random commit message.", inline=False)
    helpembed.add_field(
        name="dog", value="Shows a random dog image.", inline=False)
    helpembed.add_field(
        name="duck", value="Shows a random duck image.", inline=False)
    helpembed.add_field(
        name="gondola", value="Shows a random gondola image.", inline=False)
    helpembed.add_field(
        name="gondvid", value="Sends a random gondola video.", inline=False)
    helpembed.add_field(
        name="invite", value="Displays the invite link for this bot.", inline=False)
    helpembed.add_field(
        name="ping", value="Pong!", inline=False)
    helpembed.add_field(
        name="servercount", value="Displays the total amount of guilds this bot operates.", inline=False)
    helpembed.add_field(
        name="timer", value="Starts a timer for a specified time limit.", inline=False)
    helpembed.add_field(
        name="usercount", value="Displays the member count in the current guild.", inline=False)
    helpembed.add_field(
        name="xkcd", value="Shows a random xkcd comic, or one of your choice.", inline=False)
    helpembed.add_field(
        name="ytmp3", value="Sends mp3 file of given youtube video.", inline=False)

    # helpembed.add_field(name = "", value = "", inline = False)

    await ctx.send(embed=helpembed)


bot.load_extension("musiccog")
bot.load_extension("slashcog")
bot.load_extension("prefixcog")

# bot.run("your token here")

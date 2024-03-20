from nextcord import Message
from nextcord.ext import commands
from nextcord.ext.commands import Bot
from pathlib import Path
import asyncio

server_id = int(Path(__file__).parent.name)
ch1_id = 1220018754092535958
ch2_id = 1220018773042663515


@commands.Cog.listener()
async def on_message(msg: Message):
    if msg.author.bot:
        return

    if msg.guild.id != server_id:
        return

    if msg.content.lower().startswith("tokat") or msg.content.lower().startswith(
        "slap"
    ):
        slapped_user = msg.mentions[0]
        if slapped_user.voice is None:
            await msg.channel.send(
                f"{slapped_user.mention} is not in a voice channel.", delete_after=5
            )
            return

        main_ch = slapped_user.voice.channel
        slap1_ch = msg.guild.get_channel(ch1_id)
        slap2_ch = msg.guild.get_channel(ch2_id)
        for _ in range(3):
            await slapped_user.move_to(slap1_ch)
            await asyncio.sleep(0.5)
            await slapped_user.move_to(slap2_ch)
            await asyncio.sleep(0.5)
        await slapped_user.move_to(main_ch)

        await msg.author.send(f"{slapped_user.display_name} has been slapped.")


def setup(bot: Bot):
    bot.add_listener(on_message, "on_message")

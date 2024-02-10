from nextcord.ext import commands
from nextcord.ext.commands import Bot, Context
from engine.bot import bot


class AdminCmds(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def servers(self, ctx: Context):
        msg = ""
        index = 0
        for guild in bot.guilds:
            msg += f"{index}. {guild.name} - {guild.owner}\n"
            index += 1
        await ctx.send(msg)

    @commands.is_owner()
    @commands.command()
    async def reload_cog(self, ctx: Context, *, cog_name: str = None):
        if cog_name not in ["", None]:
            try:
                self.bot.reload_extension(cog_name)
                await ctx.send(f"Reloaded `{cog_name}` successfully.")
            except Exception as e:
                await ctx.send(f"Error reloading {cog_name}:\n```{e}```")
        else:
            await ctx.send("Please specify a cog to reload")

    @commands.is_owner()
    @commands.command()
    async def list_cogs(self, ctx: Context):
        msg = "Loaded Extensions:\n```\n"
        for extension in self.bot.extensions:
            msg += f"{extension}\n"

        await ctx.send(msg+"```")


def setup(bot: Bot):
    bot.add_cog(AdminCmds(bot))

import asyncio
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class cmds(commands.Cog):
    """
    A sample set of rules you can use when your first starting your server to save time.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["help"])
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def cmds(self, ctx):
        """"""
        embed = discord.Embed(
            title=" "
        )
        embed.set_author(name=str(ctx.author), icon_url=str(ctx.author.avatar_url))
        embed.description = """
                You can view my commands [here.](https://github.com/DrizzleAssistant/DrizzleBots/blob/master/announcement-cmds.md)
            """
        embed.set_footer(text="Users with the announcements role can use the bot.")
        embed.color = self.bot.main_color
        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(cmds(bot))

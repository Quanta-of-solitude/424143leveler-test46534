import discord
from discord.ext import commands

class Trader:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self,ctx):
        '''help menu'''
        menu = """
```Help Menu:


1. help: Shows this meu.

2. trades: Shows the list of trades available.

3. infotrade: get info on a trade.
    Usage: tr!infotrade [ID]

4. trade: Set your entry.
    Usage: tr!trade "[item]" "[quantity]" "[cost]"
    Note: The quotations are necessary.

5. invite: Invite link
```
"""
        await ctx.send("**Version 0.01 by qQnN**\n"+menu)

    @commands.command()
    async def invite(self,ctx):
        link = "<https://discordapp.com/oauth2/authorize?client_id=404329051998912513&scope=bot&permissions=0>"
        await ctx.send(link)



def setup(bot):
    bot.add_cog(Trader(bot))

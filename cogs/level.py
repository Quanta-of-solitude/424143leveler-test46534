import os
import json
import uuid
import discord
import re
import myjson
from discord.ext import commands
from operator import itemgetter

class Store:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return
        url = "{}".format(os.environ.get("storee"))
        store = myjson.get(url)
        store = json.loads(store)
        file2  = open("data/levels.json", 'r+')
        file2 = file2.read()
        levels = json.loads(file2)
        if f"{message.guild.id}" not in store:
            store[f"{message.guild.id}"] = {}
            if f"{message.author.id}" not in store[f"{message.guild.id}"]:
                store[f"{message.guild.id}"][f"{message.author.id}"] = {}
                store[f"{message.guild.id}"][f"{message.author.id}"]["points"] = 0
                store[f"{message.guild.id}"][f"{message.author.id}"]["level"] = 0
                url = myjson.store(json.dumps(store),update=url)

            else:
                point = store[f"{message.guild.id}"][f"{message.author.id}"]["points"]
                point +=2
                store[f"{message.guild.id}"][f"{message.author.id}"]["points"] = point
                if f"{point}" in levels:
                    level = levels[f"{point}"]
                    store[f"{message.guild.id}"][f"{message.author.id}"]["level"] = level
                    await message.channel.send(f"Congrats! {message.author.name} you just reached level **{level}!**")
                url = myjson.store(json.dumps(store),update=url)
        else:
            if f"{message.author.id}" not in store[f"{message.guild.id}"]:
                store[f"{message.guild.id}"][f"{message.author.id}"] = {}
                store[f"{message.guild.id}"][f"{message.author.id}"]["points"] = 0
                store[f"{message.guild.id}"][f"{message.author.id}"]["level"] = 0
                url = myjson.store(json.dumps(store),update=url)
            else:
                point = store[f"{message.guild.id}"][f"{message.author.id}"]["points"]
                point +=2
                store[f"{message.guild.id}"][f"{message.author.id}"]["points"] = point

                if f"{point}" in levels:
                    level = levels[f"{point}"]
                    store[f"{message.guild.id}"][f"{message.author.id}"]["level"] = level
                    await message.channel.send(f"Congrats! {message.author.name} you just reached level **{level}!**")
                url = myjson.store(json.dumps(store),update=url)


    @commands.command(aliases = ["point"])
    async def points(self,ctx, *, member : discord.Member=None):
        server = ctx.guild
        user = member or ctx.message.author
        url = "{}".format(os.environ.get("storee"))
        store = myjson.get(url)
        store = json.loads(store)
        if f"{user.id}" not in store[f"{server.id}"]:
            if user.id == ctx.author.id:
                await ctx.send("**You haven't started chatting yet!**")
                return
            else:
                await ctx.send(f"**{user.name} have no points yet!**")
        points = store[f"{ctx.guild.id}"][f"{user.id}"]["points"]
        level = store[f"{ctx.guild.id}"][f"{user.id}"]["level"]
        if user.id == ctx.author.id:
            em = discord.Embed(title = f"{user.name}", url = "https://placeholder.com/")
            em.colour = discord.Colour.blue()
            em.set_thumbnail(url = f"{user.avatar_url}")
            em.set_footer(text = "|Level-Test|",icon_url = self.bot.user.avatar_url)
            em.add_field(name = "Level:", value = f"{level}/50", inline = False)
            em.add_field(name = "Rank:", value = "Not Done.", inline = False)
            em.add_field(name = "Points:", value = f"{points}/99998(Total)", inline = False)
            await ctx.send(embed = em)
        else:
            em = discord.Embed(title = f"{user.name}", url = "https://placeholder.com/")
            em.colour = discord.Colour.blue()
            em.set_thumbnail(url = f"{user.avatar_url}")
            em.set_footer(text = "|Level-Test|",icon_url = self.bot.user.avatar_url)
            em.add_field(name = "Level:", value = f"{level}/50", inline = False)
            em.add_field(name = "Rank:", value = "Not Done.", inline = False)
            em.add_field(name = "Points:", value = f"{points}/99998(Total)", inline = False)
            await ctx.send(embed = em)





def setup(bot):
    bot.add_cog(Store(bot))

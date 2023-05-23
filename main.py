import discord
from NEWSAPI1 import (alt_message,
                      sourceslist,
                      get_tech_news,
                      x1,
                      get_business_news,
                      get_entertainment_news,
                      get_regional_news,
                      get_health_news,
                      get_general_news,
                      get_science_news,
                      get_sports_news,
                      get_queried_news,
                      x2,
                      x3,
                      x4,
                      x5,
                      x6,
                      x7,
                      x8,
                      x9,
                      x10
                      )

from Youtube import url_getter
from Youtube import urlist
import os
from keep_alive import keep_alive
import random

from discord import FFmpegOpusAudio,FFmpegPCMAudio 
import youtube_dl
import re
import time
from keep_alive import keep_alive

client = discord.Client()

players = {}

import ctypes
import ctypes.util
 
print("ctypes - Find opus:")
a = ctypes.util.find_library('opus')
print(a)
 
print("Discord - Load Opus:")
b = discord.opus.load_opus(a)
print(b)
 
print("Discord - Is loaded:")
c = discord.opus.is_loaded()
print(c)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='!info'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!tech"):

        get_tech_news()
        await message.channel.send("👇")

        for items in x1:
            embede = discord.Embed(
            title="Tech News 🌏",
            description= items)
        
            await message.channel.send(embed=embede)


    if message.content.startswith("!business"):
        get_business_news()
        await message.channel.send("👇")

        for items in x2:
            embede = discord.Embed(
            title="Business News 🌏",
            description= items)
        
            await message.channel.send(embed=embede)


    if message.content.startswith("!entertainment"):
        get_entertainment_news()
        await message.channel.send("👇")

        for items in x3:
            embede = discord.Embed(
            title="Entertainment News 🌏",
            description= items)
        
            await message.channel.send(embed=embede)


    if message.content.startswith("!health"):
        get_health_news()

        await message.channel.send("👇")

        for items in x5:
            embede = discord.Embed(
            title="Health News 🌏",
            description= items)
        
            await message.channel.send(embed=embede)

    if message.content.startswith("!general"):
        get_general_news()
        await message.channel.send("👇")

        for items in x4:
            embede = discord.Embed(
            title="General News 🌏",
            description= items)
        
            await message.channel.send(embed=embede)

    if message.content.startswith("!science"):
        get_science_news()
        await message.channel.send("👇")

        for items in x6:
            embede = discord.Embed(
            title="Science News 🌏",
            description= items)
        
            await message.channel.send(embed=embede)


    if message.content.startswith("!sports"):
        get_sports_news()
        await message.channel.send("👇")

        for items in x7:
            embede = discord.Embed(
            title="Sports News 🌏",
            description= items)
        
            await message.channel.send(embed=embede)

    if message.content.startswith("!regioncodes"):
        codestr = "aearataubebgbrcachcncocuczdeegfrgbgrhkhuidieilinitjpkrltlvmamxmyngnlnonzphplptrorsrusasesgsiskthtrtwuausveza"
        codelist = re.findall("..?", codestr)
        embed1 = discord.Embed(
            title="Region Codes", description=codelist, color=0x0037FF
        )
        await message.channel.send("👇")
        await message.channel.send(embed=embed1, content=None)

    if message.content.startswith("!regional"):

        await message.channel.send("Enter your region code : ")

        def check(msg):
            print(msg.content)
            return msg.content

        msg = await client.wait_for("message", check=check)

        get_regional_news(count=msg.content)
        await message.channel.send("👇")
        for items in x8:
            await message.channel.send(items)

    if message.content.startswith("!query"):
        await message.channel.send("Enter your query : ")

        def check1(msg1):
            print(msg1.content)
            return msg1.content

        msg1 = await client.wait_for("message", check=check1)
        get_queried_news(query=msg1.content)
        await message.channel.send("👇")

        for items in x9:
            await message.channel.send(items)

    if message.content.startswith("!info"):
        embed = discord.Embed(
            title="NewsBot🌏 Commands",
            description="All the commands NewsBot🌏 currently has.",
            color=0x0037FF,
        )
        embed.add_field(
            name="!tech", value="Shows the top headlines for the technology category"
        )
        embed.add_field(
            name="!health", value="Shows the top headlines for the health category"
        )
        embed.add_field(
            name="!entertainment",
            value="Shows the top headlines for the entertainment category",
        )
        embed.add_field(
            name="!general", value="Shows the top headlines for the general category"
        )
        embed.add_field(
            name="!science", value="Shows the top headlines for the science category"
        )
        embed.add_field(
            name="!sports", value="Shows the top headlines for the sports category"
        )
        embed.add_field(
            name="!business", value="Shows the top headlines for the business category"
        )
        embed.add_field(
            name="!regional", value="Shows the top headlines for the regional category"
        )
        embed.add_field(
            name="!sallubhaimarriagestatus",
            value="Shows the relationship status of our beloved Sallu Bhai",
        )
        embed.add_field(
            name="!regioncodes",
            value="Shows all the region codes available for getting regional news",
        )
        embed.add_field(
            name="!query",
            value="Shows the top headlines for the entered query. If there were no headlines for the entered query today top headlines from before will be showed.",
        )

        embed.add_field(
            name="!join",
            value="Makes the bot join the current voice channel you're in",
        )

        embed.add_field(
            name="!leave",
            value="Makes the bot leave the current voice channel you're in",
        )

        embed.add_field(
            name="!p",
            value="Prompts you to enter a query and play the most relevent video to the query",
        )

        embed.set_thumbnail(
            url="https://i.imgur.com/CImaeHa.png"
        )
        await message.channel.send(embed=embed, content=None)

    if message.content.startswith("!sourceslist"):
      embed5 = discord.Embed(
            title = "NewsBot🌏 Sources",
            description="The 2 letter Alpha-2 Codes that can be used with NewsBot can be found [here](https://www.iban.com/country-codes)",
            color=0x0037FF)
      await message.channel.send(embed=embed5, content=None)

        
        
    if message.content.startswith("!sallubhaimarriagestatus"):
        listofpics = [
            "bhai.png",
            "bhai1.png",
            "bhai2.jpg",
            "bhai3.gif",
            "bhai4.jpg",
            "bhai5.jpg",
        ]
        await message.channel.send("Current Status : STILL SINGLE 😔")
        pic = random.choice(listofpics)
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("!join"):
        channel = message.author.voice.channel
        await channel.connect()

    if message.content.startswith("!leave"):
        guild = message.author.guild
        voice_client = guild.voice_client
        await voice_client.disconnect()

    if message.content.startswith("!audio"):


        await message.channel.send("Enter your query : ")


        def check2(msg2):
            print(msg2.content)
            return msg2.content

        msg2 = await client.wait_for("message", check=check2)

        url_getter(query=msg2.content)

        guild = message.author.guild
        voice_client = guild.voice_client

        options = {

            'format': 'bestaudio',
            'keepvideo': False,
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
            }]}



        time.sleep(0)

        print(urlist[-1].strip())



        if not voice_client.is_playing():
            with youtube_dl.YoutubeDL(options) as ydl:
                info = ydl.extract_info(urlist[-1].strip(), download=False)
            await message.channel.send(f"Now Playing : {urlist[-1].strip()}")
            URL = info['formats'][0]['url']
            await message.channel.send(file=discord.File("2x.gif"))
            voice_client.play(FFmpegPCMAudio(URL))
            voice_client.is_playing()

    if message.content.startswith("!pause"):
        guild = message.author.guild
        voice_client = guild.voice_client
        voice_client.pause()

    if message.content.startswith("!play"):
        guild = message.author.guild
        voice_client = guild.voice_client
        voice_client.resume()

    if message.content.startswith("!stop"):
        guild = message.author.guild
        voice_client = guild.voice_client
        voice_client.stop()

keep_alive()
client.run("ODMyMDEwMDg1Mzk1NDY0MjAz.YHdjxg.-0ubwkBrXo2Vctu3omqUrabx3T0")

# GET THE REGION CODES WITH THEIR COUNTRY NAMES

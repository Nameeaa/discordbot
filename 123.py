import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import random

client = discord.Client()
client_prefix="#"
client = commands.Bot(command_prefix=client_prefix)





chat_filter = ["asd","asd","aasdasd"]
bypass_list = []

@client.event
async def on_ready():
    print("Bot Çevrimiçi")
@client.event
async def on_message(message):
    if message.content == "@HARBİ GICIK OLDUM BAK#5869":
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> ***He Söyle Ne Diyon ?***" % (userID))
    if message.content == "MahmuT":
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> ***Mahmut Da Mahmut Kim Bu Mahmut Aq***" % (userID))
    if message.content.startswith('#temizle'):
        tmp = await client.send_message(message.channel, '***Mesajlar Silinyor....***')
        a = 200
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)
        await client.send_message(message.channel, '***Silindi ...***')
        await client.delete_message(msg)
    if message.content.startswith('#sorucevap'):
        seçim = ['Evet',
                 'Hayır',
                 'Olabilir',
                 'Olmayabilir']
        await client.send_message(message.channel, random.choice(seçim))
        
    if message.content.startswith('#yazıtura'):
        variable = ['Yazı',
                    'Tura']
        await client.send_message(message.channel, random.choice(variable))
    if message.content.startswith('#help'):
        userID = message.author.id
        await client.send_message(message.channel, "(#)dedigimide : ***Yazıdığınızı yazar***" )
        await client.send_message(message.channel, "(#)yazıtura : ***Yazı tura Atar***" )
        await client.send_message(message.channel, "(#)temizle : ***Nerdeyse Bütün Chati Siler (Uzun Sürebilir)***" )
        await client.send_message(message.channel, "(#)sorucevap: ***Sadece Evet,Hayır,Olabilir ve Olmayabilir Olarak cevap Veren Sistem***" )
    if message.content == "SLM":
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> ***Sanada Selam :ok_hand: ***" % (userID))
    if message.content == "SA":
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> ***Aleyküm Selam Hoşgeldin :smile:***"% (userID))
    if message.content == "sa":
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> ***Aleyküm Selam Hoşgeldin :smile:***"% (userID))
    if message.content == "slm":
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> ***Sanada Selam :ok_hand: ***" % (userID))
    if message.content == "selamun aleyküm":
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> ***Aleyküm Selam Hoşgeldin :smile:***" % (userID))
    if message.content.startswith('#deneme'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> ***za!***" % (userID))
    if message.content.startswith('#dedigimide'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    if message.content.startswith('#kurucu'):
        if "476508007589478410" in [role.id for role in message.author.roles]:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Sen Kurucusun !" % (userID))
        else :
            await client.send_message(message.channel,"Bu İzne Sahip Değilsin")

client.run("NDg4OTQ1ODAyNjA2MjgwNzA0.DnkUpg.W6kSPPK08wCuKs30nWcn5RFpsfE")

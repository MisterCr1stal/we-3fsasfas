import discord
import requests
import time

TOKEN = "OTQzNTM1MzA2NDA0MTQzMTc0.Yg0duw.9EKR2Z9dIzKhFxA7zdE9D8QiIdM"


client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is now online!".format(client))


@client.event
async def on_message(message):
    if message.content.startswith('!asdasopfuasdwq9eiqw-0rfixc0xz0casdiqwoehyqwe'):
        print("JOB STARTED!")
        while True:
            time.sleep(4)
            robloxver = "http://setup.roblox.com/version"
            rq = requests.get(robloxver)

            myver = "https://pastebin.com/raw/kWbeuxTC"
            rq1 = requests.get(myver)

            if rq.content == rq1.content:
                print("EXPLOIT UPDATED!")
            else:
                print("ROBLOX UPDATED! NOTIFICATION SENDING!")
                await message.channel.send(f"***@here Роблокс Обновился! Прошлая версия роблокса: { rq1.content } Новая версия роблокса: { rq.content }. Nezy иди обновляй Neyron X! :)***")
                return

client.run(TOKEN)
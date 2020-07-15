import discord
from discord.ext import commands

import supersecret
import re

import samesame


BOT_TOKEN = supersecret.getSecret('discord_bot_samesame', 'bot_token')

NAME = "samesame#1172"
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.startswith("!samesame") and message.author != "samesame#1172":
            text = message.content[len("!samesame"):]
            result = await message.channel.send(samesame.samesame(text))
        elif message.content.startswith("!describe") and message.author != "samesame#1172":
            category_m = re.findall("!describe ([a-zA-Z0-9-]+)", message.content)
            if len(category_m) < 1:
                return
            category_name = category_m[0]
            for category in message.guild.categories:
                print(category.name)
                if category.name == category_name:
                    print("category object", repr(category))
                    result = await category.edit(position=1)
        elif message.content.startswith("!help") and message.author != NAME:
            result = await message.channel.send("commands supported: '!samesame TEXT'")
client = MyClient()
client.run(BOT_TOKEN)

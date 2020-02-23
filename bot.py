import discord
import supersecret

import samesame

BOT_TOKEN = supersecret.getSecret('discord_bot_samesame', 'bot_token')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content.startswith("!samesame") and message.author != "samesame#1172":
            text = message.content[len("!samesame"):]
            print('Message from {0.author}: {0.content}'.format(message))
            result = await message.channel.send(samesame.samesame(text))
        else:
            print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(BOT_TOKEN)

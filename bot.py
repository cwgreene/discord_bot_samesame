import discord
from discord.ext import commands

import supersecret
import re

import samesame


BOT_TOKEN = supersecret.getSecret('discord_bot_samesame', 'bot_token')

class MyClient(commands.Bot):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
client = MyClient("!",
    description="Enhance strings",
    help_command=commands.DefaultHelpCommand())

@client.command(name='samesame', help="enhance string")
async def samesame_cmd(ctx):
    print('Message from {0.author}: {0.content}'.format(ctx.message))
    text = ctx.message.content[len("!samesame"):]
    await ctx.send(samesame.samesame(text))

client.run(BOT_TOKEN)

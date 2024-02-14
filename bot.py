import json
import logging
import discord as dc
from discord import app_commands

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
with open('config.json', 'r') as cfg:
    data = json.load(cfg)
pf = data["prefix"]

guild = dc.Object(id=919366996578140230)

intents = dc.Intents.default()
intents.message_content = True

client = dc.Client(command_prefix=pf, intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="translate", description="translate msg", guild=guild)
@app_commands.describe(message='message')
async def translate(interaction, message: str):
    await interaction.response.send_message(content=message[::-1], ephemeral=True)

@client.event
async def on_ready():
    await tree.sync(guild=guild)
    print(f'Bot Setup as {client.user}')

client.run(data["token"], log_handler=handler, log_level=logging.DEBUG)
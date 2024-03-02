import json
import logging
import discord as dc
from discord import app_commands
from discord.ext import tasks, commands

with open('config.json', 'r') as cfg:
    data = json.load(cfg)

guild = dc.Object(id=1205245019703869460)

bot = commands.Bot(command_prefix='!', intents=dc.Intents.all())
tree = bot.tree

@bot.tree.command(name="translate", description="Translate a message from or into Xander Talk", guild=guild)
@app_commands.describe(message='message')
async def translate(interaction, message: str):
    print(message)
    await interaction.response.send_message(content=message[::-1], ephemeral=True)

@bot.tree.command(name="election", description="THIS COMMAND DOES NOT WORK AT ALL YET, DO NOT USE", guild=guild)
@app_commands.describe()
@app_commands.checks.has_permissions(manage_messages=True)
async def election(interaction):
    embed = dc.Embed(
        title = "Election",
        color = dc.Color.yellow()
    )
    embed.add_field(name="tester", value="test value")
    await interaction.response.send_message(embed=embed)

class BackgroundTasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @tasks.loop(minutes=3)
    async def obamna(self):
        print("Obamna Cog Task Activated")
        channel = self.bot.get_channel(1212191353035825184)
        await channel.send("obamna")

    async def cog_load(self):
        print("Cog Loaded!")
        self.obamna.start()

async def setup_hook() -> None:
    await bot.tree.sync(guild=guild)

@bot.event
async def on_ready():
    print(f'Bot Setup as {bot.user}')
    await setup(bot)

async def setup(bot: commands.Bot):
    await bot.add_cog(BackgroundTasks(bot))

bot.run(data["token"])
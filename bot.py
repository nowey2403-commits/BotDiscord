import discord
import os
from discord.ext import commands

TOKEN = os.environ.get("TOKEN")

CHANNEL_IDS = [
    1469836228773019924,
]

OWNER_IDS = [
    827931277273333830,
    1216102220009832608,
]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connecté en tant que {bot.user}")
    print(f"📡 Présent sur {len(bot.guilds)} serveur(s)")

@bot.command()
async def send(ctx, *, message):
    if ctx.author.id not in OWNER_IDS:
        await ctx.send("❌ Tu n'as pas la permission d'utiliser cette commande !")
        return

    for channel_id in CHANNEL_IDS:
        channel = bot.get_channel(channel_id)
        if channel:
            await channel.send(message)

bot.run(TOKEN)
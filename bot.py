import discord
from discord.ext import commands
import os
TOKEN = os.environ.get("MTQ3NzA4ODg5MDY2NDc3OTkxNw.G8mmLP.xry7rM4hm1ZdocVNj__W-syNx6LVpFMIT6EA3U")

# ⬇️ Remplace ces IDs par ceux que tu as copiés
CHANNEL_IDS = [
    1469836228773019924,  # Salon serveur 1
   
]

# ⬇️ Colle ton ID Discord ici (clic droit sur ton pseudo → Copier l'identifiant)
OWNER_ID = 827931277273333830

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connecté en tant que {bot.user}")
    print(f"📡 Présent sur {len(bot.guilds)} serveur(s)")

@bot.command()
async def broadcast(ctx, *, message):
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ Tu n'as pas la permission d'utiliser cette commande !")
        return

    for channel_id in CHANNEL_IDS:
        channel = bot.get_channel(channel_id)
        if channel:
            await channel.send(message)

bot.run(TOKEN)

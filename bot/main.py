import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

from services.gpt import ask_gpt


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot is online as {bot.user}')

# === Your command goes here *after* bot is defined ===
@bot.command()
async def ask(ctx, *, question):
    await ctx.send("🧠 Thinking...")
    response = await ask_gpt(question)
    await ctx.send(response[:2000])  # Trim to Discord's message limit

# === Run the bot ===
bot.run(os.getenv("DISCORD_TOKEN"))

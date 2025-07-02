import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from services.memory import reset_user_history
from services.gpt import ask_gpt
from services.token_tracker import get_tokens
from services.persona import set_mode, get_current_mode
from services.persona import user_modes


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
    response = await ask_gpt(question, ctx.author.id)
    await ctx.send(response[:2000])

@bot.command()
async def reset(ctx):
    await reset_user_history(ctx.author.id)
    user_modes.pop(ctx.author.id, None)  # reset mode to default
    await ctx.send("🧹 Memory and mode reset. You're starting fresh!")

@bot.command()
async def tokens(ctx):
    count = get_tokens(ctx.author.id)
    await ctx.send(f"📊 You've used `{count}` tokens so far.")
@bot.command()
async def mode(ctx, *, persona=None):
    if persona:
        result = set_mode(ctx.author.id, persona.lower())
        await ctx.send(result)
    else:
        current = get_current_mode(ctx.author.id)
        await ctx.send(f"🧠 Your current mode is **{current}**. Use `!mode <type>` to change.")
@bot.command()
async def modes(ctx):
    from services.persona import PRESETS
    await ctx.send("🧠 Available modes: " + ", ".join(f"`{m}`" for m in PRESETS))
# === Run the bot ===
bot.run(os.getenv("DISCORD_TOKEN"))

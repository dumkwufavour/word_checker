import os
import discord
from discord.ext import commands
import json
from dotenv import load_dotenv

# Load banned words from JSON file
with open('banned_words.json', 'r') as file:
    banned_words = json.load(file)['banned_words']

# Create a bot instance with the necessary intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix="!", intents=intents)

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    # Check if message contains banned words
    message_content = message.content.lower()
    if any(word in message_content for word in banned_words):
        await message.delete()  # Delete the message
        
        # Notify the channel
        await message.channel.send(
            f'{message.author} tried to use a banned word, but it has been blocked.'
        )

    # Allow other commands to work
    await bot.process_commands(message)

bot.run(BOT_TOKEN)

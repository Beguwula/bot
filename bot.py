import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

count_channel_id = YOUR_COUNTING_CHANNEL_ID  # Replace with your channel ID
current_count = 0

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    global current_count

    if message.channel.id == count_channel_id:
        try:
            number = int(message.content)
            if number == current_count + 1:
                current_count += 1
                await message.add_reaction('✅')
            else:
                await message.channel.send(f'{message.author.mention} messed up the count! Start again from 1.')
                current_count = 0
        except ValueError:
            pass  # Ignore messages that are not numbers

    await bot.process_commands(message)

bot.run('YOUR_BOT_TOKEN')  # Replace with your bot token

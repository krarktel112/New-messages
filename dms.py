import discord

# Replace with your bot's token
TOKEN = "YOUR_BOT_TOKEN" 

# Enable necessary intents (including message content for reading messages)
intents = discord.Intents.default()
intents.message_content = True  # You need this to read message content

# Initialize the bot
bot = discord.Client(intents=intents) 

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        return

    # Check if the message is a DM
    if isinstance(message.channel, discord.DMChannel):  
        print(f"New DM from {message.author}: {message.content}")

        # Send an alert (e.g., to a specific channel)
        # Replace 'YOUR_ALERT_CHANNEL_ID' with the ID of the channel where you want alerts
        alert_channel = bot.get_channel(YOUR_ALERT_CHANNEL_ID) 
        if alert_channel:
            await alert_channel.send(f"New DM from {message.author}: {message.content}") 
        else:
            print("Alert channel not found. Please provide a valid channel ID.")

bot.run(TOKEN)

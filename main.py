import discord
import asyncio

# at DC Token you put your discord bot token
TOKEN = "Dc Token"
# at [Channelid] you do your channel ids
CHANNELS = [
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid],
    [Channelid]
]

# change 123456 with the actual user id of the person
USER_ID = 123456
PING_INTERVAL = 0.1  
intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def ping_loop(channel_id):
    await client.wait_until_ready()
    channel = client.get_channel(channel_id)
    if channel:
        while True:
            await channel.send(f"<@{USER_ID}> 🔔 Hi")
            await asyncio.sleep(PING_INTERVAL)
    else:
        print(f"❌ Channel {channel_id} nicht gefunden!")

@client.event
async def on_ready():
    print(f"✅ Bot is online {client.user}")
    for channel_id in CHANNELS:
        asyncio.create_task(ping_loop(channel_id))

client.run(TOKEN)

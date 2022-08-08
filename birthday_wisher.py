import os
import aiohttp
from discord import Webhook, AsyncWebhookAdapter
from dotenv import load_dotenv
import asyncio
import random
import platform
from readfile import check_bday

load_dotenv()
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

wish_file = open("wishes.txt", "r")
wish_list = wish_file.read().split('\n')

birthday_peeps = check_bday()

def birthday_message(name):
    return f"""
    @everyone Wish {name} a very Happy Birthday Today
    Hey {name},
    {random.choice(wish_list)}
    """


# configuring asyncio for windows
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def wisher(msg):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(WEBHOOK_URL, adapter=AsyncWebhookAdapter(session))
        await webhook.send(msg, username='CSI Birthday Wisher')

async def main():
    
    for name in birthday_peeps : 
        await wisher(birthday_message(name))

asyncio.run(main())

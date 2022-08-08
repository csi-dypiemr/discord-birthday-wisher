import os
import aiohttp
from discord import Webhook, AsyncWebhookAdapter
from dotenv import load_dotenv
import asyncio
import platform

load_dotenv()
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

# configuring asyncio for windows
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def wisher():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(WEBHOOK_URL, adapter=AsyncWebhookAdapter(session))
        await webhook.send('Hello World', username='CSI Birthday Wisher')

async def main():
    
    await wisher()

asyncio.run(main())

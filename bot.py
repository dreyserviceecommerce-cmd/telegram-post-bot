import os
import asyncio
import random
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_IDS = os.getenv("CHAT_IDS").split(",")
INTERVAL = int(os.getenv("POST_INTERVAL_MINUTES", "60"))

MESSAGES = [
    "Need 3CX setup or call system?\nDM 👉 @didnumberforspoofing",
    "SIP trunk + DID numbers available 🌍\nMessage 👉 @didnumberforspoofing",
    "IVR + Call queue + 3CX setup\nInbox 👉 @didnumberforspoofing"
]

async def main():
    bot = Bot(token=BOT_TOKEN)

    while True:
        for chat_id in CHAT_IDS:
            try:
                await bot.send_message(chat_id=int(chat_id), text=random.choice(MESSAGES))
            except Exception as e:
                print(e)

            await asyncio.sleep(10)

        await asyncio.sleep(INTERVAL * 60)

asyncio.run(main())

import os
import asyncio
import random
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_IDS = [x.strip() for x in os.getenv("CHAT_IDS", "").split(",") if x.strip()]
INTERVAL = int(os.getenv("POST_INTERVAL_MINUTES", "1"))

MESSAGES = [
    "🚀 CALL CENTER SETUP | VOIP | IVR SOLUTIONS

I provide complete call center setup with:

✅ DID Numbers (Multiple Countries)
✅ SIP Trunk Setup
✅ IVR (Interactive Voice Response)
✅ Call Queue Configuration
✅ 3CX Setup (Users, Routing, Queues)
✅ Automation & Bot Integration

💡 Perfect for:
• Customer Support Teams
• Sales Call Centers
• Business Phone Systems
• VoIP & Telecom Projects

🌍 Countries Available:
USA 🇺🇸 | Canada 🇨🇦 | UK 🇬🇧 | Australia 🇦🇺 | Europe 🇪🇺 | Asia 🌏 & more

⚙️ Services Include:
• 3CX Installation & Configuration
• IVR Menu Setup (Multi-level)
• Call Routing & Queue Setup
• DID & SIP Integration
• Telegram / Automation Bot Integration (Optional)

📩 Message me to get started
👉 @Ledgerspoofing",
    
]

async def main():
    bot = Bot(token=BOT_TOKEN)

    while True:
        for chat_id in CHAT_IDS:
            try:
                await bot.send_message(chat_id=int(chat_id), text=random.choice(MESSAGES))
                print(f"Sent to {chat_id}")
            except Exception as e:
                print(repr(e))
            await asyncio.sleep(5)

        await asyncio.sleep(INTERVAL * 60)

asyncio.run(main())

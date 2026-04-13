import os
import asyncio
import random
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_IDS = [x.strip() for x in os.getenv("CHAT_IDS", "").split(",") if x.strip()]
INTERVAL = int(os.getenv("POST_INTERVAL_MINUTES", "5"))

# 🔥 ROTATING MESSAGES (SAFE + HIGH CONVERT)
MESSAGES = [
"""🚀 CALL CENTER SETUP | VOIP | IVR SOLUTIONS

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

🌍 Coverage: USA 🇺🇸 | UK 🇬🇧 | Canada 🇨🇦 | Australia 🇦🇺 | Europe 🇪🇺 | Asia 🌏

📩 Message me 👉 @Ledgerspoofing
""",

"""🔥 NEED A RELIABLE CALL SYSTEM?

I help businesses set up:

✔️ 3CX Phone System
✔️ IVR & Call Routing
✔️ DID Numbers (Worldwide)
✔️ SIP Trunks
✔️ Call Queue Setup

⚡ Fast & Professional Setup

📩 DM now 👉 @Ledgerspoofing
""",

"""💼 VOIP & CALL CENTER SOLUTIONS AVAILABLE

Get your system ready with:

• 3CX Setup & Configuration
• IVR Menu Setup
• Call Routing & Queues
• DID + SIP Integration
• Automation Support

🌍 Available Worldwide

📩 Contact 👉 @Ledgerspoofing
"""
]

async def main():
    bot = Bot(token=BOT_TOKEN)

    print("🚀 Bot started...")

    while True:
        for chat_id in CHAT_IDS:
            try:
                message = random.choice(MESSAGES)
                await bot.send_message(chat_id=int(chat_id), text=message)
                print(f"✅ Sent to {chat_id}")
            except Exception as e:
                print(f"❌ Error sending to {chat_id}: {repr(e)}")

            # small delay between groups (avoid spam flag)
            await asyncio.sleep(random.randint(5, 15))

        # wait before next round
        print(f"⏳ Waiting {INTERVAL} minutes...")
        await asyncio.sleep(INTERVAL * 60)

asyncio.run(main())

from telethon import TelegramClient
import base64

# Put your Telegram API ID and API HASH here directly
api_id = int(input("Enter API ID: "))
api_hash = input("Enter API HASH: ")

client = TelegramClient("ghana_session", api_id, api_hash)

async def main():
    me = await client.get_me()
    print("✅ Logged in as:", me.username or me.first_name)

with client:
    client.start()
    client.loop.run_until_complete(main())

# Convert the session to base64
with open("ghana_session.session", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

with open("ghana_session_b64.txt", "w") as f:
    f.write(b64)

print("\n⚠️ Copy the text from 'ghana_session_b64.txt' into your GitHub secret TELEGRAM_SESSION_B64.")

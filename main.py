from pyrogram import Client
from sarufi import Sarufi

from keys import keys

sarufi = Sarufi(api_key=keys["SARUFI_API_KEY"])
sarufi_bot = sarufi.get_bot(id=keys["SARUFI_BOT_ID"])

app = Client(
    name="myResumeBot",
    api_id=keys["TELEGRAM_API_ID"],
    api_hash=keys["TELEGRAM_API_HASH"],
    bot_token=keys["TELEGRAM_BOT_TOKEN"]
)


@app.on_message()
async def reply(client, message):
    response = sarufi_bot.respond(message.text)['actions'][0]['send_message'][0]
    await message.reply(response)

app.run()


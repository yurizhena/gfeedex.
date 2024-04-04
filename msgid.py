from telethon import TelegramClient
import ssl
from python_socks.sync import Proxy
# Use your own values from my.telegram.org
api_id = 123
api_hash = '123'
client = TelegramClient('anon', api_id, api_hash)
# The first parameter is the .session file name (absolute paths allowed)
async def main():
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)
with client:
    client.loop.run_until_complete(main())
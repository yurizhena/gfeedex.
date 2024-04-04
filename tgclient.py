from telethon import TelegramClient, events
from datetime import datetime

api_id = 123
api_hash = '123'

client = TelegramClient('anon', api_id, api_hash)

client.start()

print('Client on')
print('Waiting for new msg')
@client.on(events.NewMessage(chats=[-123]))
async def handler(event):
  newmsg = event.raw_text
  print(newmsg)
  timestamp = datetime.now().isoformat(timespec='milliseconds')
  print(timestamp)
  print('Waiting for news')

client.run_until_disconnected()








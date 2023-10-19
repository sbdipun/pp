#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 7405235, #get it from https://my.telegram.org/auth
    api_hash="5c9541eefe8452186e9649e2effc1f3f", #get it from https://my.telegram.org/auth
    bot_token="5540645913:AAGD5ZXVRrlPWtiRHQbx-khqakcPVksTyu0", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        

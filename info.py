import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """𝙷𝙴𝙻𝙾 {},
𝑴𝒀 𝑵𝑨𝑴𝑬 , <a href='https://t.me/Dqautofl_bot'>𝐀𝐍𝐍𝐀 𝐁𝐄𝐍</a>, 𝑰𝒕'𝒔 𝑽𝒆𝒓𝒓𝒚 𝑬𝒂𝒔𝒚. 𝑱𝒖𝒂𝒕 𝑨𝒅𝒅 𝑴𝒆 𝑻𝒐 𝒀𝒐𝒖𝒓 𝑮𝒓𝒐𝒖𝒑 𝑨𝒏𝒅 𝑴𝒂𝒌𝒆 𝑴𝒆 𝑨𝒅𝒎𝒊𝒏, 𝑻𝒉𝒂𝒕𝒔 𝑨𝒍𝒍, 𝑰'𝑳𝑳 𝑷𝒓𝒐𝒗𝒊𝒅𝒆 𝑴𝑶𝑽𝑰𝑬𝑺 𝑻𝒉𝒆𝒓𝒆 🤓
𝑯𝑬𝒀,<a href='http://t.me/Dqautofl_Bot?startgroup=true'>𝑨𝒅𝒅 𝑴𝒆 𝑻𝒐 𝒀𝒐𝒖𝒓 𝑮𝒓𝒐𝒖𝒑 𝑨𝒏𝒅 𝑴𝒂𝒌𝒆 𝑴𝒆 𝑨𝒏 𝑨𝒅𝒎𝒊𝒏 𝑻𝒉𝒆𝒓𝒆</a>
➖➖➖➖➖➖➖➖➖➖➖➖➖
©️MᴀɪɴᴛᴀɪɴᴇD Bʏ: <a href="https://t.me/pro_editor_tg"> 𝖫𝖺𝗅𝗅𝗎ˡᵃˡˡᵘˢ </a>"""
  

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')

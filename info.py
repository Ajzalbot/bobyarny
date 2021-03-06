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
default_start_msg = """๐ท๐ด๐ป๐พ {},
๐ด๐ ๐ต๐จ๐ด๐ฌ , <a href='https://t.me/Dqautofl_bot'>๐๐๐๐ ๐๐๐</a>, ๐ฐ๐'๐ ๐ฝ๐๐๐๐ ๐ฌ๐๐๐. ๐ฑ๐๐๐ ๐จ๐๐ ๐ด๐ ๐ป๐ ๐๐๐๐ ๐ฎ๐๐๐๐ ๐จ๐๐ ๐ด๐๐๐ ๐ด๐ ๐จ๐๐๐๐, ๐ป๐๐๐๐ ๐จ๐๐, ๐ฐ'๐ณ๐ณ ๐ท๐๐๐๐๐๐ ๐ด๐ถ๐ฝ๐ฐ๐ฌ๐บ ๐ป๐๐๐๐ ๐ค
๐ฏ๐ฌ๐,<a href='http://t.me/Dqautofl_Bot?startgroup=true'>๐จ๐๐ ๐ด๐ ๐ป๐ ๐๐๐๐ ๐ฎ๐๐๐๐ ๐จ๐๐ ๐ด๐๐๐ ๐ด๐ ๐จ๐ ๐จ๐๐๐๐ ๐ป๐๐๐๐</a>
โโโโโโโโโโโโโ
ยฉ๏ธMแดษชษดแดแดษชษดแดD Bส: <a href="https://t.me/pro_editor_tg"> ๐ซ๐บ๐๐๐หกแตหกหกแตหข </a>"""
  

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')

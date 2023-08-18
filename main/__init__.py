#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("29755735", default=None, cast=int)
API_HASH = 38959d422b051002e565b6faff2482be", default=None)
BOT_TOKEN = config("6662882347:AAHdXLu62pz4jTlgylXFNpVOEwuyN45VBto", default=None)
SESSION = config("BQHGCVcAPcvZEtdWsJcwNz-_vWXG6fQcFbC_CuGoLXgepV-QQoDarT6XdOg-29inOnJ46reKo3zSmrLAjDsRk_sbkeLdA-xymDEoX5lqOELNnItvjB3Az--7cKvXO56v3MKU1JjrFOVI7mqiRfLoU36WsqDvH17JMF1GM8uj_eefEic2rugLDCrU1Cp_Ovg9DdnJKuydeA8aAyWerhWG6FKSfdjxsaL_ODe2WvP0rsJkVgOxLKpn8-BG34LTNTVCQmq3Iea94-2BIuLKPIBIWM-Vv5_8tNBr1GMkylDVt4k89dhe08nj_sxhmmPNkCf2ZGBjX22lN5nT2IpqVEGtxJ8rsRYSvgAAAAEqU1CJAA", default=None)
FORCESUB = config("save_my_r", default=None)
AUTH = config("5005070473", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)

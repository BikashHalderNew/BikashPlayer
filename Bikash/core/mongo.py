# Powered By BikashHalder Or Aditya Halder IF You Fresh Any Problem To Contact The BgtRobot Owner

from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

from Bikash import config

from ..logging import LOGGER

TEMP_MONGODB = "mongodb+srv://bikashhalder123:bikash143@cluster0.u6kvanf.mongodb.net/?retryWrites=true&w=majority"


if config.MONGO_DB_URI is None:
    LOGGER(__name__).warning(
        "🌺 𝐍𝐨 MONGO DB URL 𝐅𝐨𝐮𝐧𝐝..❌ 𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐖𝐢𝐥𝐥 𝐖𝐨𝐫𝐤 𝐎𝐧 @BikashHalder MONGO 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 🇮🇳"
    )
    temp_client = Client(
        "BikashX",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()
    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)
    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]
else:
    _mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URI)
    mongodb = _mongo_async_.Bikashh
    pymongodb = _mongo_sync_.Bikashh

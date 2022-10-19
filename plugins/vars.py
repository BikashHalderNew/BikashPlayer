# Powered By @BikashHalder @AdityaHalder
# ©️ Copy Right By Bikash Halder Or Aditya Halder
# Any Problem To Report @Bgt_Chat or @AdityaDiscus
# Bot Owner @BikashHalder Or @AdityaHalder

import asyncio

from pyrogram import filters

from Bikash import config
from Bikash.strings import get_command
from Bikash import app
from Bikash.misc import SUDOERS
from Bikash.utils.database.memorydatabase import get_video_limit
from Bikash.utils.formatters import convert_bytes

VARS_COMMAND = get_command("VARS_COMMAND")


@app.on_message(filters.command(VARS_COMMAND) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "🌷 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐂𝐨𝐧𝐟𝐢𝐠 🌷"
    )
    v_limit = await get_video_limit()
    bot_name = config.MUSIC_BOT_NAME
    up_r = f"[𝐑𝐞𝐩𝐨 🇮🇳]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    cm = config.CLEANMODE_DELETE_MINS
    auto_sug = config.AUTO_SUGGESTION_TIME
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "𝐘𝐞𝐬 ✅"
    else:
        ass = "𝐍𝐨 ❌"
    if config.PRIVATE_BOT_MODE == str(True):
        pvt = "𝐘𝐞𝐬 ✅"
    else:
        pvt = "𝐍𝐨 ✅"
    if config.AUTO_SUGGESTION_MODE == str(True):
        a_sug = "𝐘𝐞𝐬 ✅"
    else:
        a_sug = "𝐍𝐨 ❌"
    if config.AUTO_DOWNLOADS_CLEAR == str(True):
        down = "𝐘𝐞𝐬 ✅"
    else:
        down = "𝐍𝐨 ❌"

    if not config.GITHUB_REPO:
        git = "𝐍𝐨 ❌"
    else:
        git = f"[𝐑𝐞𝐩𝐨 🇮🇳]({config.GITHUB_REPO})"
    if not config.START_IMG_URL:
        start = "𝐍𝐨 ❌"
    else:
        start = f"[𝐈𝐦𝐚𝐠𝐞 🇮🇳]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "𝐍𝐨 ❌"
    else:
        s_c = f"[𝐂𝐡𝐚𝐧𝐧𝐞𝐥 📡]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "𝐍𝐨 ❌"
    else:
        s_g = f"[𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "𝐍𝐨 ❌"
    else:
        token = "𝐘𝐞𝐬 ✅"
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        sotify = "𝐍𝐨 ❌"
    else:
        sotify = "𝐘𝐞𝐬 ✅"
    owners = [str(ids) for ids in config.OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    text = f"""**🇮🇳 𝐌𝐔𝐒𝐈𝐂 𝐁𝐨𝐭 𝐂𝐨𝐧𝐟𝐢𝐠 💡:**
                    
                ❰ 𝐁𝐢𝐤𝐚𝐬𝐡 ⚜️ 𝐏𝐥𝐚𝐲𝐞𝐫 ❱
                    
**<u>🌷 𝐁𝐚𝐬𝐢𝐜 𝐂𝐨𝐧𝐟𝐢𝐠 𝐕𝐚𝐫𝐬 🌷:</u>**
**🌺 𝐁𝐢𝐤𝐚𝐬𝐡 𝐁𝐨𝐭 𝐍𝐚𝐦𝐞** : `{bot_name}`
**⏱️ 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 ** : `{play_duration} 𝐌𝐢𝐧𝐮𝐭𝐞𝐬`
**🎵 𝐒𝐨𝐧𝐠 𝐃𝐨𝐰𝐧𝐋𝐨𝐚𝐝 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 ** :` {song} 𝐌𝐢𝐧𝐮𝐭𝐞𝐬`
**♕︎ 𝐎𝐰𝐧𝐞𝐫 𝐢𝐝** : `{owner_id}`
    
**<u>🌷 𝐑𝐞𝐩𝐨 𝐂𝐨𝐧𝐟𝐢𝐠 𝐕𝐚𝐫𝐬 🌷:</u>**
**📡 𝐔𝐩𝐬𝐭𝐫𝐞𝐚𝐦 𝐑𝐞𝐩𝐨** : `{up_r}`
**🌷 𝐔𝐩𝐬𝐭𝐫𝐞𝐚𝐦 𝐁𝐫𝐚𝐧𝐜𝐡** : `{up_b}`
**🌺 𝐆𝐢𝐭𝐡𝐮𝐛 𝐑𝐞𝐩𝐨** :` {git}`
**🌺 𝐆𝐢𝐭 𝐓𝐨𝐤𝐞𝐧**:` {token}`


**<u>💥 𝐁𝐨𝐭 𝐂𝐨𝐧𝐟𝐢𝐠 𝐕𝐚𝐫𝐬 💥:</u>**
**🚶‍♂️ 𝐀𝐮𝐭𝐨 𝐋𝐞𝐚𝐯𝐢𝐧𝐠 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭** : `{ass}`
**🚶‍♂️ 𝐀𝐮𝐭𝐨 𝐋𝐞𝐚𝐯𝐞 𝐓𝐢𝐦𝐞** : `{auto_leave} 𝐒𝐞𝐜𝐨𝐧𝐝𝐬`
**🚶‍♂️ 𝐀𝐮𝐭𝐨 𝐒𝐮𝐠𝐠𝐞𝐬𝐭𝐢𝐨𝐧 𝐌𝐨𝐝𝐞** :` {a_sug}`
**🚶‍♂️ 𝐀𝐮𝐭𝐨 𝐒𝐮𝐠𝐠𝐞𝐬𝐭𝐢𝐨𝐧 𝐓𝐢𝐦𝐞** : `{auto_sug} 𝐒𝐞𝐜𝐨𝐧𝐝𝐬`
**🚶‍♂️ 𝐀𝐮𝐭𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 ** : `{down}`
**🔒 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐁𝐨𝐭 𝐌𝐨𝐝𝐞 ** : `{pvt}`
**📺 𝐘𝐓 𝐄𝐝𝐢𝐭 𝐒𝐥𝐞𝐞𝐩 ** : `{yt_sleep} 𝐒𝐞𝐜𝐨𝐧𝐝𝐬`
**💥 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐄𝐝𝐢𝐭 𝐒𝐥𝐞𝐞𝐩** :` {tg_sleep} 𝐒𝐞𝐜𝐨𝐧𝐝𝐬`
**✅ 𝐂𝐥𝐞𝐚𝐧𝐦𝐨𝐝 𝐌𝐢𝐧𝐬** : `{cm} 𝐌𝐢𝐧𝐮𝐭𝐞𝐬`
**📺 𝐕𝐢𝐝𝐞𝐨 𝐒𝐭𝐫𝐞𝐚𝐦 𝐋𝐢𝐦𝐢𝐭 ** : `{v_limit} 𝐂𝐡𝐚𝐭`
**🇮🇳 𝐒𝐞𝐯𝐞𝐫 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐋𝐢𝐦𝐢𝐭 ** :` {playlist_limit}`
**✅ 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐅𝐞𝐭𝐜𝐡 𝐋𝐢𝐦𝐢𝐭** :` {fetch_playlist}`

**<u>🥀 𝐒𝐩𝐨𝐭𝐢𝐟𝐲 𝐂𝐨𝐧𝐟𝐢𝐠 𝐕𝐚𝐫𝐬 🥀:</u>**
**📢 𝐒𝐩𝐨𝐭𝐢𝐟𝐲 𝐂𝐥𝐢𝐞𝐧𝐭 𝐢𝐝** :` {sotify}`
**📢 𝐒𝐩𝐨𝐭𝐢𝐟𝐲 𝐂𝐥𝐢𝐞𝐧𝐭 𝐒𝐞𝐜𝐫𝐞𝐭** : `{sotify}`

**<u>🔰 𝐏𝐥𝐚𝐲 𝐒𝐢𝐳𝐞 𝐂𝐨𝐧𝐟𝐢𝐠 𝐕𝐚𝐫𝐬 🥀:</u>**
**🌺 𝐓𝐠 𝐀𝐮𝐝𝐢𝐨 𝐟𝐢𝐥𝐞 𝐒𝐢𝐳𝐞 𝐋𝐢𝐦𝐢𝐭** :` {tg_aud}`
**🌺 𝐓𝐠 𝐕𝐢𝐝𝐞𝐨 𝐒𝐢𝐳𝐞 𝐋𝐢𝐦𝐢𝐭 ** :` {tg_vid}`

**<u>🥀 𝐄𝐱𝐭𝐫𝐚 𝐂𝐨𝐧𝐟𝐢𝐠 𝐕𝐚𝐫𝐬 🥀:</u>**
**𝐬𝐮𝐩𝐩𝐨𝐫𝐭_𝐂𝐡𝐚𝐧𝐧𝐞𝐥** : `{s_c}`
**𝐒𝐮𝐩𝐩𝐨𝐫𝐭_𝐆𝐫𝐨𝐮𝐩** : ` {s_g}`
**𝐒𝐭𝐚𝐫𝐭_𝐈𝐦𝐠_𝐔𝐫𝐥** : ` {start}`
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)

# Powered By BikashHalder Or Aditya Halder IF You Fresh Any Problem To Contact The BgtRobot Owner
# Powered By @BikashHalder @AdityaHalder
# ©️ Copy Right By Bikash Halder Or Aditya Halder
# Any Problem To Report @Bgt_Chat or @AdityaDiscus
# Bot Owner @BikashHalder Or @AdityaHalder

from pyrogram import filters
from pyrogram.types import Message

from Bikash.strings import get_command
from Bikash import app
from Bikash.misc import SUDOERS
from Bikash.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats)

# Commands
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")


@app.on_message(filters.command(ACTIVEVC_COMMAND) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text(
        "💥 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐀𝐜𝐭𝐢𝐯𝐞 𝐕𝐨𝐢𝐞𝐜 𝐂𝐡𝐚𝐭𝐬 🚴‍♂️\n\n🌷 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐅𝐞𝐰 𝐒𝐞𝐜..🥀"
    )
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "📌 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐂𝐡𝐚𝐭 🥀"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("🍁 𝐍𝐨 𝐀𝐜𝐭𝐢𝐯𝐞  𝐕𝐜 𝐎𝐧 𝐁𝐠𝐭 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 ❎")
    else:
        await mystic.edit_text(
            f"💖 𝐁𝐠𝐭 𝐌𝐮𝐬𝐢𝐜 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐀𝐜𝐯𝐢𝐭𝐞 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭𝐬 𝐋𝐢𝐬𝐭 🔰 :-**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(ACTIVEVIDEO_COMMAND) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text(
        "💥 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐀𝐜𝐭𝐢𝐯𝐞 𝐕𝐨𝐢𝐞𝐜 𝐂𝐡𝐚𝐭𝐬 🚴‍♂️\n\n🌷 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐅𝐞𝐰 𝐒𝐞𝐜..🥀"
    )
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "🥀 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐂𝐡𝐚𝐭 🥀"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("🍁 𝐍𝐨 𝐀𝐜𝐭𝐢𝐯𝐞  𝐕𝐜 𝐎𝐧 𝐁𝐠𝐭 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 ❎")
    else:
        await mystic.edit_text(
            f"💖 𝐁𝐠𝐭 𝐌𝐮𝐬𝐢𝐜 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐀𝐜𝐯𝐢𝐭𝐞 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭𝐬 𝐋𝐢𝐬𝐭 🔰 :-**\n\n{text}",
            disable_web_page_preview=True,
        )

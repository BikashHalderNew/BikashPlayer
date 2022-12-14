# Powered By @BikashHalder @AdityaHalder
# ÂŠī¸ Copy Right By Bikash Halder Or Aditya Halder
# Any Problem To Report @Bgt_Chat or @AdityaDiscus
# Bot Owner @BikashHalder Or @AdityaHalder

import asyncio

from pyrogram import filters
from pyrogram.types import CallbackQuery, Message

from Bikash.config import BANNED_USERS, MUSIC_BOT_NAME, adminlist, lyrical
from Bikash.strings import get_command
from Bikash import app
from Bikash.core.call import Bikashh
from Bikash.misc import db
from Bikash.utils.database import get_authuser_names, get_cmode
from Bikash.utils.decorators import (ActualAdminCB, AdminActual,
                                         language)
from Bikash.utils.formatters import alpha_to_int

### Multi-Lang Commands
RELOAD_COMMAND = get_command("RELOAD_COMMAND")
RESTART_COMMAND = get_command("RESTART_COMMAND")


@app.on_message(
    filters.command(RELOAD_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def reload_admin_cache(client, message: Message, _):
    try:
        chat_id = message.chat.id
        admins = await app.get_chat_members(
            chat_id, filter="administrators"
        )
        authusers = await get_authuser_names(chat_id)
        adminlist[chat_id] = []
        for user in admins:
            if user.can_manage_voice_chats:
                adminlist[chat_id].append(user.user.id)
        for user in authusers:
            user_id = await alpha_to_int(user)
            adminlist[chat_id].append(user_id)
        await message.reply_text(_["admin_20"])
    except:
        await message.reply_text(
            "đˇđđđĻđĸđ§ đđĸđŦđ­ đđđđĢđđŦđĄ đđđĸđĨđđ â, đđđ¤đ đđŽđĢđ đđ¨đŽ đđĢđ¨đĻđ¨đ­đđ đđĄđ đđĸđ¤đđŦđĄ đđŽđŦđĸđ đđ¨đ˛ â."
        )


@app.on_message(
    filters.command(RESTART_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminActual
async def restartbot(client, message: Message, _):
    mystic = await message.reply_text(
        f"đˇ đđĨđđđŦđ đđđĸđ­ đđđ° đđĸđ§đŽđ­đđŦ ,{MUSIC_BOT_NAME} đđŦ đđđŦđ­đđĢđ­đĸđ§đ  đđ§ đđĄđĸđŦ đđĄđđ­ âģī¸."
    )
    await asyncio.sleep(1)
    try:
        db[message.chat.id] = []
        await Bikashh.stop_stream(message.chat.id)
    except:
        pass
    chat_id = await get_cmode(message.chat.id)
    if chat_id:
        try:
            await app.get_chat(chat_id)
        except:
            pass
        try:
            db[chat_id] = []
            await Bikashh.stop_stream(chat_id)
        except:
            pass
    return await mystic.edit_text(
        f"đˇđđĸđ¤đđŦđĄ đđ¨đ­ đđŽđđđđŦđŦđđŽđĨđĨđ˛ đđđŦđ­đđĢđ­đđ â {MUSIC_BOT_NAME} đđŦ đđ¨đŽđĢ đđĄđđ­, đ¸ đđ¨đ° đđ­đđĢđ­đđ đđ¨đ­ đđ đđĸđ§ & đđĨđđ˛đĸđ§đ  đđ đđĸđ§ â..."
    )


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(
    filters.regex("stop_downloading") & ~BANNED_USERS
)
@ActualAdminCB
async def stop_download(client, CallbackQuery: CallbackQuery, _):
    message_id = CallbackQuery.message.message_id
    task = lyrical.get(message_id)
    if not task:
        return await CallbackQuery.answer(
            "đˇ đđ¨đ°đ§đđ¨đđ đđĨđĢđđđđ˛ đđ¨đ§đ â.", show_alert=True
        )
    if task.done() or task.cancelled():
        return await CallbackQuery.answer(
            "đˇ đđ¨đ°đ§đđ¨đđ đđĨđĢđđđđ˛ đđ¨đ§đ â  & đđđ§đđđĨ â.",
            show_alert=True,
        )
    if not task.done():
        try:
            task.cancel()
            try:
                lyrical.pop(message_id)
            except:
                pass
            await CallbackQuery.answer(
                "đ° đđ¨đ°đ§đđ¨đđ đđĨđ¨đŦđ â.", show_alert=True
            )
            return await CallbackQuery.edit_message_text(
                f"đ đđ¨đ°đ§đđ¨đđđĸđ§đ  đđĨđ¨đŦđđ đđ˛ {CallbackQuery.from_user.mention} â"
            )
        except:
            return await CallbackQuery.answer(
                "đˇ đđ¨đ°đ§đđ¨đđ đđĨđ¨đŦđ đđđĸđĨđđ â đđĨđ¨đŦđ đđ¨đ°đ§đđ¨đđđĸđ§đ ...", show_alert=True
            )
    await CallbackQuery.answer(
        "đˇ đđđĸđĨđđ đđ¨ đđđđ¨đ đ§đĸđŗđ đđĄđ đđ§đ đ¨đĸđ§đ  đđđŦđ¤ đ.", show_alert=True
    )

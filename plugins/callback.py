# Powered By @BikashHalder @AdityaHalder
# ©️ Copy Right By Bikash Halder Or Aditya Halder
# Any Problem To Report @Bgt_Chat or @AdityaDiscus
# Bot Owner @BikashHalder Or @AdityaHalder
# Powered By BikashHalder Or Aditya Halder IF You Fresh Any Problem To Contact The BgtRobot Owner

import random

from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup

from Bikash.config import (AUTO_DOWNLOADS_CLEAR, BANNED_USERS,
                    SOUNCLOUD_IMG_URL, STREAM_IMG_URL,
                    TELEGRAM_AUDIO_URL, TELEGRAM_VIDEO_URL, adminlist)
from Bikash import YouTube, app
from Bikash.core.call import Bikashh
from Bikash.misc import SUDOERS, db
from Bikash.utils.database import (is_active_chat,
                                       is_music_playing, set_loop,
                                       is_nonadmin_chat, music_off,
                                       music_on)
from Bikash.utils.decorators.language import languageCB
from Bikash.utils.formatters import seconds_to_min
from Bikash.utils.inline.play import (panel_markup_1,
                                          stream_markup,
                                          telegram_markup)
from Bikash.utils.stream.autoclear import auto_clean
from Bikash.utils.thumbnails import gen_thumb

wrong = {}


@app.on_callback_query(filters.regex("PanelMarkup") & ~BANNED_USERS)
@languageCB
async def markup_panel(client, CallbackQuery: CallbackQuery, _):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    videoid, chat_id = callback_request.split("|")
    chat_id = CallbackQuery.message.chat.id
    buttons = panel_markup_1(_, videoid, chat_id)
    try:
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except:
        return
    if chat_id not in wrong:
        wrong[chat_id] = {}
    wrong[chat_id][CallbackQuery.message.message_id] = False


@app.on_callback_query(filters.regex("MainMarkup") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    videoid, chat_id = callback_request.split("|")
    if videoid == str(None):
        buttons = telegram_markup(_, chat_id)
    else:
        buttons = stream_markup(_, videoid, chat_id)
    chat_id = CallbackQuery.message.chat.id
    try:
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except:
        return
    if chat_id not in wrong:
        wrong[chat_id] = {}
    wrong[chat_id][CallbackQuery.message.message_id] = True


downvote = {}
downvoters = {}


@app.on_callback_query(filters.regex("ADMIN") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    command, chat = callback_request.split("|")
    chat_id = int(chat)
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(
            _["general_6"], show_alert=True
        )
    mention = CallbackQuery.from_user.mention
    is_non_admin = await is_nonadmin_chat(
        CallbackQuery.message.chat.id
    )
    if not is_non_admin:
        if CallbackQuery.from_user.id not in SUDOERS:
            admins = adminlist.get(CallbackQuery.message.chat.id)
            if not admins:
                return await CallbackQuery.answer(
                    _["admin_18"], show_alert=True
                )
            else:
                if CallbackQuery.from_user.id not in admins:
                    return await CallbackQuery.answer(
                        _["admin_19"], show_alert=True
                    )
    if command == "Pause":
        if not await is_music_playing(chat_id):
            return await CallbackQuery.answer(
                _["admin_1"], show_alert=True
            )
        await CallbackQuery.answer()
        await music_off(chat_id)
        await Bikashh.pause_stream(chat_id)
        await CallbackQuery.message.reply_text(
            _["admin_2"].format(mention)
        )
    elif command == "Resume":
        if await is_music_playing(chat_id):
            return await CallbackQuery.answer(
                _["admin_3"], show_alert=True
            )
        await CallbackQuery.answer()
        await music_on(chat_id)
        await Bikashh.resume_stream(chat_id)
        await CallbackQuery.message.reply_text(
            _["admin_4"].format(mention)
        )
    elif command == "Stop" or command == "End":
        await CallbackQuery.answer()
        await Bikashh.stop_stream(chat_id)
        await set_loop(chat_id, 0)
        await CallbackQuery.message.reply_text(
            _["admin_9"].format(mention)
        )
    elif command == "Loop":
        await CallbackQuery.answer()
        await set_loop(chat_id, 3)
        await CallbackQuery.message.reply_text(
            _["admin_25"].format(mention, 3)
        )
    elif command == "Shuffle":
        check = db.get(chat_id)
        if not check:
            return await CallbackQuery.answer(
                _["admin_21"], show_alert=True
            )
        try:
            popped = check.pop(0)
        except:
            return await CallbackQuery.answer(
                _["admin_22"], show_alert=True
            )
        check = db.get(chat_id)
        if not check:
            check.insert(0, popped)
            return await CallbackQuery.answer(
                _["admin_22"], show_alert=True
            )
        await CallbackQuery.answer()
        random.shuffle(check)
        check.insert(0, popped)
        await CallbackQuery.message.reply_text(
            _["admin_23"].format(mention)
        )
    elif command == "Skip":
        check = db.get(chat_id)
        txt = f"🌷 𝐒𝐨𝐧𝐠 𝐒𝐤𝐢𝐩𝐩𝐞𝐝 𝐁𝐲 ⏩ {mention} !"
        popped = None
        try:
            popped = check.pop(0)
            if popped:
                if AUTO_DOWNLOADS_CLEAR == str(True):
                    await auto_clean(popped)
            if not check:
                await CallbackQuery.edit_message_text(
                    f"🌷 𝐒𝐨𝐧𝐠 𝐒𝐤𝐢𝐩𝐩𝐞𝐝 𝐁𝐲 ⏩ {mention} !"
                )
                await CallbackQuery.message.reply_text(
                    _["admin_10"].format(mention)
                )
                try:
                    return await Bikashh.stop_stream(chat_id)
                except:
                    return
        except:
            try:
                await CallbackQuery.edit_message_text(
                    f"🌷 𝐒𝐨𝐧𝐠 𝐒𝐤𝐢𝐩𝐩𝐞𝐝 𝐁𝐲 ⏩ {mention} !"
                )
                await CallbackQuery.message.reply_text(
                    _["admin_10"].format(mention)
                )
                return await Bikashh.stop_stream(chat_id)
            except:
                return
        await CallbackQuery.answer()
        queued = check[0]["file"]
        title = (check[0]["title"]).title()
        user = check[0]["by"]
        streamtype = check[0]["streamtype"]
        videoid = check[0]["vidid"]
        status = True if str(streamtype) == "video" else None
        db[chat_id][0]["played"] = 0
        if "live_" in queued:
            n, link = await YouTube.video(videoid, True)
            if n == 0:
                return await CallbackQuery.message.reply_text(
                    _["admin_11"].format(title)
                )
            try:
                await Bikashh.skip_stream(chat_id, link, video=status)
            except Exception:
                return await CallbackQuery.message.reply_text(
                    _["call_9"]
                )
            button = telegram_markup(_, chat_id)
            img = await gen_thumb(videoid)
            run = await CallbackQuery.message.reply_photo(
                photo=img,
                caption=_["stream_1"].format(
                    user,
                    f"https://t.me/{app.username}?start=info_{videoid}",
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
            await CallbackQuery.edit_message_text(txt)
        elif "vid_" in queued:
            mystic = await CallbackQuery.message.reply_text(
                _["call_10"], disable_web_page_preview=True
            )
            try:
                file_path, direct = await YouTube.download(
                    videoid,
                    mystic,
                    videoid=True,
                    video=status,
                )
            except:
                return await mystic.edit_text(_["call_9"])
            try:
                await Bikashh.skip_stream(
                    chat_id, file_path, video=status
                )
            except Exception:
                return await mystic.edit_text(_["call_9"])
            button = stream_markup(_, videoid, chat_id)
            img = await gen_thumb(videoid)
            run = await CallbackQuery.message.reply_photo(
                photo=img,
                caption=_["stream_1"].format(
                    user,
                    f"https://t.me/{app.username}?start=info_{videoid}",
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "stream"
            await CallbackQuery.edit_message_text(txt)
            await mystic.delete()
        elif "index_" in queued:
            try:
                await Bikashh.skip_stream(
                    chat_id, videoid, video=status
                )
            except Exception:
                return await CallbackQuery.message.reply_text(
                    _["call_9"]
                )
            button = telegram_markup(_, chat_id)
            run = await CallbackQuery.message.reply_photo(
                photo=STREAM_IMG_URL,
                caption=_["stream_2"].format(user),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
            await CallbackQuery.edit_message_text(txt)
        else:
            try:
                await Bikashh.skip_stream(chat_id, queued, video=status)
            except Exception:
                return await CallbackQuery.message.reply_text(
                    _["call_9"]
                )
            if videoid == "telegram":
                button = telegram_markup(_, chat_id)
                run = await CallbackQuery.message.reply_photo(
                    photo=TELEGRAM_AUDIO_URL
                    if str(streamtype) == "audio"
                    else TELEGRAM_VIDEO_URL,
                    caption=_["stream_3"].format(
                        title, check[0]["dur"], user
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "tg"
            elif videoid == "soundcloud":
                button = telegram_markup(_, chat_id)
                run = await CallbackQuery.message.reply_photo(
                    photo=SOUNCLOUD_IMG_URL
                    if str(streamtype) == "audio"
                    else TELEGRAM_VIDEO_URL,
                    caption=_["stream_3"].format(
                        title, check[0]["dur"], user
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "tg"
            else:
                button = stream_markup(_, videoid, chat_id)
                img = await gen_thumb(videoid)
                run = await CallbackQuery.message.reply_photo(
                    photo=img,
                    caption=_["stream_1"].format(
                        user,
                        f"https://t.me/{app.username}?start=info_{videoid}",
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "stream"
            await CallbackQuery.edit_message_text(txt)
    else:
        playing = db.get(chat_id)
        if not playing:
            return await CallbackQuery.answer(
                _["queue_2"], show_alert=True
            )
        duration_seconds = int(playing[0]["seconds"])
        if duration_seconds == 0:
            return await CallbackQuery.answer(
                _["admin_30"], show_alert=True
            )
        file_path = playing[0]["file"]
        if "index_" in file_path or "live_" in file_path:
            return await CallbackQuery.answer(
                _["admin_30"], show_alert=True
            )
        duration_played = int(playing[0]["played"])
        if int(command) in [1, 2]:
            duration_to_skip = 10
        else:
            duration_to_skip = 30
        duration = playing[0]["dur"]
        if int(command) in [1, 3]:
            if (duration_played - duration_to_skip) <= 10:
                bet = seconds_to_min(duration_played)
                return await CallbackQuery.answer(
                    f"🤖 𝐈 𝐚𝐦 𝐍𝐨𝐭 𝐀𝐛𝐥𝐞 𝐓𝐨 𝐒𝐞𝐞𝐤 𝐃𝐮𝐞 𝐓𝐨 𝐓𝐨𝐭𝐚𝐥 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 𝐇𝐚𝐬 𝐁𝐞𝐞𝐧 𝐄𝐱𝐜𝐞𝐞𝐝𝐞𝐝.🔰\n\n✅ 𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐏𝐥𝐚𝐲𝐞𝐝**{bet}** 🔊 𝐌𝐢𝐧𝐬 𝐎𝐮𝐭 𝐎𝐟 **{duration}** 𝐌𝐢𝐧𝐬. 🌷",
                    show_alert=True,
                )
            to_seek = duration_played - duration_to_skip + 1
        else:
            if (
                duration_seconds
                - (duration_played + duration_to_skip)
            ) <= 10:
                bet = seconds_to_min(duration_played)
                return await CallbackQuery.answer(
                    f"🤖 𝐈 𝐚𝐦 𝐍𝐨𝐭 𝐀𝐛𝐥𝐞 𝐓𝐨 𝐒𝐞𝐞𝐤 𝐃𝐮𝐞 𝐓𝐨 𝐓𝐨𝐭𝐚𝐥 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 𝐇𝐚𝐬 𝐁𝐞𝐞𝐧 𝐄𝐱𝐜𝐞𝐞𝐝𝐞𝐝.🔰\n\n✅ 𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐏𝐥𝐚𝐲𝐞𝐝** {bet}** 🔊 𝐌𝐢𝐧𝐬 𝐎𝐮𝐭 𝐎𝐟 **{duration}** 𝐌𝐢𝐧𝐬 🌷",
                    show_alert=True,
                )
            to_seek = duration_played + duration_to_skip + 1
        await CallbackQuery.answer()
        mystic = await CallbackQuery.message.reply_text(_["admin_32"])
        if "vid_" in file_path:
            n, file_path = await YouTube.video(
                playing[0]["vidid"], True
            )
            if n == 0:
                return await mystic.edit_text(_["admin_30"])
        try:
            await Bikashh.seek_stream(
                chat_id,
                file_path,
                seconds_to_min(to_seek),
                duration,
                playing[0]["streamtype"],
            )
        except:
            return await mystic.edit_text(_["admin_34"])
        if int(command) in [1, 3]:
            db[chat_id][0]["played"] -= duration_to_skip
        else:
            db[chat_id][0]["played"] += duration_to_skip
        string = _["admin_33"].format(seconds_to_min(to_seek))
        await mystic.edit_text(
            f"{string}\n\n✅ 𝐂𝐡𝐚𝐧𝐠𝐞 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐁𝐲 : {mention} 🌷"
        )

# Powered By BikashHalder Or Aditya Halder IF You Fresh Any Problem To Contact The BgtRobot Owner

from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup,
                            InlineQueryResultPhoto)
from youtubesearchpython.__future__ import VideosSearch

from Bikash.config import BANNED_USERS, MUSIC_BOT_NAME
from Bikash import app
from Bikash.utils.inlinequery import answer


@app.on_inline_query(~BANNED_USERS)
async def inline_query_handler(client, query):
    text = query.query.strip().lower()
    answers = []
    if text.strip() == "":
        try:
            await client.answer_inline_query(
                query.id, results=answer, cache_time=10
            )
        except:
            return
    else:
        a = VideosSearch(text, limit=20)
        result = (await a.next()).get("result")
        for x in range(15):
            title = (result[x]["title"]).title()
            duration = result[x]["duration"]
            views = result[x]["viewCount"]["short"]
            thumbnail = result[x]["thumbnails"][0]["url"].split("?")[
                0
            ]
            channellink = result[x]["channel"]["link"]
            channel = result[x]["channel"]["name"]
            link = result[x]["link"]
            published = result[x]["publishedTime"]
            description = f"{views} | {duration} Mins | {channel}  | {published}"
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="📺 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 📺",
                            url=link,
                        )
                    ],
                ]
            )
            searched_text = f"""
📌 **𝐓𝐢𝐭𝐥𝐞:** [{title}]({link})

⏳ **𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧:** {duration} Mins
👀 **𝐕𝐢𝐞𝐰𝐬:** `{views}`
⏰ **𝐏𝐮𝐛𝐥𝐢𝐬𝐡𝐞𝐝 𝐓𝐢𝐦𝐞 :** {published}
📡 **𝐂𝐡𝐚𝐧𝐧𝐞𝐥:** {channel}
📎 **𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐋𝐢𝐧𝐤:** [👀 𝐒𝐞𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 📺]({channellink})

🔍 ** 𝐈𝐧𝐥𝐢𝐧𝐞 𝐒𝐞𝐚𝐫𝐜𝐡 𝐁𝐲 🌷 {MUSIC_BOT_NAME}**"""
            answers.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    thumb_url=thumbnail,
                    description=description,
                    caption=searched_text,
                    reply_markup=buttons,
                )
            )
        try:
            return await client.answer_inline_query(
                query.id, results=answers
            )
        except:
            return

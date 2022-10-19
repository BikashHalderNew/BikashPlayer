from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="🌷️ 𝐏𝐚𝐮𝐬𝐞 ▶️️",
            description=f"🌷 𝐏𝐚𝐮𝐬𝐞 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐕𝐨𝐢𝐜𝐞  𝐂𝐡𝐚𝐭 𝐐𝐮𝐞𝐫𝐲 ⏸️",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="🌷 𝐑𝐞𝐬𝐮𝐦𝐞 ⏸️",
            description=f"🌷 𝐑𝐞𝐬𝐮𝐦𝐞 𝐓𝐡𝐞 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭  𝐐𝐮𝐞𝐫𝐲 ⏸️",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="🌷 𝐒𝐤𝐢𝐩 ⏩",
            description=f"🌷 𝐒𝐤𝐢𝐩 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐐𝐮𝐞𝐫𝐲 ▶️",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/skip", "/next"),
        ),
        InlineQueryResultArticle(
            title="🌷 𝐌𝐮𝐭𝐞 ⏺️",
            description=f"🌷 𝐌𝐮𝐭𝐞 𝐎𝐧𝐠𝐨𝐢𝐧𝐠 𝐏𝐥𝐚𝐲𝐨𝐮𝐭 𝐨𝐧 𝐆𝐫𝐨𝐮𝐩 𝐕𝐜 ⏺️",
            thumb_url="https://telegra.ph/file/3078794f9341ffd582e18.png",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="🌷 𝐄𝐍𝐃 ❌",
            description="🌷 𝐄𝐧𝐝 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 ❌",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/end", "/x"),
        ),
        InlineQueryResultArticle(
            title="🌷 𝐒𝐡𝐮𝐟𝐟𝐥𝐞 🔴",
            description="🌷 𝐒𝐡𝐮𝐟𝐟𝐥𝐞 𝐐𝐮𝐞𝐮𝐞𝐝 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐒𝐨𝐧𝐠 𝐈𝐧 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 🔴",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="🌷 𝐒𝐞𝐞𝐤 🔰",
            description="🌷 𝐒𝐞𝐞𝐤 𝐎𝐧𝐠𝐨𝐢𝐧𝐠 𝐒𝐭𝐫𝐞𝐚𝐦 𝐓𝐨 𝐀 𝐒𝐩𝐞𝐜𝐢𝐟𝐢𝐜 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 ⏱️.",
            thumb_url="https://telegra.ph/file/cd25ec6f046aa8003cfee.png",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="🌷 𝐋𝐨𝐨𝐩 🛡️",
            description="🌷 𝐋𝐨𝐨𝐩 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐓𝐫𝐚𝐜𝐤 🛡 𝐔𝐬𝐚𝐠𝐞: /loop [enable|disable].",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)

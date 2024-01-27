from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="✨𝑯𝒆𝒍𝒑✨", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="☢ 𝐒𝙴𝚃 ☢", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="✨𝑮𝒓𝒐𝒖𝒑✨", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="✨𝑮𝒓𝒐𝒖𝒑✨", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="✨𝑴𝒂𝒊𝒏 𝑪𝒉𝒂𝒏𝒏𝒆𝒍✨", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="✨𝑭𝒆𝒂𝒕𝒖𝒓𝒆𝒔✨", callback_data="settings_back_helper")
        ],
    ]
    return buttons

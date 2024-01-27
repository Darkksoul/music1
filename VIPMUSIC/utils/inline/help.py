from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from VIPMUSIC import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
        InlineKeyboardButton(
            text="✨𝑴𝒐𝒓𝒆✨", callback_data="help_callback hb13"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✨𝑨𝒅𝒎𝒊𝒏✨",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="✨𝑨𝒖𝒕𝒉✨",
                    callback_data="help_callback hb2",
                ),
            
                InlineKeyboardButton(
                    text="✨𝑩𝒍𝒐𝒄𝒌✨",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✨𝑮𝒄𝒂𝒔𝒕✨",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="✨𝑮𝒃𝒂𝒏✨",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="✨𝑳𝒚𝒓𝒊𝒄𝒔✨",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✨𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕✨",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="✨𝑽𝒐𝒊𝒄𝒆 𝑪𝒉𝒂𝒕✨",
                    callback_data="help_callback hb10",
                ),
            ],
            [
           
                InlineKeyboardButton(
                    text="✨𝑷𝒍𝒂𝒚✨",
                    callback_data="help_callback hb8",
                ),
            
            
                InlineKeyboardButton(
                    text="✨𝑺𝒖𝒅𝒐✨",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✨𝑺𝒕𝒂𝒓𝒕✨",
                    callback_data="help_callback hb11",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
                InlineKeyboardButton(
                    text="✨𝑴𝒐𝒓𝒆✨", callback_data="help_callback hb13"
                )

            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✨𝑯𝒆𝒍𝒑✨",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons

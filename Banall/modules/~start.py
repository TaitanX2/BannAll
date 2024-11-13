import time
import random
import requests
from Banall import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup , CallbackQuery 

START_PIC = [
    "https://te.legra.ph/file/b7a0900b8bc08a83e481e.jpg",
    "https://te.legra.ph/file/0535d3bf2d554248916af.jpg",
    
]
ban_txt = """
ʜᴇʟʟᴏ **{}**
ɪ ʜᴀᴠᴇ sᴏᴍᴇ ɪɴᴛᴇʀᴇsᴛɪɴɢ ᴘʟᴜɢɪɴs ʏᴏᴜ sʜᴏᴜʟᴅ ᴛʀʏ ɪᴛ ʙʏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ.
ᴀᴅᴅ ᴍᴇ ɪɴ ᴏᴛʜᴇʀs ɢʀᴏᴜᴘ ᴛᴏ ᴅᴇsᴛʀᴏʏ ɪᴛ.
ᴘᴏᴡᴇʀ ʙʏ : @ll_BAD_MUNDA_ll
"""

help_txt = """
» ᴛᴀᴘ ᴛᴏ sᴇᴇ ᴄᴏᴍᴍᴀɴᴅs
"""
killall_txt = """
**ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ɪɴ ɢʀᴏᴜᴘs**

1. ᴀᴅᴅ ʏᴏᴜʀ ʙᴏᴛ ɪɴ ᴡʜɪᴄʜ ɢʀᴏᴜᴘ.
2. ᴍᴀᴋᴇ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴀʟʟ ᴘᴏᴡᴇʀ ᴛʜᴇ ʙᴏᴛ.
3. ɴᴏᴡ ꜱᴇɴᴅ ᴍᴇꜱꜱᴇɢᴇ ɪɴ ɢʀᴏᴜᴘ : <code>hii</code>

ɴᴏᴡ ʙᴏᴛ ᴡɪʟʟ ᴡᴏʀᴋɪɴɢ  ✅.
"""
app_buttons = [

                [ 
                    InlineKeyboardButton("ʜᴇʟᴘ", callback_data="banall_"),
        
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home_"),
                    InlineKeyboardButton("⟲ ᴄʟᴏꜱᴇ ⟳", callback_data="close_data")
                ]
                ]

back_buttons  = [[
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="help_"),                    
                ]]

button = InlineKeyboardMarkup([
        
        [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/PBX_CHAT"),    
        ],
    [
           InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_"),    
      ]
    
])

@app.on_message(filters.command(["start"], prefixes=[".","/","!"]) & filters.private)
async def start(_, message):
    await message.reply_photo(
        photo=random.choice(START_PIC),
        caption=ban_txt.format(message.from_user.mention, message.from_user.id),
        reply_markup=button
    )    

@app.on_callback_query()
async def cb_handler(client, query):
    if query.data=="home_":
        buttons =  [
            [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/ll_THE_BAD_BOT_ll"),    
        ],
            [
                InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_")
            ]    
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                ban_txt.format(query.from_user.mention, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="help_":        
        reply_markup = InlineKeyboardMarkup(app_buttons)
        try:
            await query.edit_message_text(
                help_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass



    elif query.data=="banall_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                killall_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
            
    elif query.data=="close_data":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass


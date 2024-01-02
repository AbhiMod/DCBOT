from pyrogram import Client, filters
from pyrogram.types import Message
from DCBOT import app
from DCBOT.utils.database import get_served_chats
from config import LOGS
import random
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)


async def lul_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)


@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        matlabi_jhanto = message.chat.title
        served_chats = len(await get_served_chats())
        chat_id = message.chat.id
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        lemda_text = f"🌹 ʙᴏᴛ ᴀᴅᴅᴇᴅ ᴛᴏ ɴᴇᴡ ɢʀᴏᴜᴘ ..\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ **ᴄʜᴀᴛ** › : {matlabi_jhanto}\n┣★ **ᴄʜᴀᴛ ɪᴅ** › : {chat_id}\n┣★ **ᴄʜᴀᴛ ᴜɴᴀᴍᴇ** › : {chatusername}\n┣★ **ᴛᴏᴛᴀʟ ᴄʜᴀᴛ** › : {served_chats}\n┣★ **ᴀᴅᴅᴇᴅ ʙʏ** › :\n┗━━━ {added_by}"
        await lul_message(LOGS, lemda_text)
        
@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        lemda_text = f"ʙᴏᴛ ʟᴇꜰᴛ ᴛᴏ ɢʀᴏᴜᴘ ..\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ **ᴄʜᴀᴛ** › : {title}\n┣★ **ᴄʜᴀᴛ ɪᴅ** › : {chat_id}\n┣★ **ʙᴏᴛ ᴜɴᴀᴍᴇ** › : {username}\n┣★ **ʀᴇᴍᴏᴠᴇᴅ ʙʏ** › :\n┗━━━ {remove_by}"
        await app.send_message(LOGS, lemda_text)


import asyncio
import random
import re
import json
import base64
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from asyncio.exceptions import TimeoutError
from telethon import events
from ..sql_helper.memes_sql import get_link, add_link, delete_link, BASE, SESSION, AljokerLink
from telethon.errors.rpcerrorlist import YouBlockedUserError
from VIPABH import ABH
from abh import __init__.py
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID


plugin_category = "tools"
aljoker_links = {}

# BOTLOG_CHATID = Config.BOTLOG_CHATID

@ABH.on(admin_cmd(outgoing=True, pattern="لطمية$"))
async def jepThe(theme):
    try:
        rl = random.randint(19, 170)        
        # rl = random.randint(999, 988)        
        url = f"https://t.me/x04ou/{rl}"
        await theme.ABH.send_file(
            theme.chat_id, 
            url, 
            caption="᯽︙  اذكر القائم", 
            parse_mode="html"
        )        
        await theme.delete()
    except Exception as e:
        error_message = str(e)
        message_link = f"https://t.me/c/{theme.chat_id}/{theme.id}" 
        
        await theme.ABH.send_message(
            BOTLOG_CHATID,
            f"❌ **حدث خطأ أثناء إرسال اللطمية**\n",
            f"رابط الرسالة: {message_link}\n",
            f"تفاصيل الخطأ: {error_message}",
            f"رابط اللطمية الخاطئة: {url}"
        )
        await theme.edit(" حدث خطأ أثناء إرسال اللطمية.")

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
from ..helpers.utils import reply_id
plugin_category = "tools"
aljoker_links = {}

@ABH.on(admin_cmd(outgoing=True, pattern="لطمية$"))
async def jepThe(theme):
    rl = random.randint(19, 170)
    url = f"https://t.me/x04ou/{rl}"
    await theme.client.send_file(theme.chat_id, url, caption="᯽︙  اذكر القائم ", parse_mode="html")
    await theme.delete()


@ABH.on(admin_cmd(pattern="محرم ?(.*)"))
async def _(event):
    await event.edit("**- يتم جلب النتيجة**")
    async with event.client.conversation("@tt_tabot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=7308514832)
            )
            await conv.send_message("محرم")
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("** وحاول مجددا**")
            return
        await event.edit(f"- {response.message.message}\n @tt_tabot")

@ABH.on(admin_cmd(pattern="احسب ?(.*)"))
async def _(event):
    input_equation = event.pattern_match.group(1)  # التقاط المعادلة المُدخلة
    if not input_equation:
        await event.edit("**✾╎يرجى إدخال المعادلة بعد الأمر**")
        return

    await event.edit("**- يتم جلب النتيجة**")
    async with event.client.conversation("@NewCalcuBot") as conv:
        try:
            await conv.send_message(input_equation)  # إرسال المعادلة إلى البوت
            response = await conv.wait_event(
                events.NewMessage(incoming=True, from_users=6878741756)  # معرف @NewCalcuBot
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            result = response.message.text
            await event.edit(f"**{result}**")
        except YouBlockedUserError:
            await event.edit("**✾╎يرجى التحقق من عدم حظر البوت @NewCalcuBot وحاول مجددا**")

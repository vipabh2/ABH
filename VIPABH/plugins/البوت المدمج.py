import asyncio
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import get_user_from_event, sanga_seperator
from ..helpers.utils import _format
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import GetMessagesRequest
from telethon.tl.functions.users import GetFullUserRequest
from VIPABH import ABH

@ABH.on(admin_cmd(pattern="احسب ?(.*)"))
async def _(event):
    input_equation = event.pattern_match.group(1)  
    if not input_equation:
        await event.edit("**✾╎يرجى إدخال المعادلة بعد الأمر**")
        return

    await event.edit("**- يتم جلب النتيجة**")
    async with event.client.conversation("@NewCalcuBot") as conv:
        try:
            await conv.send_message(input_equation) 
            response = await conv.wait_event(
                events.NewMessage(incoming=True, from_users=6878741756)  
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            result = response.message.text
            await event.edit(f"**{result}**")
        except YouBlockedUserError:
            await event.edit("**✾╎يرجى التحقق من عدم حظر البوت @NewCalcuBot وحاول مجددا**")


@ABH.on(admin_cmd(pattern="رجب"))
async def _(event):

    await event.edit("**- يتم جلب النتيجة**")
    async with event.client.conversation("@TT_TABOT") as conv:
        try:
            await conv.send_message("رجب") 
            response = await conv.wait_event(
                events.NewMessage(incoming=True, from_users=7308514832)  
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            result = response.message.text
            await event.edit(f"**{result}**")
        except YouBlockedUserError:
            await event.edit("**✾╎يرجى التحقق من عدم حظر البوت @NewCalcuBot وحاول مجددا**")

@ABH.on(admin_cmd(pattern="شعبان"))
async def _(event):

    await event.edit("**- يتم جلب النتيجة**")
    async with event.client.conversation("@TT_TABOT") as conv:
        try:
            await conv.send_message("شعبان") 
            response = await conv.wait_event(
                events.NewMessage(incoming=True, from_users=7308514832)  
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            result = response.message.text
            await event.edit(f"**{result}**")
        except YouBlockedUserError:
            await event.edit("**✾╎يرجى التحقق من عدم حظر البوت @NewCalcuBot وحاول مجددا**")

@ABH.on(admin_cmd(pattern="رمضان"))
async def _(event):

    await event.edit("**- يتم جلب النتيجة**")
    async with event.client.conversation("@TT_TABOT") as conv:
        try:
            await conv.send_message("رمضان") 
            response = await conv.wait_event(
                events.NewMessage(incoming=True, from_users=7308514832)  
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            result = response.message.text
            await event.edit(f"**{result}**")
        except YouBlockedUserError:
            await event.edit("**✾╎يرجى التحقق من عدم حظر البوت @NewCalcuBot وحاول مجددا**")

@ABH.on(admin_cmd(pattern="محرم"))
async def _(event):

    await event.edit("**- يتم جلب النتيجة**")
    async with event.client.conversation("@TT_TABOT") as conv:
        try:
            await conv.send_message("محرم") 
            response = await conv.wait_event(
                events.NewMessage(incoming=True, from_users=7308514832)  
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            result = response.message.text
            await event.edit(f"**{result}**")
        except YouBlockedUserError:
            await event.edit("**✾╎يرجى التحقق من عدم حظر البوت @NewCalcuBot وحاول مجددا**")


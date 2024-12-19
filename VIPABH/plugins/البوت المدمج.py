import asyncio
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import get_user_from_event, sanga_seperator
from ..helpers.utils import _format
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import GetMessagesRequest
from telethon.tl.functions.users import GetFullUserRequest
from VIPABH import ABH

# @ABH.on(admin_cmd(pattern="(حساب|احسب)$"))
# @ABH.on(admin_cmd(pattern="احسب ?(.*)"))
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


@l313l.on(admin_cmd(pattern="حالتي ?(.*)"))
async def _(event):
    await event.edit("**- يتم التاكد من حالتك اذا كنت محظور او لا**")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("** اولا الغي حظر @SpamBot وحاول مجددا**")
            return
        await event.edit(f"- {response.message.message}\n @jepthon")

@ABH.on(admin_cmd(pattern="شعبان ?(.*)"))
async def _(event):
    await event.edit("**- يتم جلب النتيجة**")
    async with event.client.conversation("@tt_tabot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=7308514832)
            )
            await conv.send_message("شعبان")
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("** وحاول مجددا**")
            return
        await event.edit(f"- {response.message.message}\n @tt_tabot")

@ABH.on(admin_cmd(pattern="رمضان ?(.*)"))
async def _(event):
    await event.edit("**- يتم جلب النتيجة**")
    async with event.client.conversation("@tt_tabot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=7308514832)
            )
            await conv.send_message("رمضان")
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("** وحاول مجددا**")
            return
        await event.edit(f"- {response.message.message}\n @tt_tabot")

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
            


@ABH.on(admin_cmd(pattern="ايميل وهمي(?: |$)(.*)"))
async def _(event):
    chat = "@TempMailBot"
    geez = await event.edit("**جاري انشاء بريد ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=220112646)
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            ABHmail = response.reply_markup.rows[2].buttons[0].url
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await geez.edit("**الغي حظر @TempMailBot  و حاول مجددا**")
            return
        await event.edit(
            f"الايميل الخاص هو `{response.message.message}`\n[ اضغط هنا لرؤية من رسائل الايميل الواردة]({ABHmail})"
        )
       

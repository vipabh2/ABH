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
# ياقائم آل محمد
from JoKeRUB import l313l
from ..helpers.utils import reply_id
plugin_category = "tools"
aljoker_links = {}
@l313l.on(admin_cmd(pattern="رجب ?(.*)"))
async def _(event):
    await event.edit("**- يتم جلب النتيجة**")
    async with event.client.conversation("@tt_tabot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=7308514832)
            )
            await conv.send_message("رجب")
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("** وحاول مجددا**")
            return
        await event.edit(f"- {response.message.message}\n @tt_tabot")

@l313l.on(admin_cmd(pattern="شعبان ?(.*)"))
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

@l313l.on(admin_cmd(pattern="رمضان ?(.*)"))
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

@l313l.on(admin_cmd(pattern="محرم ?(.*)"))
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
            


@l313l.on(admin_cmd(pattern="الاغنية ?(.*)"))
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await event.edit("**▾∮ يجب الرد على الاغنيه اولا**")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                await event.edit("**▾∮ يتم التعرف على الاغنية انتظر**")
                start_msg = await conv.send_message("/start")
                response = await conv.get_response()
                send_audio = await conv.send_message(reply_message)
                check = await conv.get_response()
                if not check.text.startswith("Audio received"):
                    return await event.edit(
                        "**▾∮ يجب ان يكون حجم الاغنيه من 5 الى 10 ثواني **."
                    )
                await event.edit("- انتظر قليلا")
                result = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("```Mohon buka blokir (@auddbot) dan coba lagi```")
                return
            namem = f"**الأغنية : **{result.text.splitlines()[0]}\n\n**التفاصيـل : **{result.text.splitlines()[2]}"
            await event.edit(namem)
            await event.client.delete_messages(
                conv.chat_id,
                [start_msg.id, send_audio.id, check.id, result.id, response.id],
            )
    except TimeoutError:
        return await event.edit("***حدث خطا ما حاول مجددا**")


@l313l.on(admin_cmd(pattern="ايميل وهمي(?: |$)(.*)"))
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
            l313lmail = response.reply_markup.rows[2].buttons[0].url
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await geez.edit("**الغي حظر @TempMailBot  و حاول مجددا**")
            return
        await event.edit(
            f"الايميل الخاص هو `{response.message.message}`\n[ اضغط هنا لرؤية من رسائل الايميل الواردة]({l313lmail})"
        )


@l313l.on(admin_cmd(outgoing=True, pattern="افتار$"))
async def jepThe(theme):
    rl = random.randint(4, 57)
    url = f"https://t.me/iamMUAOL/{rl}"
    await theme.client.send_file(theme.chat_id, url, caption="᯽︙  اذكر القائم")
    await theme.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="لطمية$"))
async def jepThe(theme):
    rl = random.randint(19, 170)
    url = f"https://t.me/x04ou/{rl}"
    await theme.client.send_file(theme.chat_id, url, caption="᯽︙  اذكر القائم ", parse_mode="html")
    await theme.delete()

  
@l313l.ar_cmd(pattern="لتغلط$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/4"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="ببجي$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1134"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="نشاقة$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/3"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="احب الله$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/2"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="هع$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1165"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="شنهي$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1115"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="تف$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1161"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="شش$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/79"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="ماذا$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/81"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="هه$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/338"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="نية$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1157"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="مرهم$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/537"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="سبحان$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/541"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="طط$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/طط"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="لاا$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/571"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="زيج$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/VIPABH/1171"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="زيج2$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/20"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="(عبود|شيلة عبود)")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/VIPABH/1162"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="وخر$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/589"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="هههه$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/44"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="انجب$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/592"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="امريكا$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1113"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="شسوي$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1114"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="ها$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1115"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="لتغلطط$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/4"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="مي$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1116"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="انعل$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/597"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="فلا")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1160"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="طاح$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/612"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="شماته$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/37"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="ماكدر$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/38"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="لب$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/614"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="خوش$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/57"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="صل$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/735"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="ط$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/736"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="يولن$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/292"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="ههه$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1164"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="كعبة")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1155"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="شبيك$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1163"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="دكي$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/987"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="نعال$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1156"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="دنجب$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/988"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="روح$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/71"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="مزنجر$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/997"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="الهي$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/23"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="ملحد$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/55"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="يدكتور$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1107"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="بط")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/VIPABH/1168"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="اي$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1098"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="الماوارثها$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1093"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="يامرحبا$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/60"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="نيو$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/5"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="نوكيا$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1111"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="ايرور$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/7"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="بوربه$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1159"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="طبك$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/65"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="سييي$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/66"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="سبيدر مان")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/67"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="خاف حرام$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/68"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="تحيه لاختك$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/69"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="نيه$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/71"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="امشي كحبة$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/72"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="امداك$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/73"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="الحس$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/74"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="افتهمنا$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/75"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="اطلع$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/77"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="اوني تشان")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/78"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="اخت التنيج$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/79"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="اوني تشان2$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/97"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="كعدت الديوث$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/98"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="خبز يابس$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/100"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="خيار بصل$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/101"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.ar_cmd(pattern="ماي ارو$")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/102"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern=r"ميمز (\S+) (.+)"))
async def Hussein(event):
    url = event.pattern_match.group(1)
    lMl10l = event.pattern_match.group(2)
    add_link(lMl10l, url)
    await event.edit(f"**᯽︙ تم اضافة البصمة {lMl10l} بنجاح ✓ **")
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass

@l313l.on(admin_cmd(outgoing=True, pattern="?(.*)"))
async def Hussein(event):
    lMl10l = event.pattern_match.group(1)
    Joker = await reply_id(event)
    url = get_link(lMl10l)
    if url:
        await event.client.send_file(event.chat_id, url, parse_mode="html", reply_to=Joker)
        await event.delete()
        joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
        joker = Get(joker)
        try:
            await event.client(joker)
        except BaseException:
            pass

@l313l.ar_cmd(pattern="ازالة(?:\s|$)([\s\S]*)")
async def delete_aljoker(event):
    lMl10l = event.pattern_match.group(1)
    delete_link(lMl10l)
    await event.edit(f"**᯽︙ تم حذف البصمة '{lMl10l}' بنجاح ✓**")
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass

@l313l.on(admin_cmd(outgoing=True, pattern="قائمة الميمز"))
async def list_aljoker(event):
    links = SESSION.query(AljokerLink).all()
    if links:
        message = "**᯽︙ قائمة تخزين اوامر الميمز:**\n"
        for link in links:
            message += f"- البصمة : .`{link.key}`\n"
    else:
        message = "**᯽︙ لاتوجد بصمات ميمز مخزونة حتى الآن**"
    await event.edit(message)
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass
@l313l.on(admin_cmd(outgoing=True, pattern="ازالة_البصمات"))
async def delete_all_aljoker(event):
    SESSION.query(AljokerLink).delete()
    await event.edit("**᯽︙ تم حذف جميع بصمات الميمز من القائمة **")
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass
    try:
        await event.client(joker)
    except BaseException:
        pass

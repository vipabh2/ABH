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
#ياقائم آل محمد
from VIPABH import ABH
from ..helpers.utils import reply_id
plugin_category = "tools"
    
@ABH.on(admin_cmd(pattern="حالتي ?(.*)"))
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


@ABH.on(admin_cmd(pattern="الاغنية ?(.*)"))
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
            namem = f"**الأغنية : **{result.text.splitlines()[0]}\
        \n\n**التفاصيـل : **{result.text.splitlines()[2]}"
            await event.edit(namem)
            await event.client.delete_messages(
                conv.chat_id,
                [start_msg.id, send_audio.id, check.id, result.id, response.id],
            )
    except TimeoutError:
        return await event.edit("***حدث خطا ما حاول مجددا**")


@ABH.on(admin_cmd(pattern="ايميل وهمي(?: |$)(.*)"))
async def _(event):
    chat = "@TempMailBot"
    geez = await event.edit("**جاري انشاء بريد ...**")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=220112646)
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            ABHmail = (response).reply_markup.rows[2].buttons[0].url
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await geez.edit("**الغي حظر @TempMailBot  و حاول مجددا**")
            return
        await event.edit(
            f"الايميل الخاص هو `{response.message.message}`\n[ اضغط هنا لرؤية من رسائل الايميل الواردة]({ABHmail})"
        )
@ABH.on(admin_cmd(outgoing=True, pattern="غنيلي$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/DwDi1/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="᯽︙ BY : @jepthon 🎀",parse_mode="html")
  await joker313.delete()
    
@ABH.on(admin_cmd(outgoing=True, pattern="شعر$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/L1BBBL/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="᯽︙ BY : @jepthon 🎀",parse_mode="html")
  await vois.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="قران$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/QuraanJep/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="᯽︙ BY : @jepthon 🤲🏻☪️",parse_mode="html")
  await vois.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="ثيم$"))
async def jepThe(theme):
  rl = random.randint(2,510)
  url = f"https://t.me/GSSSD/{rl}"
  await theme.client.send_file(theme.chat_id,url,caption="᯽︙ THEME BY : @jepthon 🎊",parse_mode="html")
  await theme.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="لاتغلط$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/4"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="بجيت$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/5"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="نشاقة$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/3"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="احب الله$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/2"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="روح$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/6"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="انمي1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/7"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="انمي2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/9"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="انمي3$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/11"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="انمي4$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/12"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="انمي5$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/13"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="انمي6$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/14"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="انمي7$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/15"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="انمي8$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/16"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="انمي9$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/17"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="انمي10$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/18"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="زيج2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/19"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="زيج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/20"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="(شيله عبود|شيلة عبود)"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/21"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="تخوني$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/26"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="احب العراق$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/27"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="مستمرة الكلاوات$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/28"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="احبك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/29"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="اخت التنيج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/30"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="اذا اكمشك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/31"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="اسكت$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/32"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="افتهمنا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/33"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="اكل خرا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/34"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="الكعده وياكم"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/35"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="الكمر اني$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/36"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="اللهم لا شماته$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/37"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="اني مااكدر$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/38"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="بقولك ايه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/39"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="تف على شرفك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/40"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="شجلبت$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/41"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="شكد شفت ناس$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/42"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="صباح القنادر$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/43"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="ضحكة فيطية$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/44"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="طاهر القلب"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/45"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="غطيلي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/46"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="في منتصف الجبهة$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/49"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="لاتقتل المتعه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/50"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="لا لتغلط$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/51"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="لا يمه لا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/52"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="لحد يحجي وياي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/53"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="ماادري يعني$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/54"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="منو انت$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/55"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="مو صوجكم$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/56"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="خوش تسولف"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/57"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="يع$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/58"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="يعني مااعرف$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/59"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="يامرحبا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/60"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="منو انتة$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/61"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="ماتستحي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/62"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="عيب$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/63"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="عنعانم$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/64"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="طبك مرض$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/65"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="سييي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/66"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="سبيدر مان"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/67"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="خاف حرام$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/68"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="تحيه لاختك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/69"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="روح$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/71"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="امشي كحبة$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/72"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="امداك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/73"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="الحس$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/74"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="افتهمنا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/75"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="اطلع برا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/77"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="اوني تشان"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/78"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="اخت التنيج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/79"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="اوني تشان2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/97"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="كعدت الديوث$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/98"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="خبز يابس$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/100"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="خيار بصل$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/101"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(admin_cmd(outgoing=True, pattern="ماي ارو$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/102"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@ABH.on(admin_cmd(outgoing=True, pattern=r"ميمز (\S+) (.+)"))
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

@ABH.on(admin_cmd(outgoing=True, pattern="?(.*)"))
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

@ABH.ar_cmd(pattern="ازالة(?:\s|$)([\s\S]*)")
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

@ABH.on(admin_cmd(outgoing=True, pattern="قائمة الميمز"))
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
@ABH.on(admin_cmd(outgoing=True, pattern="ازالة_البصمات"))
async def delete_all_aljoker(event):
    SESSION.query(AljokerLink).delete()
    await event.edit("**᯽︙ تم حذف جميع بصمات الميمز من القائمة **")
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass

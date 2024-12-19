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
# @ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*لطمية$'))
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
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*لتغلط$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/4"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*ببجي$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1134"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*نشاقة$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/3"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*احب الله$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/2"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*هع$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1165"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*شنهي$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1115"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*تف$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1161"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*شش$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/79"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*ماذا$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/81"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*هه$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/338"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*نية$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1157"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*مرهم$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/537"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*سبحان$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/541"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*طط$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/طط"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*لاا$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/571"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*زيج$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/VIPABH/1171"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*زيج2$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/20"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*(عبود|شيلة عبود)")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/VIPABH/1162"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*وخر$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/589"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*هههه$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/44"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*انجب$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/592"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*امريكا$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1113"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*شسوي$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1114"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*ها$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1115"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*لتغلطط$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/4"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*مي$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1116"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*انعل$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/597"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*فلا")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1160"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*طاح$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/612"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*شماته$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/37"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*ماكدر$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/38"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*لب$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/614"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*خوش$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/57"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*صل$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/735"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*ط$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/736"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*يولن$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/292"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*ههه$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1164"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*كعبة")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1155"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*شبيك$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1163"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*دكي$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/987"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*نعال$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1156"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*دنجب$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/988"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*روح$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/71"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*مزنجر$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/997"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*الهي$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/23"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*ملحد$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/55"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*يدكتور$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1107"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*بط")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/VIPABH/1168"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*اي$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1098"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*الماوارثها$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1093"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*يامرحبا$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/60"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*نيو$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/5"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*نوكيا$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1111"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*ايرور$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/7"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*بوربه$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/1159"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*طبك$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/memesoundjep/65"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*سييي$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/66"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*سبيدر مان")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/67"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*خاف حرام$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/68"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*تحيه لاختك$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/69"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*نيه$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/71"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*امشي كحبة$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/72"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*امداك$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/73"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*الحس$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/74"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*افتهمنا$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/75"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*اطلع$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/77"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*اوني تشان")
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/78"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*اخت التنيج$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/79"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*اوني تشان2$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/97"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*كعدت الديوث$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/98"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*خبز يابس$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/100"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*خيار بصل$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/101"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ABH.on(events.NewMessage(outgoing=True, pattern=r'^\.*ماي ارو$'))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/vipabh/102"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

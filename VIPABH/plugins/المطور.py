import random
import re
import time
from platform import python_version

from telethon import version, Button, events
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from JoKeRUB import StartTime, l313l, JEPVERSION

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import mention

plugin_category = "utils"

@l313l.ar_cmd(
    pattern="ابن هاشم$",
    command=("ابن هاشم", plugin_category),
    info={
        "header": "لأظهار مطورين السورس",
        "usage": [
            "{tr}ابن هاشم",
        ],
    },
)
async def amireallyalive(event):
    await event.delete()
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  - "
    CUSTOM_ALIVE_TEXT = gvarstatus("ALIVE_TEXT")
    CAT_IMG = "https://forkgraph.zaid.pro/file/2ReShkSyFhju"
    if CAT_IMG:
        CAT = [x for x in CAT_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        cat_caption = f"ابن هاشم الراقي \n"        
        cat_caption = f"ملجائي👇 \n"
        cat_caption += f"✛━ EHIEX.t.me ━✛\n"
        cat_caption += f"✛━ x04ou.t.me ━✛\n"
        cat_caption += f"✛━ sszxl.t.me ━✛\n"
        await event.client.send_file(
            event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id
        )
progs = [1910015590]

@l313l.on(events.NewMessage(incoming=True))
async def reda(event):
    if event.reply_to and event.sender_id in progs:
       reply_msg = await event.get_reply_message()
       owner_id = reply_msg.from_id.user_id
       if owner_id == l313l.uid:
           if event.message.message == "حظر من السورس":
               await event.reply("**حاظر مطوري ، لقد تم حظره من استخدام السورس**")
               addgvar("blockedfrom", "yes")
           elif event.message.message == "الغاء الحظر من السورس":
               await event.reply("**حاظر مطوري، لقد الغيت الحظر**")
               delgvar("blockedfrom")
              

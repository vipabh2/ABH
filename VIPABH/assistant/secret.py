import json
import os
import re

from telethon.events import CallbackQuery

from VIPABH import ABH


@ABH.tgbot.on(CallbackQuery(data=re.compile(b"rzan_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    if os.path.exists("./VIPABH/secrets.txt"):
        jsondata = json.load(open("./VIPABH/secrets.txt"))
        try:
            message = jsondata[f"{timestamp}"]
            userid = message["userid"]
            ids = [userid, ABH.uid]
            if event.query.user_id in ids:
                encrypted_tcxt = message["text"]
                reply_pop_up_alert = encrypted_tcxt
            else:
                reply_pop_up_alert = "⌯︙عـذرا هذه الهـمسة ليست مخصصة لـك"
        except KeyError:
            reply_pop_up_alert = "⌯︙عـذرا هذه الهمسة لم تعد موجوده في سيـرفرات جـيبثون"
    else:
        reply_pop_up_alert = "⌯︙عـذرا هذه الهمسة لم تعد موجوده  "
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

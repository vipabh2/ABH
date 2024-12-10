import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from VIPABH.utils import admin_cmd

@borg.on(admin_cmd(pattern="تحويل نص ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
        await event.edit("᯽︙ يـجب الرد علـى رسالة لتحويلها.")
        return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
        await event.edit("᯽︙ يـجب الرد علـى رسالة نصية.")
        return
    chat = "@QuotLyBot"
    if reply_message.sender.bot:
        await event.edit("᯽︙ يـجب الرد علـى رسالة مستخدم.")
        return
    await event.edit("᯽︙ جار تحويل النص إلى ملصق...")
    async with event.client.conversation(chat) as conv:
        try:     
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=1031952739))
            await event.client.forward_messages(chat, reply_message)
            response = await response 
        except YouBlockedUserError: 
            await event.reply("᯽︙ يرجى إلغاء الحظر عن البوت (@QuotLyBot).")
            return
        if response.text.startswith("Hi!"):
            await event.edit("᯽︙ يرجى إلغاء خصوصية التوجيه أولا.")
        else: 
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


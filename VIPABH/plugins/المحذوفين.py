from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from ..core.managers import edit_delete, edit_or_reply

@ABH.ar_cmd(pattern=r"المحذوفين ?([\s\S]*)")
async def rm_deletedacc(show):
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "**⎉╎لا توجـد حـسابات محذوفـة في هـذه المجموعـة !**"
    if con != "تنظيف":
        event = await edit_or_reply(show, "**⎉╎جـارِ البحـث عـن الحسابـات المحذوفـة ⌯**")
        async for user in show.ABH.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(0.5)
        if del_u > 0:
            del_status = f"**⎉╎تم ايجـاد  {del_u}  من  الحسابـات المحذوفـه في هـذه المجموعـه**\n**⎉╎لحذفهـم إستخـدم الأمـر  ⩥ :**  `.المحذوفين تنظيف`"
        await event.edit(del_status)
        return
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_delete(show, "**⎉╎ليس لـدي صلاحيـات المشـرف هنـا ؟!**", 5)
        return
    event = await edit_or_reply(show, "**⎉╎جـارِ حـذف الحسـابات المحذوفـة ⌯**")
    del_u = 0
    del_a = 0
    async for user in show.ABH.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.ABH.kick_participant(show.chat_id, user.id)
                await sleep(0.5)
                del_u += 1
            except ChatAdminRequiredError:
                await edit_delete(event, "**⎉╎ ليس لدي صلاحيات الحظر هنا**", 5)
                return
            except UserAdminInvalidError:
                del_a += 1
    if del_u > 0:
        del_status = f"**⎉╎تـم حـذف  {del_u}  الحسـابات المحذوفـة ✓**"
    if del_a > 0:
        del_status = f"**⎉╎تـم حـذف {del_u} الحسـابات المحذوفـة، ولڪـن لـم يتـم حذف الحسـابات المحذوفـة للمشرفيـن !**"
    await edit_delete(event, del_status, 5)
    if BOTLOG:
        await show.ABH.send_message(
            BOTLOG_CHATID,
            f"**⎉╎تنظيف :**\
            \n⎉╎{del_status}\
            \n*⎉╎المحادثـة ⌂** {show.chat.title}(`{show.chat_id}`)",
        )

  
@ABH.ar_cmd(pattern="رسائلي$")
async def zed(event):
    zzm = "me"
    a = await bot.get_messages(event.chat_id, 0, from_user=zzm)
    await edit_or_reply(event, f"**⎉╎لديـك هنـا ⇽**  `{a.total}`  **رسـالـه 📩**")


@ABH.ar_cmd(pattern="رسائله ?(.*)")
async def zed(event):
    k = await event.get_reply_message()
    if k:
        a = await bot.get_messages(event.chat_id, 0, from_user=k.sender_id)
        return await edit_or_reply(event, f"**⎉╎لديـه هنـا ⇽**  `{a.total}`  **رسـالـه 📩**")
    zzm = event.pattern_match.group(1)
    if zzm:
        a = await bot.get_messages(event.chat_id, 0, from_user=zzm)
        return await edit_or_reply(event, f"**⎉╎المستخـدم** {zzm} **لديـه هنـا ⇽**  `{a.total}`  **رسـالـه 📩**")
    else:
        await edit_or_reply(event, f"**⎉╎بالـرد ع الشخص او بـ إضافة أيـدي او يـوزر الشخـص لـ الامـر**")


@ABH.ar_cmd(pattern="(الرسائل|رسائل) ?(.*)")
async def zed(event):
    k = await event.get_reply_message()
    if k:
        a = await bot.get_messages(event.chat_id, 0, from_user=k.sender_id)
        return await edit_or_reply(event, f"**⎉╎لديـه هنـا ⇽**  `{a.total}`  **رسـالـه 📩**")
    zzm = event.pattern_match.group(1)
    if zzm:
        a = await bot.get_messages(event.chat_id, 0, from_user=zzm)
        return await edit_or_reply(event, f"**⎉╎المستخـدم** {zzm} **لديـه هنـا ⇽**  `{a.total}`  **رسـالـه 📩**")
    else:
        await edit_or_reply(event, f"**⎉╎بالـرد ع الشخص او بـ إضافة أيـدي او يـوزر الشخـص لـ الامـر**")

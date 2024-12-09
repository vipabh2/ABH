import asyncio
import time
from telethon import functions, types, events
from telethon.tl.types import UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusRecently, ChatBannedRights
from telethon.errors import ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, BadRequestError, ChatAdminRequiredError, FloodWaitError, MessageNotModifiedError, UserAdminInvalidError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc, DiscardGroupCallRequest as stopvc, GetGroupCallRequest as getvc, InviteToGroupCallRequest as invitetovc
from telethon.utils import get_display_name
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format


@l313l.ar_cmd(
    pattern="اكسباير ?([\s\S]*)",
    command=("اكسباير", plugin_category),
    info={
        "header": "To get breif summary of members in the group",
        "description": "To get breif summary of members in the group . Need to add some features in future.",
        "usage": [
            "{tr}اكسباير",
        ],
    },
    groups_only=True,
)
async def _(event):  # sourcery no-metrics
    "To get breif summary of members in the group.1 11"
    input_str = event.pattern_match.group(1)
    if input_str:
        chat = await event.get_chat()
        if not chat.admin_rights and not chat.creator:
            await edit_or_reply(event, "**⎉╎عـذراً عـزيـزي .. انت لسـت مشرفـاً هنـا 🙇🏻**")
            return False
    p = 0
    b = 0
    c = 0
    d = 0
    e = []
    m = 0
    n = 0
    y = 0
    w = 0
    o = 0
    q = 0
    r = 0
    et = await edit_or_reply(event, "**⪼ البحث في قـوائم المشارڪين ..**")
    async for i in event.client.iter_participants(event.chat_id):
        p += 1
        #
        # Note that it's "reversed". You must set to ``True`` the permissions
        # you want to REMOVE, and leave as ``None`` those you want to KEEP.
        rights = ChatBannedRights(until_date=None, view_messages=True)
        if isinstance(i.status, UserStatusEmpty):
            y += 1
            if "y" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("أحتاج امتيازات المشرف لأداء هذا الإجراء")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusLastMonth):
            m += 1
            if "m" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("أحتاج امتيازات المشرف لأداء هذا الإجراء")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusLastWeek):
            w += 1
            if "w" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("أحتاج امتيازات المشرف لأداء هذا الإجراء")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusOffline):
            o += 1
            if "o" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("أحتاج امتيازات المشرف لأداء هذا الإجراء")
                    e.append(str(e))
                    break
                else:
                    c += 1
        if isinstance(i.status, UserStatusOnline):
            q += 1
            if "q" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("أحتاج امتيازات المشرف لأداء هذا الإجراء")
                    e.append(str(e))
                    break
                else:
                    c += 1
        if isinstance(i.status, UserStatusRecently):
            r += 1
            if "r" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("أحتاج امتيازات المشرف لأداء هذا الإجراء")
                    e.append(str(e))
                    break
        if i.bot:
            b += 1
            if "b" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("أحتاج امتيازات المشرف لأداء هذا الإجراء")
                    e.append(str(e))
                    break
                else:
                    c += 1
        elif i.deleted:
            d += 1
            if "d" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("أحتاج امتيازات المشرف لأداء هذا الإجراء")
                    e.append(str(e))
        elif i.status is None:
            n += 1
    if input_str:
        required_string = """𓆰 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 **- 🝢 - معـلومـات المجمـوعــه** 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻 
⪼ المطرودين {} / {} المستخدمين
⪼ **الحسابات المحذوفه ↫** {}
⪼ **اخر ظهور منذ زمن طويل ↫** {}
⪼ **اخر ظهور منذ شهر ↫** {}
⪼ **اخر ظهور منذ اسبوع ↫** {}
⪼ **غير متصل ↫** {}
⪼ **متصل ↫** {}
⪼ **اخر ظهور قبل قليل ↫** {}
⪼ **البوتات ↫** {}
⪼ **غيـر معلـوم ↫** {}

𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"""
        await et.edit(required_string.format(c, p, d, y, m, w, o, q, r, b, n))
        await sleep(5)
    await et.edit(
        """𓆰 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 **- 🝢 - معـلومـات المجمـوعــه** 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻
⪼ **العدد ↫ {} **مستخدماً
⪼ **الحسابات المحذوفه ↫** {}
⪼ **اخر ظهور منذ زمن طويل ↫** {}
⪼ **اخر ظهور منذ شهر ↫** {}
⪼ **اخر ظهور منذ اسبوع ↫** {}
⪼ **غير متصل ↫** {}
⪼ **متصل ↫** {}
⪼ **اخر ظهور قبل قليل ↫** {}
⪼ **البوتات ↫** {}
⪼ **غيـر معلـوم ↫** {}
𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻""".format(
            p, d, y, m, w, o, q, r, b, n
        )
    )


@l313l.ar_cmd(pattern=r"المحذوفين ?([\s\S]*)")
async def rm_deletedacc(show):
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "**⎉╎لا توجـد حـسابات محذوفـة في هـذه المجموعـة !**"
    if con != "تنظيف":
        event = await edit_or_reply(show, "**⎉╎جـارِ البحـث عـن الحسابـات المحذوفـة ⌯**")
        async for user in show.client.iter_participants(show.chat_id):
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
    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client.kick_participant(show.chat_id, user.id)
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
        await show.client.send_message(
            BOTLOG_CHATID,
            f"**⎉╎تنظيف :**\
            \n⎉╎{del_status}\
            \n*⎉╎المحادثـة ⌂** {show.chat.title}(`{show.chat_id}`)",
        )

  
@l313l.ar_cmd(pattern="رسائلي$")
async def zed(event):
    zzm = "me"
    a = await bot.get_messages(event.chat_id, 0, from_user=zzm)
    await edit_or_reply(event, f"**⎉╎لديـك هنـا ⇽**  `{a.total}`  **رسـالـه 📩**")


@l313l.ar_cmd(pattern="رسائله ?(.*)")
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


@l313l.ar_cmd(pattern="(الرسائل|رسائل) ?(.*)")
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

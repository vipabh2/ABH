from telethon.tl.types import MessageReactions
from asyncio import sleep
import asyncio
import requests
import random
from datetime import datetime
import time
from telethon.tl import types
from telethon.tl.types import Channel, Chat, User, ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.errors.rpcerrorlist import ChannelPrivateError
from telethon.tl.custom import Message
from ..Config import Config
from telethon.errors import (
    UserNotParticipantError,
    ChatAdminRequiredError,
    FloodWaitError,
    MessageNotModifiedError,
    UserAdminInvalidError,
    InputUserDeactivatedError,
    UserBlockedError,
    UserBotError,
    UserChannelsTooMuchError,
    UserKickedError,
    UserPrivacyRestrictedError,
    UserNotMutualContactError
)
stop_addCon = False
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.channels import EditBannedRequest, LeaveChannelRequest
from telethon.tl.functions.channels import EditAdminRequest
from telethon import events, functions, errors
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantCreator,
    ChannelParticipantsKicked,
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
    InputPeerChat,
    MessageEntityCustomEmoji,
)
from VIPABH import ABH
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from datetime import datetime
from telethon.tl.functions.channels import GetParticipantRequest
from ..core.logger import logging
from telethon.tl.types import InputUser
from ..helpers.utils import reply_id
from ..sql_helper.locks_sql import *
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import readable_time
from . import BOTLOG, BOTLOG_CHATID
LOGS = logging.getLogger(__name__)
plugin_category = "admin"
spam_chats = []
aljoker_time = None
BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

async def ban_user(chat_id, i, rights):
    try:
        await ABH(functions.channels.EditBannedRequest(chat_id, i, rights))
        return True, None
    except Exception as exc:
        return False, str(exc)        

#Reda
@ABH.ar_cmd(pattern="(اضف جهاتي|اضف جهتي)")
async def reda_add_con(event):
    global stop_addCon
    await event.delete()
    
    Redaresult = await event.client(functions.channels.GetParticipantRequest(
        event.chat_id, (await event.client.get_me()).id
    ))

    if not Redaresult.participant.admin_rights.invite_users:
        return await event.respond(
            "᯽︙ - يبدو انه ليس لديك صلاحيات لإضافة الاعضاء للدردشة"
        )

    count = 0
    try:
        contacts_result = await event.client(functions.contacts.GetContactsRequest(hash=0))
        
        for u in contacts_result.users:
            if stop_addCon:
                break
            try:
                try:
                    await event.client(functions.channels.InviteToChannelRequest(
                        channel=event.chat_id,
                        users=[u]
                    ))
                except errors.FloodWaitError as e:
                    await asyncio.sleep(e.seconds)
                    await event.client(functions.channels.InviteToChannelRequest(
                        channel=event.chat_id,
                        users=[u]
                    ))
                
                count += 1
                await asyncio.sleep(2)
            except (UserChannelsTooMuchError, 
                    UserPrivacyRestrictedError, 
                    InputUserDeactivatedError, 
                    UserBlockedError, 
                    UserKickedError,
                    UserNotParticipantError,
                    UserNotMutualContactError,
                    ChatMemberAddFailedError) as e:
                
                continue
            except Exception:
                continue

    except errors.FloodWaitError as e:
        await asyncio.sleep(e.seconds)
    except Exception:
        pass
    await event.client.send_message(event.chat_id, f"تم اضافة {count} للكروب.")

@ABH.ar_cmd(pattern="(ايقاف الاضافة|ايقاف|ايقاف الاضافه)")
async def stop_add_con(event):
    global stop_addCon
    stop_addCon = True


@ABH.ar_cmd(pattern="ارسل")
async def remoteaccess(event):

    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:
        chat_id = int(chat_id)
    except BaseException:

        pass

    msg = ""
    mssg = await event.get_reply_message()
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("تم الارسال الرسالة الى الرابط الذي وضعتة")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("تم ارسال الرساله الى الرابط الذي وضعتة")
    except BaseException:
        await event.edit("** عذرا هذا ليست مجموعة **")
@ABH.ar_cmd(
    pattern="اطردني$",
    command=("اطردني", plugin_category),
    info={
        "header": "To kick myself from group.",
        "usage": [
            "{tr}kickme",
        ],
    },
    groups_only=True,
)
async def kickme(leave):
    "to leave the group."
    await leave.edit("᯽︙  حسنا سأغادر المجموعه وداعا ")
    await leave.client.kick_participant(leave.chat_id, "me")

@ABH.ar_cmd(
    pattern="تفليش بالطرد$",
    command=("تفليش بالطرد", plugin_category),
    info={
        "header": "To kick everyone from group.",
        "description": "To Kick all from the group except admins.",
        "usage": [
            "{tr}kickall",
        ],
    },
    require_admin=True,
)
async def _(event):
    "To kick everyone from group."
    await event.delete()
    result = await event.client(
        functions.channels.GetParticipantRequest(event.chat_id, event.client.uid)
    )
    if not result.participant.admin_rights.ban_users:
        return await edit_or_reply(
            event, "᯽︙ - يبدو انه ليس لديك صلاحيات الحذف في هذه الدردشة "
        )
    admins = await event.client.get_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    )
    admins_id = [i.id for i in admins]
    total = 0
    success = 0
    async for user in event.client.iter_participants(event.chat_id):
        total += 1
        try:
            if user.id not in admins_id:
                await event.client.kick_participant(event.chat_id, user.id)
                success += 1
                await sleep(0.5)
        except Exception as e:
            LOGS.info(str(e))
            await sleep(0.5)
    await event.reply(
        f"᯽︙  تم بنجاح طرد من {total} الاعضاء ✅ "
    )

@ABH.ar_cmd(
    pattern="تفليش$",
    command=("تفليش", plugin_category),
    info={
        "header": "To ban everyone from group.",
        "description": "To ban all from the group except admins.",
        "usage": [
            "{tr}kickall",
        ],
    },
    require_admin=True,
)
async def _(event):
    "To ban everyone from group."
    await event.delete()
    result = await event.client(
        functions.channels.GetParticipantRequest(event.chat_id, event.client.uid)
    )
    if not result:
        return await edit_or_reply(
            event, "᯽︙ - يبدو انه ليس لديك صلاحيات الحذف في هذه الدردشة ❕"
        )
    admins = await event.client.get_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    )
    admins_id = [i.id for i in admins]
    total = 0
    success = 0
    async for user in event.client.iter_participants(event.chat_id):
        total += 1
        try:
            if user.id not in admins_id:
                await event.client(
                    EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS)
                )
                success += 1
                await sleep(0.5) # for avoid any flood waits !!-> do not remove it 
        except Exception as e:
            LOGS.info(str(e))
    await event.reply(
        f"᯽︙  تم بنجاح حظر من {total} الاعضاء ✅ "
    )



plugin_category = "admin"
@ABH.ar_cmd(
    pattern="المحذوفين ?([\s\S]*)",
    command=("المحذوفين", plugin_category),
    info={
        "header": "لتحقق من الحسابات المحذوفة وتنظيفها",
        "description": "يبحث عن حسابات محذوفة في مجموعة. استخدم `.المحذوفين اطردهم` لإزالة الحسابات المحذوفة من المجموعة.",
        "usage": ["{tr}المحذوفين", "{tr}المحذوفين اطردهم"],
    },
    groups_only=True,
)
async def rm_deletedacc(show):
    "للتحقق من الحسابات المحذوفة وتنظيفها"
    command = show.pattern_match.group(1).lower()
    deleted_users_count = 0
    no_deleted_msg = "᯽︙ لم يتم العثور على حسابات متروكة أو محذوفة، المجموعة نظيفة."
    
    if command != "اطردهم":
        event = await edit_or_reply(show, "᯽︙ يتم البحث عن حسابات محذوفة، انتظر...")
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                deleted_users_count += 1
                await asyncio.sleep(0.5)
                
        if deleted_users_count > 0:
            response_msg = f"᯽︙ تم العثور على **{deleted_users_count}** حسابات محذوفة في هذه الدردشة،\
                            \nيمكنك طردهم بواسطة `.المحذوفين اطردهم`."
        else:
            response_msg = no_deleted_msg
        
        await event.edit(response_msg)
        return

    chat = await show.get_chat()
    is_admin = chat.admin_rights or chat.creator
    
    if not is_admin:
        await edit_or_reply(show, "᯽︙ ليس لدي صلاحيات كافية هنا.", 5)
        return
    
    event = await edit_or_reply(show, "᯽︙ جاري حذف الحسابات المحذوفة...")
    deleted_users_count = 0
    admin_deleted_count = 0
    
    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client.kick_participant(show.chat_id, user.id)
                await asyncio.sleep(0.5)
                deleted_users_count += 1
            except ChatAdminRequiredError:
                await edit_or_reply(event, "᯽︙ ليس لدي صلاحيات الحظر هنا.", 5)
                return
            except UserAdminInvalidError:
                admin_deleted_count += 1
    
    response_msg = f"التنظيف: **{deleted_users_count}** حسابات محذوفة تم حذفها."
    if admin_deleted_count > 0:
        response_msg += f"\n**{admin_deleted_count}** حسابات لم أستطع حذفها لأنها مشرفين."
    
    await edit_or_reply(event, response_msg, 5)
    
    if BOTLOG:
        await show.client.send_message(
            BOTLOG_CHATID,
            f"#تنظيف المحذوفات\
            \n{response_msg}\
            \nالدردشة: {show.chat.title}(`{show.chat_id}`)",
        )



@ABH.ar_cmd(pattern="حظر_الكل(?:\s|$)([\s\S]*)")
async def banall(event):
     chat_id = event.chat_id
     if event.is_private:
         return await edit_or_reply(event, "** ᯽︙ هذا الامر يستعمل للقنوات والمجموعات فقط !**")
     msg = "حظر"
     is_admin = False
     try:
         partici_ = await ABH(GetParticipantRequest(
           event.chat_id,
           event.sender_id
         ))
     except UserNotParticipantError:
         is_admin = False
     spam_chats.append(chat_id)
     usrnum = 0
     async for usr in ABH.iter_participants(chat_id):
         if not chat_id in spam_chats:
             break
         userb = usr.username
         usrtxt = f"{msg} @{userb}"
         if str(userb) == "None":
             userb = usr.id
             usrtxt = f"{msg} {userb}"
         await ABH.send_message(chat_id, usrtxt)
         await asyncio.sleep(1)
         await event.delete()
     try:
         spam_chats.remove(chat_id)
     except:
         pass
@ABH.ar_cmd(pattern="كتم_الكل(?:\s|$)([\s\S]*)")
async def muteall(event):
     if event.is_private:
         return await edit_or_reply(event, "** ᯽︙ هذا الامر يستعمل للقنوات والمجموعات فقط !**")
     msg = "كتم"
     is_admin = False
     try:
         partici_ = await ABH(GetParticipantRequest(
           event.chat_id,
           event.sender_id
         ))
     except UserNotParticipantError:
         is_admin = False
     spam_chats.append(chat_id)
     usrnum = 0
     async for usr in ABH.iter_participants(chat_id):
         if not chat_id in spam_chats:
             break
         userb = usr.username
         usrtxt = f"{msg} @{userb}"
         if str(userb) == "None":
             userb = usr.id
             usrtxt = f"{msg} {userb}"
         await ABH.send_message(chat_id, usrtxt)
         await asyncio.sleep(1)
         await event.delete()
     try:
         spam_chats.remove(chat_id)
     except:
         pass
@ABH.ar_cmd(pattern="طرد_الكل(?:\s|$)([\s\S]*)")
async def kickall(event):
     chat_id = event.chat_id
     if event.is_private:
         return await edit_or_reply(event, "** ᯽︙ هذا الامر يستعمل للقنوات والمجموعات فقط !**")
     msg = "طرد"
     is_admin = False
     try:
         partici_ = await ABH(GetParticipantRequest(
           event.chat_id,
           event.sender_id
         ))
     except UserNotParticipantError:
         is_admin = False
     spam_chats.append(chat_id)
     usrnum = 0
     async for usr in ABH.iter_participants(chat_id):
         if not chat_id in spam_chats:
             break
         userb = usr.username
         usrtxt = f"{msg} @{userb}"
         if str(userb) == "None":
             userb = usr.id
             usrtxt = f"{msg} {userb}"
         await ABH.send_message(chat_id, usrtxt)
         await asyncio.sleep(1)
         await event.delete()
     try:
         spam_chats.remove(chat_id)
     except:
         pass
@ABH.ar_cmd(pattern="الغاء التفليش")
async def ca_sp(event):
  if not event.chat_id in spam_chats:
    return await edit_or_reply(event, "** ᯽︙ 🤷🏻 لا يوجد طرد او حظر او كتم لأيقافه**")
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await edit_or_reply(event, "** ᯽︙ تم الغاء العملية بنجاح ✓**")

@ABH.ar_cmd(pattern="تصفية الخاص")
async def hussein(event):
    await event.edit("**᯽︙ جارِ حذف جميع الرسائل الخاصة الموجودة في حسابك ...**")
    dialogs = await event.client.get_dialogs()
    for dialog in dialogs:
        if dialog.is_user:
            try:
                await event.client(DeleteHistoryRequest(dialog.id, max_id=0, just_clear=True))
            except Exception as e:
                print(f"حدث خطأ أثناء حذف المحادثة الخاصة: {e}")
    await event.edit("**᯽︙ تم تصفية جميع محادثاتك الخاصة بنجاح ✓ **")

@ABH.ar_cmd(pattern="تصفية البوتات")
async def Hussein(event):
    await event.edit("**᯽︙ جارٍ حذف جميع محادثات البوتات في الحساب ...**")
    result = await event.client(GetContactsRequest(0))
    bots = [user for user in result.users if user.bot]
    for bot in bots:
        try:
            await event.client(DeleteHistoryRequest(bot.id, max_id=0, just_clear=True))
        except Exception as e:
            print(f"حدث خطأ أثناء حذف محادثات البوت: {e}")
    await event.edit("**᯽︙ تم حذف جميع محادثات البوتات بنجاح ✓ **")

# الكود من كتابة فريق الجوكر بس تسرقة تنشر بقناة الفضايح انتَ وقناتك 🖤
@ABH.ar_cmd(pattern=r"ذكاء(.*)")
async def hussein(event):
    await event.edit("**᯽︙ جارِ الجواب على سؤالك انتظر قليلاً ...**")
    text = event.pattern_match.group(1).strip()
    if text:
        url = f'http://api.itdevo.uz/ChatGPT/api/index.php?text={text}'
        response = requests.get(url).text
        await event.edit(response)
    else:
        await event.edit("يُرجى كتابة رسالة مع الأمر للحصول على إجابة.")
is_Reham = False
No_group_Joker = "@jepthonsupport"
active_aljoker = []

@ABH.ar_cmd(pattern=r"الذكاء تفعيل")
async def enable_bot(event):
    global is_Reham
    if not is_Reham:
        is_Reham = True
        active_aljoker.append(event.chat_id)
        await event.edit("**᯽︙ تم تفعيل امر الذكاء الاصطناعي سيتم الرد على اسئلة الجميع عند الرد علي.**")
    else:
        await event.edit("**᯽︙ الزر مُفعّل بالفعل.**")
@ABH.ar_cmd(pattern=r"الذكاء تعطيل")
async def disable_bot(event):
    global is_Reham
    if is_Reham:
        is_Reham = False
        active_aljoker.remove(event.chat_id)
        await event.edit("**᯽︙ تم تعطيل امر الذكاء الاصطناعي.**")
    else:
        await event.edit("**᯽︙ الزر مُعطّل بالفعل.**")
@ABH.on(events.NewMessage(incoming=True))
async def reply_to_hussein(event):
    if not is_Reham:
        return
    if event.is_private or event.chat_id not in active_aljoker:
        return
    message = event.message
    if message.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        if reply_message.sender_id == event.client.uid:
            text = message.text.strip()
            if event.chat.username == No_group_Joker:
                return
            response = requests.get(f'https://gptzaid.zaidbot.repl.co/1/text={text}').text
            await asyncio.sleep(4)
            await event.reply(response)
Ya_Hussein = False
active_joker = []
@ABH.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if not Ya_Hussein:
        return
    if event.is_private or event.chat_id not in active_joker:
        return
    sender_id = event.sender_id
    if sender_id != 1910015590:
        if isinstance(event.message.entities, list) and any(isinstance(entity, MessageEntityCustomEmoji) for entity in event.message.entities):
            await event.delete()
            sender = await event.get_sender()
            aljoker_entity = await ABH.get_entity(sender.id)
            aljoker_profile = f"[{aljoker_entity.first_name}](tg://user?id={aljoker_entity.id})"
            await event.reply(f"**᯽︙ عذرًا {aljoker_profile}، يُرجى عدم إرسال الرسائل التي تحتوي على إيموجي المُميز**")
@ABH.ar_cmd(pattern="المميز تفعيل")
async def disable_emoji_blocker(event):
    global Ya_Hussein
    Ya_Hussein = True
    active_joker.append(event.chat_id)
    await event.edit("**᯽︙ ✓ تم تفعيل امر منع الايموجي المُميز بنجاح**")
@ABH.ar_cmd(pattern="المميز تعطيل")
async def disable_emoji_blocker(event):
    global Ya_Hussein
    Ya_Hussein = False
    active_joker.remove(event.chat_id)
    await event.edit("**᯽︙ تم تعطيل امر منع الايموجي المُميز بنجاح ✓ **")
remove_admins_aljoker = {}
@ABH.on(events.ChatAction)
async def Hussein(event):
    if gvarstatus("Mn3_Kick"):
        if event.user_kicked:
            user_id = event.action_message.from_id
            chat = await event.get_chat()
            if chat and user_id:
                now = datetime.now()
                if user_id in remove_admins_aljoker:
                    if (now - remove_admins_aljoker[user_id]).seconds < 60:
                        admin_info = await event.client.get_entity(user_id)
                        joker_link = f"[{admin_info.first_name}](tg://user?id={admin_info.id})"
                        await event.reply(f"**᯽︙ تم تنزيل المشرف {joker_link} بسبب قيامه بعملية تفليش فاشلة 🤣**")
                        await event.client.edit_admin(chat, user_id, change_info=False)
                    remove_admins_aljoker.pop(user_id)
                    remove_admins_aljoker[user_id] = now
                else:
                    remove_admins_aljoker[user_id] = now

@ABH.ar_cmd(pattern="منع_التفليش", require_admin=True)
async def Hussein_aljoker(event):
    addgvar("Mn3_Kick", True)
    await event.edit("**᯽︙ تم تفعيل منع التفليش للمجموعة بنجاح ✓**")

@ABH.ar_cmd(pattern="سماح_التفليش", require_admin=True)
async def Hussein_aljoker(event):
    delgvar("Mn3_Kick")
    await event.edit("**᯽︙ تم تفعيل منع التفليش للمجموعة بنجاح ✓**")
message_counts = {}
enabled_groups = []
Ya_Abbas = False
@ABH.ar_cmd(pattern="النشر تعطيل")
async def enable_code(event):
    global Ya_Abbas
    Ya_Abbas = True
    enabled_groups.append(event.chat_id)
    await event.edit("**᯽︙ ✓ تم تفعيل امر منع النشر التلقائي بنجاح**")
@ABH.ar_cmd(pattern="النشر تفعيل")
async def disable_code(event):
    global Ya_Abbas
    Ya_Abbas = False
    enabled_groups.remove(event.chat_id)
    await event.edit("**᯽︙ تم تعطيل امر منع النشر التلقائي بنجاح ✓ **")

@ABH.on(events.NewMessage)
async def handle_new_message(event):
    if not Ya_Abbas:
        return
    if event.is_private or event.chat_id not in enabled_groups:
        return
    user_id = event.sender_id
    message_text = event.text
    if user_id not in message_counts:
        message_counts[user_id] = {'last_message': None, 'count': 0}
    if message_counts[user_id]['last_message'] == message_text:
        message_counts[user_id]['count'] += 1
    else:
        message_counts[user_id]['last_message'] = message_text
        message_counts[user_id]['count'] = 1
    if message_counts[user_id]['count'] >= 3:
        try:
            await ABH.edit_permissions(event.chat_id, user_id, send_messages=False)
            sender = await event.get_sender()
            aljoker_entity = await ABH.get_entity(sender.id)
            aljoker_profile = f"[{aljoker_entity.first_name}](tg://user?id={aljoker_entity.id})"
            explanation_message = f"**᯽︙ تم تقييد {aljoker_profile} من إرسال الرسائل بسبب تفعيله نشر التلقائي**"
            await event.reply(explanation_message)
            del message_counts[user_id]
        except ChatAdminRequiredError:
            explanation_message = "عذرًا، ليس لدينا الصلاحيات الكافية لتنفيذ هذا الأمر. يرجى من مشرفي المجموعة منحنا صلاحيات مشرف المجموعة."
            await event.reply(explanation_message)
aljoker_Menu = set()
afk_start_time = datetime.now()
@ABH.on(events.NewMessage)
async def handle_messages(event):
    if gvarstatus("5a9_dis"):
        sender_id = event.sender_id
        current_user_id = await ABH.get_me()
        if event.is_private and sender_id != current_user_id.id:
            await event.delete()
            if sender_id not in aljoker_Menu:
                aljoker_time = aljoker_waqt()
                aljoker_message = gvarstatus("aljoker_message") or f" صاحب الحساب غير متواجد !! "
                aljoker_url = gvarstatus("aljoker_url") or "https://forkgraph.zaid.pro/file/Qs0KYYCtvbCI"
                await ABH.send_file(sender_id, aljoker_url, caption=f'**{aljoker_message}**\n**مدة الغياب: {aljoker_time}**')
                aljoker_Menu.add(sender_id)
@ABH.ar_cmd(pattern="الخاص تعطيل")
async def joker5a9(event: Message):
    global afk_start_time
    addgvar("5a9_dis", True)
    afk_start_time = datetime.now()
    await event.edit('**᯽︙ تم قفل الخاص بنجاح الان لا احد يمكنهُ مراسلتك**')
@ABH.ar_cmd(pattern="الخاص تفعيل")
async def joker5a9(event: Message):
    global afk_start_time
    delgvar("5a9_dis")
    afk_start_time = None
    aljoker_Menu.clear()
    await event.edit('**᯽︙ تم تفعيل الخاص بنجاح الان يمكنهم مراسلتك**')
def aljoker_waqt():
    global afk_start_time
    if afk_start_time:
        current_time = datetime.now()
        duration = current_time - afk_start_time
        days, seconds = duration.days, duration.seconds
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        if days > 0:
            return f"{days} يوم {hours} ساعة {minutes} دقيقة {seconds} ثانية"
        elif hours > 0:
            return f"{hours} ساعة {minutes} دقيقة {seconds} ثانية"
        else:
            return f"{minutes} دقيقة {seconds} ثانية" if minutes > 0 else f"{seconds} ثانية"
    return "N/A"
points = {}
is_game_started = False
is_word_sent = False
word = ''
async def get_bot_entity():
    return await ABH.get_entity('me')

@ABH.on(events.NewMessage(outgoing=True, pattern=r'\.اسرع (.*)'))
async def handle_start(event):
    global is_game_started, is_word_sent, word, bot_entity
    is_game_started = True
    is_word_sent = False
    word = event.pattern_match.group(1)
    chat_id = event.chat_id
    await event.edit(f"**اول من يكتب ( {word} ) سيفوز**")

@ABH.on(events.NewMessage(incoming=True))
async def handle_winner(event):
    global is_game_started, is_word_sent, winner_id, word, points
    if is_game_started and not is_word_sent and word.lower() in event.raw_text.lower():
        if event.chat_id:
            bot_entity = await get_bot_entity()
            if bot_entity and event.sender_id != bot_entity.id:
                is_word_sent = True
                winner_id = event.sender_id
                if winner_id not in points:
                    points[winner_id] = 0
                points[winner_id] += 1
                sender = await event.get_sender()
                sender_first_name = sender.first_name if sender else 'مجهول'
                sorted_points = sorted(points.items(), key=lambda x: x[1], reverse=True)
                points_text = '\n'.join([f'{i+1}• {(await ABH.get_entity(participant_id)).first_name}: {participant_points}' for i, (participant_id, participant_points) in enumerate(sorted_points)])
                await ABH.send_message(event.chat_id, f'الف مبرووووك 🎉 الاعب ( {sender_first_name} ) فاز! \n اصبحت نقاطة: {points[winner_id]}\nنقاط المشاركين:\n{points_text}')
joker = [
    "تلعب وخوش تلعب 👏🏻",
    "لك عاش يابطل استمر 💪🏻",
    "على كيفك ركزززز انتَ كدها 🤨",
    "لك وعلي ذيييب 😍",
]

correct_answer = None
game_board = [["👊", "👊", "👊", "👊", "👊", "👊"]]
numbers_board = [["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]]
original_game_board = [["👊", "👊", "👊", "👊", "👊", "👊"]]
joker_player = None
is_game_started2 = False
group_game_status = {}
points = {}

async def handle_clue(event):
    global group_game_status, correct_answer, game_board
    chat_id = event.chat_id
    if chat_id not in group_game_status or not group_game_status[chat_id]:
        group_game_status[chat_id] = {
            'is_game_started2': False,
            'joker_player': None
        }
    if not group_game_status[chat_id]['is_game_started2']:
        group_game_status[chat_id]['is_game_started2'] = True
        group_game_status[chat_id]['joker_player'] = None
        correct_answer = random.randint(1, 6)
        await event.edit(f"**اول من يرسل كلمة (انا) سيشارك في لعبة المحيبس\nملاحظة : لفتح العضمة ارسل طك ورقم العضمة لأخذ المحبس أرسل جيب ورقم العضمة**")

@ABH.ar_cmd(pattern="محيبس")
async def restart_game(event):
    global group_game_status
    chat_id = event.chat_id
    if chat_id in group_game_status:
        group_game_status[chat_id]['is_game_started2'] = False
    await handle_clue(event)

@ABH.on(events.NewMessage(pattern=r'\طك (\d+)'))
async def handle_strike(event):
    global group_game_status, correct_answer, game_board
    chat_id = event.chat_id
    if chat_id in group_game_status and group_game_status[chat_id]['is_game_started2'] and event.sender_id == group_game_status[chat_id]['joker_player']:
        strike_position = int(event.pattern_match.group(1))
        if strike_position == correct_answer:
            game_board = [["💍" if i == correct_answer - 1 else "🖐️" for i in range(6)]]
            await event.reply(f"** خسرت شبيك مستعجل وجه الچوب 😒\n{format_board(game_board, numbers_board)}**")
            game_board = [row[:] for row in original_game_board]
            group_game_status[chat_id]['is_game_started2'] = False
            group_game_status[chat_id]['joker_player'] = None
        else:
            game_board[0][strike_position - 1] = '🖐️'
            lMl10l = random.choice(joker)
            await event.reply(f"**{lMl10l}**\n{format_board(game_board, numbers_board)}")

@ABH.on(events.NewMessage(pattern=r'\جيب (\d+)'))
async def handle_guess(event):
    global group_game_status, correct_answer, game_board
    chat_id = event.chat_id
    if chat_id in group_game_status and group_game_status[chat_id]['is_game_started2'] and event.sender_id == group_game_status[chat_id]['joker_player']:
        guess = int(event.pattern_match.group(1))
        if 1 <= guess <= 6:
            if guess == correct_answer:
                winner_id = event.sender_id
                if winner_id not in points:
                    points[winner_id] = 0
                points[winner_id] += 1
                sender = await event.get_sender()
                sender_first_name = sender.first_name if sender else 'مجهول'
                sorted_points = sorted(points.items(), key=lambda x: x[1], reverse=True)
                points_text = '\n'.join([f'{i+1}• {(await ABH.get_entity(participant_id)).first_name}: {participant_points}' for i, (participant_id, participant_points) in enumerate(sorted_points)])
                game_board = [["💍" if i == correct_answer - 1 else "🖐️" for i in range(6)]]
                await ABH.send_message(event.chat_id, f'الف مبروووك 🎉 الاعب ( {sender_first_name} ) وجد المحبس 💍!\n{format_board(game_board, numbers_board)}')
                game_board = [row[:] for row in original_game_board]
                await ABH.send_message(event.chat_id, f'نقاط الاعب : {points[winner_id]}\nنقاط المشاركين:\n{points_text}')
            else:
                game_board = [["💍" if i == correct_answer - 1 else "🖐️" for i in range(6)]]
                await event.reply(f"**ضاع البات ماضن بعد تلگونة ☹️\n{format_board(game_board, numbers_board)}**")
                game_board = [row[:] for row in original_game_board]
            group_game_status[chat_id]['is_game_started2'] = False
            group_game_status[chat_id]['joker_player'] = None

@ABH.on(events.NewMessage(pattern=r'\انا'))
async def handle_incoming_message(event):
    global group_game_status
    chat_id = event.chat_id
    if chat_id not in group_game_status:
        group_game_status[chat_id] = {
            'is_game_started2': False,
            'joker_player': None
        }
    if group_game_status[chat_id]['is_game_started2'] and not group_game_status[chat_id]['joker_player']:
        group_game_status[chat_id]['joker_player'] = event.sender_id
        await event.reply(f"**تم تسجيلك في المسابقة روح لحسين بظهرك\n{format_board(game_board, numbers_board)}**")

def format_board(game_board, numbers_board):
    formatted_board = ""
    formatted_board += " ".join(numbers_board[0]) + "\n"
    formatted_board += " ".join(game_board[0]) + "\n"
    return formatted_board
@ABH.ar_cmd(pattern="تصفير")
async def Husssein(event):
    global points
    points = {}
    await event.respond('**تم تصفير نقاط المشاركين بنجاح!**')



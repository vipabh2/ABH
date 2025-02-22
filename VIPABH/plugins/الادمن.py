import asyncio  
from asyncio import sleep

from telethon import functions
from telethon.errors import (
    BadRequestError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
)
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import (
    ChatAdminRights,
    ChatBannedRights,
    InputChatPhotoEmpty,
    MessageMediaPhoto,
)

from VIPABH import ABH

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type
from ..helpers.utils import _format, get_user_from_event
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID

# =================== STRINGS ============
PP_TOO_SMOL = "**᯽︙ الصورة صغيرة جدًا** "
PP_ERROR = "**᯽︙ فشل أثناء معالجة الصورة** "
NO_ADMIN = "**᯽︙ أنا لست مشرف هنا!!** "
NO_PERM = "**᯽︙ ليس لدي أذونات كافية!** "
CHAT_PP_CHANGED = "**᯽︙ تم تغيير صورة الدردشة بنجاح ✅**"
INVALID_MEDIA = "**᯽︙ ملحق غير صالح** "
joker_ban = "https://forkgraph.zaid.pro/file/2ReShkSyFhju"
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
UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

LOGS = logging.getLogger(__name__)
MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

plugin_category = "aadmin" 
# ================================================


@ABH.ar_cmd(
    pattern="الصورة( -وضع| -حذف)$",
    command=("الصورة", plugin_category),
    info={
        "᯽︙ الأسـتخدام": "For changing group display pic or deleting display pic",
        "᯽︙ الشـرح": "Reply to Image for changing display picture",
        "flags": {
            "-s": "To set group pic",
            "-d": "To delete group pic",
        },
        "᯽︙ الأمـر": [
            "{tr}الصورة -وضع <reply to image>",
            "{tr}gpic -حذف",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def set_group_photo(event):  # sourcery no-metrics
    "For changing Group dp"
    flag = (event.pattern_match.group(1)).strip()
    if flag == "-s":
        replymsg = await event.get_reply_message()
        photo = None
        if replymsg and replymsg.media:
            if isinstance(replymsg.media, MessageMediaPhoto):
                photo = await event.client.download_media(message=replymsg.photo)
            elif "image" in replymsg.media.document.mime_type.split("/"):
                photo = await event.client.download_file(replymsg.media.document)
            else:
                return await edit_delete(event, INVALID_MEDIA)
        if photo:
            try:
                await event.client(
                    EditPhotoRequest(
                        event.chat_id, await event.client.upload_file(photo)
                    )
                )
                await edit_delete(event, CHAT_PP_CHANGED)
            except PhotoCropSizeSmallError:
                return await edit_delete(event, PP_TOO_SMOL)
            except ImageProcessFailedError:
                return await edit_delete(event, PP_ERROR)
            except Exception as e:
                return await edit_delete(event, f"**خـطأ : **`{str(e)}`")
            process = "updated"
    else:
        try:
            await event.client(EditPhotoRequest(event.chat_id, InputChatPhotoEmpty()))
        except Exception as e:
            return await edit_delete(event, f"**خـطأ : **`{str(e)}`")
        process = "deleted"
        await edit_delete(event, "**᯽︙ تـم حذف الـصورة بنـجاح ✅")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#صوره_المجموعة\n"
            f"صورة المجموعه {process} بنجاح "
            f"الدردشه: {event.chat.title}(`{event.chat_id}`)",
        )
        from telethon.tl.functions.channels import EditAdminRequest
import asyncio
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import InputPeerUser
import asyncio

@ABH.ar_cmd(
    pattern="لقب(?:\s|$)([\s\S]*)",
    command=("لقب", plugin_category),
    info={
        "الامر": "᯽︙ لتغيير لقب شخص في المجموعة.",
        "الشرح": "᯽︙ لتغيير لقب شخص بالمجموعة قم بالرد على الشخص مع تحديد اللقب الجديد.\
            \n᯽︙ تحتاج إلى صلاحيات لتغيير اللقب.",
        "الاستخدام": [
            "{tr}لقب <لقب جديد> (بالرد على المستخدم)",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def promote(event):
    await event.delete()
    user, rank = await get_user_from_event(event)

    if not user:
        await event.reply("᯽︙ لم يتم العثور على المستخدم!")
        return

    if event.pattern_match.group(1):
        rank = event.pattern_match.group(1).strip()
    else:
        rank = "مشرف"

    try:
        input_user = InputPeerUser(user.id, user.access_hash)
        await event.client(EditAdminRequest(
            channel=event.chat_id,
            user_id=input_user,
            admin_rights=None,
            rank=rank
        ))
        reply_message = await event.reply(f"᯽︙ تم تغيير اللقب لـ {user.first_name} إلى {rank}!")
        await asyncio.sleep(4)
        await reply_message.delete()
    except Exception as e:
        await event.reply(f"᯽︙ حدث خطأ مع {user.first_name}: {str(e)}")

  
@ABH.ar_cmd(
    pattern="مشرف0(?:\s|$)([\s\S]*)",
    command=("مشرف0", plugin_category),
    info={
        "الامر": "᯽︙ لرفع الشخص مشرف مع صلاحيات",
        "الشرح": "᯽︙ لرفع الشخص مشرف بالمجموعة قم بالرد على الشخص\
            \n᯽︙ تـحتاج الصلاحـيات لـهذا الأمـر",
        "الاستخدام": [
            "{tr}رفع مشرف <ايدي/معرف/بالرد عليه>",
            "{tr}رفع مشرف <ايدي/معرف/بالرد عليه> <لقب>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def promote(event):
    "᯽︙ لـرفع مستخدم مشرف في الكروب"
    
    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=True,
        change_info=False,
        ban_users=False,
        delete_messages=False,
        pin_messages=False,
        manage_call=False,
        post_stories=True,
        edit_stories=True,
        delete_stories=True
    )
    
    await event.delete()  
    user, rank = await get_user_from_event(event)

    if event.pattern_match.group(1):
        rank = event.pattern_match.group(1).strip()
    else:
        rank = "مشرف"

    if user:
        try:
            await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
            
            reply_message = await event.reply(f"᯽︙ تم رفع {user.first_name} بلقب {rank}!")
            await asyncio.sleep(4) 
            await reply_message.delete()  
        except Exception as e:
            await event.reply(f"᯽︙ حدث خطأ أثناء رفع {user.first_name}: {str(e)}")
    else:
        await event.reply("᯽︙ لم يتم العثور على المستخدم!")
        await event.delete()  
@ABH.ar_cmd(
    pattern="مشرف(?:\s|$)([\s\S]*)",
    command=("مشرف", plugin_category),
    info={
        "الامر": "᯽︙ لرفع الشخص مشرف مع صلاحيات",
        "الشرح": "᯽︙ لرفع الشخص مشرف بالمجموعة قم بالرد على الشخص\
            \n᯽︙ تـحتاج الصلاحـيات لـهذا الأمـر",
        "الاستخدام": [
            "{tr}رفع مشرف <ايدي/معرف/بالرد عليه>",
            "{tr}رفع مشرف <ايدي/معرف/بالرد عليه> <لقب>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def promote(event):
    "᯽︙ لـرفع مستخدم مشرف في الكروب"
    
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=False,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
        post_stories=True,
        edit_stories=True,
        delete_stories=True
    )
    
    await event.delete()  
    user, rank = await get_user_from_event(event)

    if event.pattern_match.group(1):
        rank = event.pattern_match.group(1).strip()
    else:
        rank = "مشرف"

    if user:
        try:
            await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
            
            reply_message = await event.reply(f"᯽︙ تم رفع {user.first_name} بلقب {rank}!")
            await asyncio.sleep(4) 
            await reply_message.delete()  
        except Exception as e:
            await event.reply(f"᯽︙ حدث خطأ أثناء رفع {user.first_name}: {str(e)}")
    else:
        await event.reply("᯽︙ لم يتم العثور على المستخدم!")
        await event.delete()  
@ABH.ar_cmd(
    pattern="مشرف2(?:\s|$)([\s\S]*)",
    command=("مشرف2", plugin_category),
    info={
        "الامر": "᯽︙ لرفع الشخص مشرف مع صلاحيات",
        "الشرح": "᯽︙ لرفع الشخص مشرف بالمجموعة قم بالرد على الشخص\
            \n᯽︙ تـحتاج الصلاحـيات لـهذا الأمـر",
        "الاستخدام": [
            "{tr}رفع مشرف <ايدي/معرف/بالرد عليه>",
            "{tr}رفع مشرف <ايدي/معرف/بالرد عليه> <لقب>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def promote(event):
    "᯽︙ لـرفع مستخدم مشرف في الكروب"
    
    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=True,
        change_info=True,
        ban_users=False,
        delete_messages=True,
        pin_messages=True,
        manage_call=False,
        post_stories=True,
        edit_stories=True,
        delete_stories=True
    )
    
    await event.delete()  
    user, rank = await get_user_from_event(event)

    if event.pattern_match.group(1):
        rank = event.pattern_match.group(1).strip()
    else:
        rank = "مشرف"

    if user:
        try:
            await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
            
            reply_message = await event.reply(f"᯽︙ تم رفع {user.first_name} بلقب {rank}!")
            await asyncio.sleep(4) 
            await reply_message.delete()  
        except Exception as e:
            await event.reply(f"᯽︙ حدث خطأ أثناء رفع {user.first_name}: {str(e)}")
    else:
        await event.reply("᯽︙ لم يتم العثور على المستخدم!")
        await event.delete()  

@ABH.ar_cmd(
    pattern="نغيير لقب(?:\s|$)([\s\S]*)",
    command=("لقب", plugin_category),
    info={
        "الامر": "᯽︙ لتغيير لقب الشخص المشرف",
        "الشرح": "᯽︙ لتغيير لقب الشخص المشرف في المجموعة قم بالرد على الشخص\
            \n᯽︙ تـحتاج الصلاحيات لـهذا الأمـر",
        "الاستخدام": [
            "{tr}لقب <ايدي/معرف/بالرد عليه> <لقب>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def change_rank(event):
    "᯽︙ لـتغيير لقب مشرف في الكروب"
    
    if event.pattern_match.group(1):
        new_rank = event.pattern_match.group(1).strip()
    else:
        return await event.reply("᯽︙ يجب عليك تحديد اللقب الجديد!")

    user, _ = await get_user_from_event(event)

    if user:
        try:
            await event.client(EditAdminRequest(event.chat_id, user.id, None, new_rank))
            
            reply_message = await event.reply(f"᯽︙ تم تغيير لقب {user.first_name} إلى {new_rank}!")
            await asyncio.sleep(4) 
            await reply_message.delete() 
        except Exception as e:
            await event.reply(f"᯽︙ حدث خطأ أثناء تغيير لقب {user.first_name}: {str(e)}")
    else:
        await event.reply("᯽︙ لم يتم العثور على المستخدم!")
        await event.delete()  

@ABH.ar_cmd(
    pattern="تنزيل الكل(?:\s|$)([\s\S]*)",
    command=("تنزيل الكل", plugin_category),
    info={
        "الامر": "᯽︙ لتنزيل الشخص كن الاشراف",
        "الشرح": "᯽︙ يقوم هذا الامر بحذف جميع صلاحيات المشرف\
            \n᯽︙ ملاحظه :**لازم تكون انت الشخص الي رفعه او تكون مالك المجموعه حتى تنزله**",
        "الاستخدام": [
            "{tr}تك <الايدي/المعرف/بالرد عليه>",
            "{tr}تك <الايدي/المعرف/بالرد عليه>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def demote(event):
    "᯽︙ لـتنزيـل شـخص من الأشـراف"
    user, _ = await get_user_from_event(event)
    if not user:
        return
    catevent = await edit_or_reply(event, "**᯽︙ يـتم التنزيل من الاشراف**")
    newrights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
        manage_call=None

    )
    rank = "."
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, newrights, rank))
    except BadRequestError:
        return await catevent.edit(NO_PERM)
    await catevent.edit("**᯽︙ تـم تنزيله من قائمه الادمنيه بنجاح ✅**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#تنزيل_مشرف\
            \nالمعرف: [{user.first_name}](tg://user?id={user.id})\
            \nالدردشه: {event.chat.title}(`{event.chat_id}`)",
        )
@ABH.ar_cmd(
    pattern="طرد(?:\s|$)([\s\S]*)",
    command=("طرد", plugin_category),
    info={
        "᯽︙ الأسـتخدام": "لـطرد شـخض من الـكروب",
        "᯽︙ الشـرح": "لـطرد شخص من المـجموعة يستطيع الأنضـمام مرة اخـرى.\
        \n᯽︙ تـحتاج الصلاحـيات لـهذا الأمـر.",
        "᯽︙ الأمـر": [
            "{tr}طرد <الايدي/المعرف/بالرد عليه>",
            "{tr}طرد <الايدي/المعرف/بالرد عليه> <السبب> ",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def endmute(event):
    "لـطرد شـخض من الـكروب"
    user, reason = await get_user_from_event(event)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_delete(event, "**- لا يمڪنني حظر مطـوري دي لك**")
    catevent = await edit_or_reply(event, "᯽︙ يـتم طـرد الـمستخدم أنتـظر")
    try:
        await event.client.kick_participant(event.chat_id, user.id)
    except Exception as e:
        return await catevent.edit(NO_PERM + f"\n{str(e)}")
    if reason:
        await catevent.edit(
            f"᯽︙ الـمستخدم [{user.first_name}](tg://user?id={user.id})\n ᯽︙ تـم طرده بنجاح ✅ \n᯽︙ السـبب : {reason}"
        )
    else:
        await catevent.edit(f"᯽︙ الـمستخدم [{user.first_name}](tg://user?id={user.id})\n ᯽︙ تـم طرده بنجاح ✅ ")
@ABH.ar_cmd(
    pattern="حظر(?:\s|$)([\s\S]*)",
    command=("حظر", plugin_category),
    info={
        "᯽︙ الاستخدام": "يقـوم بـحظر شخـص في الـكروب الذي تـم اسـتخدام الأمر فيـه.",
        "᯽︙ الشرح": "لحـظر شخـص من الكـروب ومـنعه من الأنـضمام مجـددا. تـحتاج الصلاحـيات لـهذا الأمـر.",
        "᯽︙ الامر": [
            "{tr}حظر <الايدي/المعرف/بالرد عليه>",
            "{tr}حظر <الايدي/المعرف/بالرد عليه> <السبب>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def jokerban(event):
    "᯽︙ لحـظر شخص في كـروب مـعين"
    await event.delete()
    user, reason = await get_user_from_event(event)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_delete(event, "**- لا يمڪنني حظر مطـوري دي لك**")
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        return await edit_or_reply(event, NO_PERM)
    try:
        reply = await event.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        return await edit_or_reply(event, "᯽︙ ليـس لـدي جـميع الصـلاحيـات لكـن سيـبقى محـظور")
    if reason:
        await event.client.send_file(
            event.chat_id,
            joker_ban,
            caption=f"᯽︙ المسـتخدم {_format.mentionuser(user.first_name, user.id)} \n ᯽︙ تـم حـظره بنـجاح !!\n**⌔︙السبب : **`{reason}`"
        )
    else:
        await event.client.send_file(
            event.chat_id,
            joker_ban,
            caption=f"᯽︙ المسـتخدم {_format.mentionuser(user.first_name, user.id)} \n ᯽︙ تـم حـظره بنـجاح ✅"
        )
    if BOTLOG:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"᯽︙ الحـظر\
                \nالمسـتخدم: [{user.first_name}](tg://user?id={user.id})\
                \nالـدردشـة: {event.chat.title}\
                \nايدي الكروب(`{event.chat_id}`)\
                \nالسبـب : {reason}",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"᯽︙ الحـظر\
                \nالمسـتخدم: [{user.first_name}](tg://user?id={user.id})\
                \nالـدردشـة: {event.chat.title}\
                \n ايـدي الكـروب: (`{event.chat_id}`)",
            )


@ABH.ar_cmd(
    pattern="الغاء حظر(?:\s|$)([\s\S]*)",
    command=("الغاء حظر", plugin_category),
    info={
        "᯽︙ الأسـتخدام": "يقـوم بـالغاء حـظر الشـخص في الـكروب الذي اسـتخدمت فيـه الامر.",
        "᯽︙ الشرح": "لألـغاء حـظر شخـص من الكـروب والسـماح له من الأنـضمام مجـددا\
            \n᯽︙ تـحتاج الصلاحـيات لـهذا الأمـر.",
        "᯽︙ الأمـر": [
            "{tr}الغاء حظر <الايدي/المعرف/بالرد عليه>",
            "{tr}الغاء حظر <الايدي/المعرف/بالرد عليه> <السبب> ",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def nothanos(event):
    "᯽︙ لألـغاء الـحظر لـشخص في كـروب مـعين"
    user, _ = await get_user_from_event(event)
    if not user:
        return
    catevent = await edit_or_reply(event, "᯽︙ جـار الـغاء الـحظر أنتـظر رجـاءا")
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
        await catevent.edit(
            f"᯽︙ الـمستخدم {_format.mentionuser(user.first_name ,user.id)}\n ᯽︙ تـم الـغاء حـظره بنـجاح "
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "᯽︙ الـغاء الـحظر \n"
                f"الـمستخدم: [{user.first_name}](tg://user?id={user.id})\n"
                f"الـدردشـة: {event.chat.title}(`{event.chat_id}`)",
            )
    except UserIdInvalidError:
        await catevent.edit("᯽︙ يـبدو أن هذه الـعمليـة تم إلغاؤهـا")
    except Exception as e:
        await catevent.edit(f"**خـطأ :**\n`{e}`")


@ABH.ar_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        try:
            await event.delete()
        except Exception as e:
            LOGS.info(str(e))

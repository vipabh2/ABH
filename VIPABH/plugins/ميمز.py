# from VIPABH import ABH, bot
# import random
# from telethon import events
# from VIPABH import ABH
# from . import BOTLOG, BOTLOG_CHATID
# from .memes_sql import AljokerLink, get_link, add_link, delete_link, SESSION
# import base64

# plugin_category = "tools"


# @ABH.on(admin_cmd(outgoing=True, pattern="لطمية$"))
# async def jepThe(theme):
#     try:
#         الارقام_المحظورة = {25, 26, 40, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80}
#         الارقام_المسموحة = [i for i in range(24, 28) if i not in الارقام_المحظورة]
#         الرقم_المحدد = random.choice(الارقام_المسموحة)
#         الرابط = f"https://t.me/x04ou/{الرقم_المحدد}"
#         await theme.client.send_file(
#             theme.chat_id, 
#             الرابط, 
#             caption="᯽︙  اذكر القائم", 
#             parse_mode="html"
#         )
#         await theme.delete()
#     except Exception as e:
#         error_message = str(e)
#         message_link = f"https://t.me/c/{theme.chat_id}/{theme.id}" 
#         await theme.client.send_message(BOTLOG_CHATID,
#             f"❌ **حدث خطأ أثناء إرسال اللطمية**\n",
#             f"رابط الرسالة: {message_link}\n",
#             f"تفاصيل الخطأ: {error_message}\n\n",
#             f"رابط اللطمية الخاطئة: {الرابط}"
#         )
#         await theme.edit("❌ حدث خطأ أثناء إرسال اللطمية.")

# @ABH.on(admin_cmd(outgoing=True, pattern=r"ميمز (\S+) (.+)"))
# async def Hussein(event):
#     url = event.pattern_match.group(1)
#     lMl10l = event.pattern_match.group(2)
#     add_link(lMl10l, url)
#     await event.edit(f"**᯽︙ تم اضافة البصمة {lMl10l} بنجاح ✓ **")
#     ABH = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
#     ABH = Get(ABH)
#     try:
#         await event.client(ABH)
#     except BaseException:
#         pass

# @ABH.on(admin_cmd(outgoing=True, pattern="?(.*)"))
# async def Hussein(event):
#     lMl10l = event.pattern_match.group(1)
#     ABH = await reply_id(event)
#     url = get_link(lMl10l)
#     if url:
#         await event.client.send_file(event.chat_id, url, parse_mode="html", reply_to=ABH)
#         await event.delete()
#         ABH = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
#         ABH = Get(ABH)
#         try:
#             await event.client(ABH)
#         except BaseException:
#             pass

# @ABH.on(admin_cmd(outgoing=True, pattern="ازالة(?:\s|$)([\s\S]*)"))
# async def delete_alABH(event):
#     lMl10l = event.pattern_match.group(1)
#     delete_link(lMl10l)
#     await event.edit(f"**᯽︙ تم حذف البصمة '{lMl10l}' بنجاح ✓**")
#     ABH = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
#     ABH = Get(ABH)
#     try:
#         await event.client(ABH)
#     except BaseException:
#         pass

# @ABH.on(admin_cmd(outgoing=True, pattern="قائمة الميمز"))
# async def list_alABH(event):
#     links = SESSION.query(AljokerLink).all()
#     if links:
#         message = "**᯽︙ قائمة تخزين اوامر الميمز:**\n"
#         for link in links:
#             message += f"- البصمة : .`{link.key}`\n"
#     else:
#         message = "**᯽︙ لاتوجد بصمات ميمز مخزونة حتى الآن**"
#     await event.edit(message)
#     ABH = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
#     ABH = Get(ABH)
#     try:
#         await event.client(ABH)
#     except BaseException:
#         pass

# @ABH.on(admin_cmd(outgoing=True, pattern="ازالة_البصمات"))
# async def delete_all_alABH(event):
#     SESSION.query(AljokerLink).delete()
#     await event.edit("**᯽︙ تم حذف جميع بصمات الميمز من القائمة **")
#     ABH = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
#     ABH = Get(ABH)
#     try:
#         await event.client(ABH)
#     except BaseException:
#         pass
#     try:
#         await event.client(ABH)
#     except BaseException:
#         pass

from VIPABH import ABH, bot
import random
from telethon import events
from VIPABH import ABH
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "tools"


@ABH.on(admin_cmd(outgoing=True, pattern="لطمية$"))
async def jepThe(theme):
    try:
        الارقام_المحظورة = {25, 26, 40, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80}
        الارقام_المسموحة = [i for i in range(24, 28) if i not in الارقام_المحظورة]
        الرقم_المحدد = random.choice(الارقام_المسموحة)
        الرابط = f"https://t.me/x04ou/{الرقم_المحدد}"
        await theme.client.send_file(
            theme.chat_id, 
            الرابط, 
            caption="᯽︙  اذكر القائم", 
            parse_mode="html"
        )
        await theme.delete()
    except Exception as e:
        error_message = str(e)
        message_link = f"https://t.me/c/{theme.chat_id}/{theme.id}" 
        await theme.client.send_message(BOTLOG_CHATID,
            f"❌ **حدث خطأ أثناء إرسال اللطمية**\n",
            f"رابط الرسالة: {message_link}\n",
            f"تفاصيل الخطأ: {error_message}\n\n",
            f"رابط اللطمية الخاطئة: {الرابط}"
        )
        await theme.edit("❌ حدث خطأ أثناء إرسال اللطمية.")

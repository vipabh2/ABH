import random
from telethon import events
from VIPABH import ABH
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "tools"

# تأكد من أن BOTLOG_CHATID تم تعيينه بشكل صحيح في مكان ما
# BOTLOG_CHATID = "YOUR_BOT_LOG_CHAT_ID"  # استبدل بهذه القيمة من Config أو متغير آخر

@ABH.on(admin_cmd(outgoing=True, pattern="لطمية$"))
async def jepThe(theme):
    try:
        # توليد رقم عشوائي بين 19 و 170
        # rl = random.randint(19, 170)
        rl = random.randint(900, 902)
        
        # بناء الرابط باستخدام الرقم العشوائي
        url = f"https://t.me/x04ou/{rl}"
        
        # إرسال الرابط مع تعليق مخصص
        await theme.client.send_file(
            theme.chat_id, 
            url, 
            caption="᯽︙  اذكر القائم", 
            parse_mode="html"
        )
        
        # حذف الرسالة الأصلية بعد الإرسال
        await theme.delete()

    except Exception as e:
        # في حالة حدوث خطأ أثناء إرسال اللطمية، إرسال إشعار في مجموعة الإشعارات
        error_message = str(e)
        message_link = f"https://t.me/c/{theme.chat_id}/{theme.id}"  # رابط الرسالة في الدردشة
        
        # إرسال رسالة إلى مجموعة الإشعارات مع رابط الرسالة وتوضيح الخطأ
        await theme.client.send_message(
            BOTLOG_CHATID,
            f"❌ **حدث خطأ أثناء إرسال اللطمية**\n"
            f"رابط الرسالة: {message_link}\n"
            f"تفاصيل الخطأ: {error_message}\n\n"
            f"رابط اللطمية الخاطئة: {url}"
        )

        # إرسال إشعار في الدردشة الأصلية
        await theme.edit("❌ حدث خطأ أثناء إرسال اللطمية.")

from telethon.tl.types import (
    InputMessagesFilterDocument,
    InputMessagesFilterPhotos,
    InputMessagesFilterUrl
)
from JoKeRUB import l313l

plugin_category = "extra"

# قائمة المعرفات التي سيتم استثناؤها
excluded_user_ids = [793977288, 1421907917, 7308514832, 6387632922]

@l313l.ar_cmd(
    pattern="امسح(\s*| \d+)$",  # يسمح بإضافة عدد التكرار في الأمر إن رغبت
    command=("امسح", plugin_category),
    info={
        "header": "لحذف الرسائل من نوع معين.",
        "description": "يحذف الرسائل مثل الصور، الفيديوهات، الروابط، وغيرها بناءً على الفلاتر المحددة.",
        "usage": ["{tr}امسح"],
        "examples": "{tr}امسح",
    },
)
async def delete_filtered_messages(event):
    """حذف الرسائل بناءً على فلاتر محددة."""

    await event.delete()  # حذف الرسالة الأصلية لإخفاء الأمر

    try:
        # الفلاتر وأنواع الرسائل
        filters = {
            "الملفات": InputMessagesFilterDocument,
            "الروابط": InputMessagesFilterUrl,
            "الصور": InputMessagesFilterPhotos
        }

        total_deleted = 0  # إجمالي عدد الرسائل المحذوفة
        deleted_counts = {key: 0 for key in filters.keys()}  # عدد الرسائل المحذوفة لكل نوع

        # المرور على الفلاتر
        for msg_type, msg_filter in filters.items():
            async for message in event.client.iter_messages(event.chat_id, filter=msg_filter):
                # استثناء المعرفات المحددة
                if message.sender_id in excluded_user_ids:
                    continue 
                # حذف الرسالة
                if message:
                    await message.delete()
                    deleted_counts[msg_type] += 1
                    total_deleted += 1

        # الرد بالتفاصيل
        if total_deleted > 0:
            details = "\n".join([f"{msg_type}: {count}" for msg_type, count in deleted_counts.items() if count > 0])
            await event.reply(f"تم حذف {total_deleted} رسالة.\nالتفاصيل:\n{details}")
        else:
            await event.reply("لا توجد رسائل تطابق الفلاتر المحددة!")

    except Exception as e:
        # التعامل مع الأخطاء
        await event.reply(f"حدث خطأ أثناء الحذف: {str(e)}")

from telethon.tl.types import (
    InputMessagesFilterDocument,
    InputMessagesFilterPhotos,
    InputMessagesFilterUrl
)
from VIPABH import ABH
from telethon import events

plugin_category = "extra"

excluded_user_ids = [793977288, 1421907917, 7308514832, 6387632922, 7908156943]
uid = {
    1910015590, 890952036, 1446637898, 5914876113, 6498922948,
    7817624164, 7615088480, 6164435743, 5213325425, 1122162341,
    1260870186, 6783332896, 7722512961, 1494932118, 7483592520,
    201728276, 7497654775
}

@ABH.on(events.NewMessage(pattern=r"امسح(?:\s*|\d+)$"))  # إصلاح ال regex 
async def delete_filtered_messages(event):
    id = event.sender_id
    if id in uid:
        try:
            filters = {
                "الملفات": InputMessagesFilterDocument,
                "الروابط": InputMessagesFilterUrl,
                "الصور": InputMessagesFilterPhotos
            }
            total_deleted = 0
            deleted_counts = {key: 0 for key in filters.keys()}
            
            for msg_type, msg_filter in filters.items():
                async for message in event.client.iter_messages(event.chat_id, filter=msg_filter):
                    if message.sender_id in excluded_user_ids:
                        continue
                    await message.delete()
                    deleted_counts[msg_type] += 1
                    total_deleted += 1

            if total_deleted > 0:
                details = "\n".join([f"{msg_type}: {count}" for msg_type, count in deleted_counts.items() if count > 0])
                await event.reply(f" تم حذف {total_deleted} رسالة.\n📝 التفاصيل:\n{details}")
            else:
                await event.reply(" لا توجد رسائل تطابق الفلاتر المحددة!")
        
        except Exception as e:
            await event.reply(f" حدث خطأ أثناء الحذف: {str(e)}")

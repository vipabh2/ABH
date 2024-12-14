from datetime import datetime
from ..core.managers import edit_delete, edit_or_reply

@ABH.ar_cmd(pattern="مواليد(?:\s|$)([\s\S]*)")
async def _(event):
    yar = event.text[12:].strip()  # استبعاد المسافات
    if not yar or not yar.isdigit():
        return await edit_or_reply(event, "**✾╎استخـدم الامر كالتالي: حساب العمر + السنة**")

    YearNow = datetime.now().year  # الحصول على السنة الحالية
    try:
        birth_year = int(yar)  # تحويل السنة المدخلة إلى عدد صحيح
        MyAge = YearNow - birth_year  # حساب العمر
        await edit_or_reply(event, f"**🚹╎عمرك هـو : {MyAge} سنة**")
    except ValueError:
        return await edit_or_reply(event, "**✾╎حدث خطأ، تأكد من إدخال سنة صحيحة.**")

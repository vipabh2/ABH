from asyncio import sleep
from vipabh import abh

plugin_category = "utils"

@ABH.ar_cmd(
    pattern=r"^مؤجل (\d+)\s+([\s\S]+)$", 
    command=("مؤجل", plugin_category),
    info={
        "header": "لجدولة رسالة بعد عدد معين من الثواني.",
        "usage": "{tr}مؤجل <عدد الثواني> <النص لإرساله>",
        "examples": "{tr}مؤجل 120 مرحباً ",
    },
)
async def _(event):
    "لجدولة رسالة بعد عدد معين من الثواني"
    try:
        # استخراج عدد الثواني والنص من الرسالة المدخلة
        args = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        
        if len(args) < 2:
            await event.respond("᯽︙ يرجى تحديد عدد الثواني والنص الذي ترغب في إرساله.")
            return

        time_input = args[0]
        message = args[1]

        try:
            ttl = int(time_input)
        except ValueError:
            await event.respond("᯽︙ يجب إدخال عدد صحيح من الثواني.")
            return

        if ttl <= 0:
            await event.respond("᯽︙ الوقت يجب أن يكون أكبر من الصفر.")
            return

        await event.delete()
        await sleep(ttl)

        await event.respond(message)

    except Exception as e:
        await event.respond(f"᯽︙ حدث خطأ: {str(e)}")

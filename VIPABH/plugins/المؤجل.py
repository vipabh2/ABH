from asyncio import sleep
from vipabh import abh
from datetime import datetime

plugin_category = "utils"

@ABH.ar_cmd(
    pattern=r"^مؤجل (\d{4}/\d{2}/\d{2}) (\d+:\d{2})\s+([\s\S]+)$",  # النمط الجديد الذي يقبل التاريخ والوقت
    command=("مؤجل", plugin_category),
    info={
        "header": "لجدولة رسالة بعد وقت محدد باستخدام تاريخ ووقت (yyyy/mm/dd m:ss).",
        "usage": "{tr}مؤجل <التاريخ بصيغة yyyy/mm/dd> <الوقت بصيغة m:ss> <النص لإرساله>",
        "examples": "{tr}مؤجل 2024/12/21 2:10 مرحباً ",
    },
)
async def _(event):
    "لجدولة رسالة بعد وقت محدد باستخدام تاريخ ووقت"
    try:
        args = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)

        if len(args) < 3:
            await event.respond("᯽︙ يرجى تحديد التاريخ والوقت والنص الذي ترغب في إرساله.")
            return

        date_input = args[0]
        time_input = args[1]
        message = args[2]

        try:
            scheduled_date = datetime.strptime(date_input, "%Y/%m/%d")
        except ValueError:
            await event.respond("᯽︙ صيغة التاريخ غير صحيحة. يرجى استخدام الصيغة yyyy/mm/dd.")
            return

        if ":" in time_input:
            minutes, seconds = map(int, time_input.split(":"))
            if seconds >= 60:  # التأكد من أن الثواني أقل من 60
                await event.respond("᯽︙ صيغة الوقت غير صحيحة، الثواني يجب أن تكون أقل من 60.")
                return
            ttl = minutes * 60 + seconds
        else:
            await event.respond("᯽︙ صيغة الوقت غير صحيحة. يرجى استخدام الصيغة m:ss.")
            return

        current_time = datetime.now()
        if scheduled_date < current_time:
            await event.respond("᯽︙ التاريخ المدخل هو في الماضي. يرجى تحديد تاريخ مستقبلي.")
            return

        time_difference = (scheduled_date - current_time).total_seconds() + ttl

        if time_difference <= 0:
            await event.respond("᯽︙ الوقت يجب أن يكون أكبر من الصفر.")
            return

        await event.delete()
        await sleep(time_difference)

        await event.respond(message)

    except ValueError:
        await event.respond("᯽︙ صيغة الوقت أو التاريخ غير صحيحة.")
    except Exception as e:
        await event.respond(f"᯽︙ حدث خطأ: {str(e)}")

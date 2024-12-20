from asyncio import sleep
from vipabh import abh

plugin_category = "utils"


@ABH.ar_cmd(
    pattern="مؤجل (\d+:\d+|\d+) ([\s\S]*)",
    command=("مؤجل", plugin_category),
    info={
        "header": "لجدولة رسالة بعد وقت محدد (بالدقائق والثواني أو بالثواني فقط).",
        "usage": "{tr}مؤجل <الوقت بصيغة m:ss أو عدد الثواني> <النص لإرساله>",
        "examples": "{tr}مؤجل 2:00 مرحباً ",
    },
)
async def _(event):
    "لجدولة رسالة بعد وقت محدد"
    try:
        args = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        time_input = args[0]
        message = args[1]

        if ":" in time_input:
            minutes, seconds = map(int, time_input.split(":"))
            ttl = minutes * 60 + seconds
        else:
            ttl = int(time_input)

        await event.delete()
        await sleep(ttl)
        await event.respond(message)
    except Exception as e:
        await event.respond(f"حدث خطأ: {str(e)}")

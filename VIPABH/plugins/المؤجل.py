from asyncio import sleep
from vipabh import abh

plugin_category = "utils"

@ABH.ar_cmd(
    pattern=r"^مؤجل (\d+:\d{2})\s+([\s\S]+)$",  # النمط يتأكد من صيغة m:ss فقط
    command=("مؤجل", plugin_category),
    info={
        "header": "لجدولة رسالة بعد وقت محدد (بالدقائق والثواني فقط).",
        "usage": "{tr}مؤجل <الوقت بصيغة m:ss> <النص لإرساله>",
        "examples": "{tr}مؤجل 2:10 مرحباً ",
    },
)
async def _(event):
    "لجدولة رسالة بعد وقت محدد بصيغة m:ss"
    try:
        args = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        
        if len(args) < 2:
            await event.respond("᯽︙ يرجى تحديد الوقت والنص الذي ترغب في إرساله.")
            return

        time_input = args[0]
        message = args[1]

        if ":" in time_input:
            minutes, seconds = map(int, time_input.split(":"))
            if seconds >= 60: 
                await event.respond("᯽︙ صيغة الوقت غير صحيحة، الثواني يجب أن تكون أقل من 60.")
                return
            ttl = minutes * 60 + seconds
        else:
            await event.respond("᯽︙ صيغة الوقت غير صحيحة. يرجى استخدام الصيغة m:ss.")
            return

        if ttl <= 0:
            await event.respond("᯽︙ الوقت يجب أن يكون أكبر من الصفر.")
            return

        await event.delete()
        await sleep(ttl)

        await event.respond(message)

    except ValueError:
        await event.respond("᯽︙ صيغة الوقت غير صحيحة. يرجى استخدام الصيغة m:ss.")
    except Exception as e:
        await event.respond(f"᯽︙ حدث خطأ: {str(e)}")

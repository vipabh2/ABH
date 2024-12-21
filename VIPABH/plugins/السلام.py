from telethon import events
from VIPABH import ABH

plugin_category = "extra"

auto_replay = False  

@ABH.ar_cmd(pattern="السلام تعطيل")
async def auto_replay_off(event):
    global auto_replay
    auto_replay = False
    await event.reply("تم تعطيل الرد التلقائي على السلام.")

@ABH.ar_cmd(pattern="السلام تفعيل")
async def auto_replay_on(event):
    global auto_replay
    auto_replay = True 
    await event.reply("تم تفعيل الرد التلقائي على السلام.")

@ABH.ar_cmd(
    incoming=True,
    func=lambda e: e.text and (e.text.strip().lower() == "السلام عليكم" or e.text.strip().lower() == "سلام عليكم"),
    edited=False
)
async def reply_salam(event):
    if event.sender.id in banned_users:
        return  

    if not auto_replay:
        return 

    await event.reply("عليكم السلام")

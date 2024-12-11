import sys
import contextlib
import VIPABH
from VIPABH import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from .Config import Config
from .core.logger import logging
from .core.session import ABH
from .utils import (
    add_bot_to_logger_group,
    install_externalrepo,
    load_plugins,
    setup_bot,
    mybot,
    startupmessage,
    verifyLoggerGroup,
    saves,
)

LOGS = logging.getLogger("VIPABH")
imam_ali = """
⣿⣿⣿⣿⣿⢿⠛⢛⠿⠉⠉⠉⡉⢙⣻⠻⠻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠟⢁⡠⠀⠄⠀⠀⠀⠉⠙⠒⠃⠾⠹⣲⡘⠿⣿⣿⣿
⣿⡿⠁⠀⠀⠀⠈⠛⠚⠉⠉⠛⠉⠙⠳⠖⣤⢌⡑⠂⠞⢿⣿
⡟⠐⠂⠅⡠⠂⠁⠀⠀⢀⣴⣦⣶⣶⣶⣦⣌⠘⢮⡔⡈⠙⣿
⠁⢀⠄⡈⠄⢀⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⡆⠈⢣⠈⠜⣿
⠄⠑⡨⠈⠀⢠⣴⠿⡿⣿⣿⣿⣿⣿⣿⡿⠟⠻⡄⠈⢸⡀⠚
⡤⠪⠀⠀⢠⣿⣥⡴⠦⠤⠉⣙⣿⣿⠡⡔⠾⠟⣾⠀⠨⢀⠘
⠃⠀⠀⠀⢸⣿⣤⡠⠧⢤⡻⢼⣿⣿⣼⣿⣤⣧⣿⠀⡄⢸⠀
⠀⣀⠀⠀⠀⣿⣿⣿⣷⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⡄⢀⢸⠀
⠠⡇⠀⠀⠀⢹⣿⡿⣿⣿⣏⡖⢿⣿⢓⣽⣿⣿⣿⠁⢨⢸⠀
⠠⠇⠀⠀⠀⠀⠫⣿⣿⠟⠉⠀⠀⠄⠀⠉⠙⢿⡟⠀⠈⠸⠀
⡐⡆⠀⠀⠀⠀⠀⠘⠁⠀⢀⡐⠒⠒⠢⠂⠀⠀⠂⠀⢀⠀⠀
⣹⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢰
⢺⠀⠀⠀⠈⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⡘
⡎⠀⠀⠀⠀⠄⣇⠠⢄⠀⠀⠀⠀⠀⠀⣀⡀⡄⠀⠀⠀⠀⡇
⠄⠀⠀⠀⠀⡇⣷⡀⠩⡇⣠⣮⣶⣿⠿⣫⡾⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⣷⠑⠳⠋⣾⡿⠟⣫⢵⡿⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠐⠁⢀⣴⠀⣩⡖⡽⠝⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣴⡏⣫⣾⠟⠉⢀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⢟⠕⠋⢀⣠⣲⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠠⣷⠋⣠⠞⣰⣿⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⠁⣼⡟⣼⡏⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢁⣾⣯⢃⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⢤⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣲⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡿⣜⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡟⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⣼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣽⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢰⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⡇⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⣿⠇⠀⢀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣶⡆⢹⡇⢠⣴⣶⣶⠀⣿⡇⠀⣸⣷⠀⠀⠀
⠀⠀⢸⡇⠀⢸⡯⣿⣷⣾⣷⣾⣿⣶⣶⠀⣿⣶⣶⣿⣿⠀⠀⠀
⠀⠀⠙⢿⣶⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⠀⡶⠀⠀⠀
⠀⠀⠀⠾⠐⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
print(VIPABH.__copyright__)
print("Licensed under the terms of the " + VIPABH.__license__)
print(imam_ali)
cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("جارِ بدء بوت ABH ✓")
    ABH.loop.run_until_complete(setup_bot())
    LOGS.info("تم اكتمال تنصيب البوت ✓")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()

try:
    LOGS.info("يتم تفعيل وضع الانلاين")
    ABH.loop.run_until_complete(mybot())
    LOGS.info("تم تفعيل وضع الانلاين بنجاح ✓")
except Exception as jep:
    LOGS.error(f"- {jep}")
    sys.exit()    

async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("᯽︙بـوت ABH يعـمل بـنجاح ")
    print(
        f"تم تشغيل الانلاين تلقائياً ارسل {cmdhr}الاوامر لـرؤيـة اوامر السورس")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    await verifyLoggerGroup()
    await saves()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    return

async def externalrepo():
    if Config.VCMODE:
        await install_externalrepo("https://github.com/jepthoniq/JepVc", "jepvc", "jepthonvc")

ABH.loop.run_until_complete(externalrepo())
ABH.loop.run_until_complete(startup_process())

if len(sys.argv) in {1, 3, 4}:
    with contextlib.suppress(ConnectionError):
        ABH.run_until_disconnected()
else:
    ABH.disconnect()

import sys
import VIPABH
from VIPABH import BOTLOG_CHATID, PM_LOGGER_GROUP_ID
from .Config import Config
from .core.logger import logging
from .core.session import ABH

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
"""

print(VIPABH.__copyright__)
print("Licensed under the terms of the " + VIPABH.__license__)
print(imam_ali)
cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("جارِ بدء سورس ABH ✓")
    ABH.loop.run_until_complete(setup_bot())
    LOGS.info("تم اكتمال تنصيب السورس ✓")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()

async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("᯽︙سورس ABH يعـمل بـنجاح ")
    print(
        f"تم تشغيل الانلاين تلقائياً ارسل {cmdhr}الاوامر لـرؤيـة اوامر السورس\
        \nللمسـاعدة تواصـل  https://t.me/K_4X1"
    )
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
        await install_externalrepo("https://github.com/VIPABH/ABH")

ABH.loop.run_until_complete(externalrepo())
ABH.loop.run_until_complete(startup_process())
ABH.run_until_disconnected()

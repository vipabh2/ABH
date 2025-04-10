import time

import heroku3

from .Config import Config
from .core.logger import logging
from .core.session import ABH
from .sql_helper.globals import addgvar, delgvar, gvarstatus

__version__ = "3.1.3"
__license__ = "كـتابة وتـعديل ABH"
__copyright__ = "abh (C) 2024"
__author__ = "ABH <https://T.ME/k_4x1>"

ABH.version = __version__
ABH.tgbot.version = __version__
LOGS = logging.getLogger("ABH")
bot = ABH

StartTime = time.time()
JEPVERSION = "3.1.3"

if Config.UPSTREAM_REPO == "abh":
    UPSTREAM_REPO_URL = "https://github.com/vipabh/abh"
else:
    UPSTREAM_REPO_URL = Config.UPSTREAM_REPO

if Config.PRIVATE_GROUP_BOT_API_ID == 0:
    if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is None:
        Config.BOTLOG = False
        Config.BOTLOG_CHATID = "me"  # تعيين القيمة الافتراضية
    else:
        Config.BOTLOG_CHATID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))
        Config.PRIVATE_GROUP_BOT_API_ID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))
        Config.BOTLOG = True
else:
    if str(Config.PRIVATE_GROUP_BOT_API_ID)[0] != "-":
        Config.BOTLOG_CHATID = int("-" + str(Config.PRIVATE_GROUP_BOT_API_ID))
    else:
        Config.BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID
    Config.BOTLOG = True

# التحقق من BOTLOG_CHATID إذا لم يتم تحديد قيمة صالحة
if not Config.BOTLOG_CHATID or Config.BOTLOG_CHATID == "me":
    print("⚠️ لم يتم العثور على BOTLOG_CHATID. يرجى تحديد معرف صالح (ID) أو كتابة 'me' لاستقبال الرسائل في حسابك الشخصي.")
    user_input = input("أدخل BOTLOG_CHATID (أو اتركه فارغًا لاستخدام 'me'): ").strip()
    if user_input:
        try:
            Config.BOTLOG_CHATID = int(user_input)
        except ValueError:
            Config.BOTLOG_CHATID = "me"
    else:
        Config.BOTLOG_CHATID = "me"
    print(f"تم تعيين BOTLOG_CHATID إلى: {Config.BOTLOG_CHATID}")

if Config.PM_LOGGER_GROUP_ID == 0:
    if gvarstatus("PM_LOGGER_GROUP_ID") is None:
        Config.PM_LOGGER_GROUP_ID = -100
    else:
        Config.PM_LOGGER_GROUP_ID = int(gvarstatus("PM_LOGGER_GROUP_ID"))
elif str(Config.PM_LOGGER_GROUP_ID)[0] != "-":
    Config.PM_LOGGER_GROUP_ID = int("-" + str(Config.PM_LOGGER_GROUP_ID))
try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except Exception:
    HEROKU_APP = None

# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
CMD_LIST = {}
SUDO_LIST = {}
# for later purposes
INT_PLUG = ""
LOAD_PLUG = {}

# Variables
BOTLOG = Config.BOTLOG
BOTLOG_CHATID = Config.BOTLOG_CHATID
PM_LOGGER_GROUP_ID = Config.PM_LOGGER_GROUP_ID

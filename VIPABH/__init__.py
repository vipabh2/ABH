import time
import heroku3
from .Config import Config
from .core.logger import logging
from .core.session import ABH
from .sql_helper.globals import addgvar, delgvar, gvarstatus

__version__ = "3.1.3"
__license__ = "تـعديل فريـق abh"
__author__ = "abh <https://T.ME/k_4x1>"
__copyright__ = "ABH TEAM (C) 2021 - 2023  " + __author__

ABH.version = __version__
ABH.tgbot.version = __version__
LOGS = logging.getLogger("abh")
bot = ABH

StartTime = time.time()
JEPVERSION = "3.1.3"

# تحديد مستودع المشروع
UPSTREAM_REPO_URL = (
    "https://github.com/vipabh/abh"
    if Config.UPSTREAM_REPO == "abh"
    else Config.UPSTREAM_REPO
)

# التعامل مع PRIVATE_GROUP_BOT_API_ID
if Config.PRIVATE_GROUP_BOT_API_ID == 0:
    botlog_chat_id = gvarstatus("PRIVATE_GROUP_BOT_API_ID")
    if botlog_chat_id is None:
        Config.BOTLOG = False
        Config.BOTLOG_CHATID = "me"
    else:
        try:
            Config.BOTLOG_CHATID = int(botlog_chat_id)
        except ValueError:
            LOGS.error(f"Invalid BOTLOG_CHATID value: '{botlog_chat_id}'. Setting BOTLOG to False.")
            Config.BOTLOG = False
        else:
            if str(Config.BOTLOG_CHATID)[0] != "-":
                Config.BOTLOG_CHATID = int("-" + str(Config.BOTLOG_CHATID))
            Config.BOTLOG = True
else:
    Config.BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID
    Config.BOTLOG = True

# التعامل مع PM_LOGGER_GROUP_ID
if Config.PM_LOGGER_GROUP_ID == 0:
    pm_logger_id = gvarstatus("PM_LOGGER_GROUP_ID")
    if pm_logger_id is None:
        Config.PM_LOGGER_GROUP_ID = -100
    else:
        try:
            Config.PM_LOGGER_GROUP_ID = int(pm_logger_id)
        except ValueError:
            LOGS.error(f"Invalid PM_LOGGER_GROUP_ID value: '{pm_logger_id}'. Setting default to -100.")
            Config.PM_LOGGER_GROUP_ID = -100
        else:
            if str(Config.PM_LOGGER_GROUP_ID)[0] != "-":
                Config.PM_LOGGER_GROUP_ID = int("-" + str(Config.PM_LOGGER_GROUP_ID))
else:
    if str(Config.PM_LOGGER_GROUP_ID)[0] != "-":
        Config.PM_LOGGER_GROUP_ID = int("-" + str(Config.PM_LOGGER_GROUP_ID))

# إعداد اتصال Heroku
try:
    if Config.HEROKU_API_KEY and Config.HEROKU_APP_NAME:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps().get(Config.HEROKU_APP_NAME)
    else:
        HEROKU_APP = None
except Exception as e:
    LOGS.error(f"Error connecting to Heroku: {e}")
    HEROKU_APP = None

# تعريف المتغيرات العامة
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
CMD_LIST = {}
SUDO_LIST = {}
INT_PLUG = ""
LOAD_PLUG = {}

# المتغيرات النهائية
BOTLOG = Config.BOTLOG
BOTLOG_CHATID = Config.BOTLOG_CHATID
PM_LOGGER_GROUP_ID = Config.PM_LOGGER_GROUP_ID

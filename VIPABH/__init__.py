import time
import heroku3
from .Config import Config
from .core.logger import logging
from .core.session import ABH
from .sql_helper.globals import addgvar, delgvar, gvarstatus

__version__ = "3.1.3"
__license__ = "كـتابة وتـعديل فريـق الجوكر"
__author__ = "الجوكر <https://T.ME/Jepthon>"
__copyright__ = "AlJOKER TEAM (C) 2021 - 2023  " + __author__

ABH.version = __version__
ABH.tgbot.version = __version__
LOGS = logging.getLogger("ABH")
bot = ABH

StartTime = time.time()
JEPVERSION = "3.1.3"

# إعداد المستودع الرئيسي
if Config.UPSTREAM_REPO == "jepthoniq":
    UPSTREAM_REPO_URL = "https://github.com/redaiq90/jepthon"
else:
    UPSTREAM_REPO_URL = Config.UPSTREAM_REPO

# إعداد PRIVATE_GROUP_BOT_API_ID
try:
    if Config.PRIVATE_GROUP_BOT_API_ID == 0:
        if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is None:
            Config.BOTLOG = False
            Config.BOTLOG_CHATID = "me"
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
except ValueError as e:
    LOGS.error(f"Error in setting PRIVATE_GROUP_BOT_API_ID: {e}")
    Config.BOTLOG = False
    Config.BOTLOG_CHATID = "me"

# إعداد PM_LOGGER_GROUP_ID
try:
    if Config.PM_LOGGER_GROUP_ID == 0:
        if gvarstatus("PM_LOGGER_GROUP_ID") is None:
            Config.PM_LOGGER_GROUP_ID = -100
        else:
            Config.PM_LOGGER_GROUP_ID = int(gvarstatus("PM_LOGGER_GROUP_ID"))
    elif str(Config.PM_LOGGER_GROUP_ID)[0] != "-":
        Config.PM_LOGGER_GROUP_ID = int("-" + str(Config.PM_LOGGER_GROUP_ID))
except ValueError as e:
    LOGS.error(f"Error in setting PM_LOGGER_GROUP_ID: {e}")
    Config.PM_LOGGER_GROUP_ID = -100

# إعداد تطبيق Heroku
try:
    if Config.HEROKU_API_KEY is not None and Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except Exception as e:
    LOGS.error(f"Error connecting to Heroku: {e}")
    HEROKU_APP = None

# المتغيرات العالمية
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

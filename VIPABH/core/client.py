import datetime
import inspect
import re
import sys
import traceback
from pathlib import Path
from typing import Dict, List, Union
from ..sql_helper.globals import gvarstatus
from telethon import TelegramClient, events
from telethon.errors import MessageIdInvalidError, MessageNotModifiedError
from ..Config import Config
from ..helpers.utils.events import checking
from ..helpers.utils.format import paste_message
from ..helpers.utils.utils import runcmd
from ..sql_helper.globals import gvarstatus
from . import BOT_INFO, CMD_INFO, GRP_INFO, LOADED_CMDS, PLG_INFO
from .cmdinfo import _format_about
from .data import _sudousers_list, blacklist_chats_list, sudo_enabled_cmds
from .events import *
from .fasttelethon import download_file, upload_file
from .logger import logging
from .managers import edit_delete
from .pluginManager import get_message_link, restart_script

LOGS = logging.getLogger(__name__)

DEVJOKR = [1910015590]
class REGEX:
    def __init__(self):
        self.regex = ""
        self.regex1 = ""
        self.regex2 = ""


REGEX_ = REGEX()
sudo_enabledcmds = sudo_enabled_cmds()


class HuReClient(TelegramClient):
    def ar_cmd(
        self: TelegramClient,
        pattern: str or tuple = None,
        info: Union[str, Dict[str, Union[str, List[str], Dict[str, str]]]]
        or tuple = None,
        groups_only: bool = False,
        private_only: bool = False,
        allow_sudo: bool = True,
        edited: bool = True,
        forword=False,
        disable_errors: bool = False,
        command: str or tuple = None,
        **kwargs,
    ) -> callable:  # sourcery no-metrics
        kwargs["func"] = kwargs.get("func", lambda e: e.via_bot_id is None)
        kwargs.setdefault("forwards", forword)
        if gvarstatus("blacklist_chats") is not None:
            kwargs["blacklist_chats"] = True
            kwargs["chats"] = blacklist_chats_list()
        stack = inspect.stack()
        previous_stack_frame = stack[1]
        file_test = Path(previous_stack_frame.filename)
        # file_test = file test.stem.replace(".py", "")
        if command is not None:
            command = list(command)
            if not command[1] in BOT_INFO:
                BOT_INFO.append(command[1])
            try:
                if file_test not in GRP_INFO[command[1]]:
                    GRP_INFO[command[1]].append(file_test)
            except BaseException:
                GRP_INFO.update({command[1]: [file_test]})
            try:
                if command[0] not in PLG_INFO[file_test]:
                    PLG_INFO[file_test].append(command[0])
            except BaseException:
                PLG_INFO.update({file_test: [command[0]]})
            if not command[0] in CMD_INFO:
                CMD_INFO[command[0]] = [_format_about(info)]
        if pattern is not None:
            if (
                pattern.startswith(r"\#")
                or not pattern.startswith(r"\#")
                and pattern.startswith(r"^")
            ):
                REGEX_.regex1 = REGEX_.regex2 = re.compile(pattern)
            else:
                reg1 = "\\" + Config.COMMAND_HAND_LER
                reg2 = "\\" + Config.SUDO_COMMAND_HAND_LER
                REGEX_.regex1 = re.compile(reg1 + pattern)
                REGEX_.regex2 = re.compile(reg2 + pattern)

        def decorator(func):  # sourcery no-metrics
            async def wrapper(check):
                if gvarstatus("blockedfrom") == "yes":
                    await edit_delete(check, "**انت محظور من استعمال السورس من قبل المطور**")
                    return
                chat = check.chat
                # if hasattr(chat, "title"):
                #     if( "ALjoker" in     chat.title and not (chat.admin_rights or chat.creator) and not (check.sender_id in DEVJOKR)
                #     ):
                #         await edit_delete(check, "** ᯽︙ لا يمكنني استخدام سورس ABH هنا في هذه المجموعة 🤷🏻 **")
                #         return
                if groups_only and not check.is_group:
                    await edit_delete(check, "`لا أعتقد ان هذه مجموعة, جرب بلكروب عزيزي.`", 10)
                    return
                if private_only and not check.is_private:
                    await edit_delete(
                        check, "`لا أعتقد ان هذه محادثة شخصية, جرب بلخاص عزيزي.`", 10
                    )
                    return
                try:
                    await func(check)
                except events.StopPropagation:
                    raise events.StopPropagation
                except KeyboardInterrupt:
                    pass
                except MessageNotModifiedError:
                    LOGS.error("Message was same as previous message")
                except MessageIdInvalidError:
                    LOGS.error("Message was deleted or cant be found")
                except BaseException as e:
                    LOGS.exception(e)
                    if not disable_errors:
                        if Config.PRIVATE_GROUP_BOT_API_ID == 0:
                            return
                        date = (datetime.datetime.now()).strftime("%m/%d/%Y, %H:%M:%S")
                        ftext = f"\nDisclaimer:\nThis file is pasted only here ONLY here,\
                                  \nwe logged only fact of error and date,\nwe respect your privacy,\
                                  \nyou may not report this error if you've\
                                  \nany confidential data here, no one will see your data\
                                  \n\n--------BEGIN VIPABH TRACEBACK LOG--------\
                                  \nDate: {date}\nGroup ID: {str(check.chat_id)}\
                                  \nSender ID: {str(check.sender_id)}\
                                  \nMessage Link: {await check.client.get_msg_link(check)}\
                                  \n\nEvent Trigger:\n{str(check.text)}\
                                  \n\nTraceback info:\n{str(traceback.format_exc())}\
                                  \n\nError text:\n{str(sys.exc_info()[1])}"
                        new = {
                            "error": str(sys.exc_info()[1]),
                            "date": datetime.datetime.now(),
                        }
                        ftext += "\n\n--------END VIPABH TRACEBACK LOG--------"
                        command = 'git log --pretty=format:"%an: %s" -5'
                        ftext += "\n\n\nLast 5 commits:\n"
                        output = (await runcmd(command))[:2]
                        result = output[0] + output[1]
                        ftext += result
                        pastelink = await paste_message(
                            ftext, pastetype="s", markdown=False
                        )
                        text = "**تقرير خطا ABH**\n\n"
                        link = "[هنا](https://t.me/k_4x1)"
                        text += "إذا كنت تريد الإبلاغ عن ذلك"
                        text += f"- فقط قم بإعادة توجيه هذه الرسالة {link}.\n"
                        text += "لا يتم تسجيل اي خطا فقط التاريخ والوقت\n\n"
                        text += f"**⌯︙تقرير الخطأ : ** [{new['error']}]({pastelink})"
                        await check.client.send_message(
                            Config.PRIVATE_GROUP_BOT_API_ID, text, link_preview=False
                        )

            from .session import ABH

            if not func.__doc__ is None:
                CMD_INFO[command[0]].append((func.__doc__).strip())
            if pattern is not None:
                if command is not None:
                    if command[0] in LOADED_CMDS and wrapper in LOADED_CMDS[command[0]]:
                        return None
                    try:
                        LOADED_CMDS[command[0]].append(wrapper)
                    except BaseException:
                        LOADED_CMDS.update({command[0]: [wrapper]})
                if edited:
                    ABH.add_event_handler(
                        wrapper,
                        MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                ABH.add_event_handler(
                    wrapper,
                    NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                )
                if allow_sudo and gvarstatus("sudoenable") is not None:
                    if command is None or command[0] in sudo_enabledcmds:
                        if edited:
                            ABH.add_event_handler(
                                wrapper,
                                MessageEdited(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        ABH.add_event_handler(
                            wrapper,
                            NewMessage(
                                pattern=REGEX_.regex2,
                                from_users=_sudousers_list(),
                                **kwargs,
                            ),
                        )
            else:
                if file_test in LOADED_CMDS and func in LOADED_CMDS[file_test]:
                    return None
                try:
                    LOADED_CMDS[file_test].append(func)
                except BaseException:
                    LOADED_CMDS.update({file_test: [func]})
                if edited:
                    ABH.add_event_handler(func, events.MessageEdited(**kwargs))
                ABH.add_event_handler(func, events.NewMessage(**kwargs))
            return wrapper

        return decorator

    def bot_cmd(
        self: TelegramClient,
        disable_errors: bool = False,
        edited: bool = False,
        **kwargs,
    ) -> callable:  # sourcery no-metrics
        kwargs["func"] = kwargs.get("func", lambda e: e.via_bot_id is None)

        def decorator(func):
            async def wrapper(check):
                try:
                    await func(check)
                except events.StopPropagation:
                    raise events.StopPropagation
                except KeyboardInterrupt:
                    pass
                except MessageNotModifiedError:
                    LOGS.error("Message was same as previous message")
                except MessageIdInvalidError:
                    LOGS.error("Message was deleted or cant be found")
                except BaseException as e:
                    # Check if we have to disable error logging.
                    LOGS.exception(e)  # Log the error in console
                    if not disable_errors:
                        if Config.PRIVATE_GROUP_BOT_API_ID == 0:
                            return
                        date = (datetime.datetime.now()).strftime("%m/%d/%Y, %H:%M:%S")
                        ftext = f"\nDisclaimer:\nThis file is pasted only here ONLY here,\
                                    \nwe logged only fact of error and date,\nwe respect your privacy,\
                                    \nyou may not report this error if you've\
                                    \nany confidential data here, no one will see your data\
                                    \n\n--------BEGIN VIPABH TRACEBACK LOG--------\
                                    \nDate: {date}\nGroup ID: {str(check.chat_id)}\
                                    \nSender ID: {str(check.sender_id)}\
                                    \nMessage Link: {await check.client.get_msg_link(check)}\
                                    \n\nEvent Trigger:\n{str(check.text)}\
                                    \n\nTraceback info:\n{str(traceback.format_exc())}\
                                    \n\nError text:\n{str(sys.exc_info()[1])}"
                        new = {
                            "error": str(sys.exc_info()[1]),
                            "date": datetime.datetime.now(),
                        }
                        ftext += "\n\n--------END VIPABH TRACEBACK LOG--------"
                        command = 'git log --pretty=format:"%an: %s" -5'
                        ftext += "\n\n\nLast 5 commits:\n"
                        output = (await runcmd(command))[:2]
                        result = output[0] + output[1]
                        ftext += result
                        pastelink = await paste_message(
                            ftext, pastetype="s", markdown=False
                        )
                        text = "**تقرير خطا ABH**\n\n"
                        link = "[هنا](https://t.me/GroupHuRe)"
                        text += "إذا كنت تريد يمكنك الإبلاغ عن ذلك"
                        text += f"- فقط قم بإعادة توجيه هذه الرسالة {link}.\n"
                        text += "لا يتم تسجيل اي خطا فقط التاريخ والوقت\n\n"
                        text += f"**⌯︙تقرير الخطأ : ** [{new['error']}]({pastelink})"
                        await check.client.send_message(
                            Config.PRIVATE_GROUP_BOT_API_ID, text, link_preview=False
                        )

            from .session import ABH

            if edited is True:
                ABH.tgbot.add_event_handler(func, events.MessageEdited(**kwargs))
            else:
                ABH.tgbot.add_event_handler(func, events.NewMessage(**kwargs))

            return wrapper

        return decorator

    async def get_traceback(self, exc: Exception) -> str:
        return "".join(
            traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__)
        )

    def _kill_running_processes(self) -> None:
        """Kill all the running asyncio subprocessess"""
        for _, process in self.running_processes.items():
            try:
                process.kill()
                LOGS.debug("Killed %d which was still running.", process.pid)
            except Exception as e:
                LOGS.debug(e)
        self.running_processes.clear()



HuReClient.fast_download_file = download_file
HuReClient.fast_upload_file = upload_file
HuReClient.reload = restart_script
HuReClient.get_msg_link = get_message_link
HuReClient.check_testcases = checking
try:
    send_message_check = TelegramClient.send_message
except AttributeError:
    HuReClient.send_message = send_message
    HuReClient.send_file = send_file
    HuReClient.edit_message = edit_message


from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from ..core.logger import logging

LOGS = logging.getLogger(__name__)


# Admin checker by uniborg
async def is_admin(ABH, chat_id, userid):
    if not str(chat_id).startswith("-100"):
        return False
    try:
        req_jo = await ABH.get_permissions(chat_id, userid)
        chat_participant = req_jo.participant
        if isinstance(
            chat_participant, (ChannelParticipantCreator, ChannelParticipantAdmin)
        ):
            return True
    except Exception as e:
        return False
    else:
        return False

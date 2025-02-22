import html
import os
import random
from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

from VIPABH import ABH
from random import choice
from ABH.razan.resources.strings import *
from telethon import events
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch
from telethon.utils import get_display_name
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format

plugin_category = "utils"



rehu = [
    "شكم مره كتلك خلي نفلش الكروب",
    "باع هذا اللوكي شديسوي",
    "** مالك الكروب واحد زباله ويدور بنات **",
    "**اول مره اشوف بنات يدورن ولد 😂 **",
    "** راح اعترفلك بشي طلعت احب اختك 🥺 **",
    "**مالك الكروب والمشرفين وفرده من قندرتك ضلعي**",
    "**هذا واحد غثيث وكلب ابن كلب**",
    "**لتحجي كدامه هذا يوصل حجي**",
    "**هذا المالك واحد ساقط وقرام ويدور حلوين**",
    "**يفشلون شنو هاي دضحك**",
    "**عسل مو فشار**"
]

@ABH.on(admin_cmd(pattern="رفع مرتي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    VIPABH = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"🚻 ** ᯽︙  المستخدم => • ** [{VIPABH}](tg://user?id={user.id}) \n ☑️ **᯽︙  تم رفعها مرتك بواسطه  :**{my_mention} 👰🏼‍♀️.\n**᯽︙  يلا حبيبي امشي نخلف بيبي 👶🏻🤤** ")

@ABH.on(admin_cmd(pattern="رفع جلب(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{VIPABH}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه جلب 🐶 بواسطة :** {my_mention} \n**᯽︙  خليه خله ينبح 😂**")

@ABH.on(admin_cmd(pattern="رفع تاج(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"᯽︙ المستخدم [{VIPABH}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه تاج بواسطة :** {my_mention} 👑🔥")

@ABH.on(admin_cmd(pattern="رفع قرد(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"᯽︙ المستخدم [{VIPABH}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه قرد واعطائه موزة 🐒🍌 بواسطة :** {my_mention}")

@ABH.on(admin_cmd(pattern="رفع بكلبي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{VIPABH}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه بكلـبك 🤍 بواسطة :** {my_mention} \n**᯽︙  انت حبي الابدي 😍**")
    
    

@ABH.on(admin_cmd(pattern="رفع مطي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{VIPABH}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه مطي 🐴 بواسطة :** {my_mention} \n**᯽︙  تعال حبي استلم  انه **")
    
#كـتابة المـلف وتعديل.    :   السيد حسين.   اخمط وسمي روحك مطور فرخي 😂
# اذا انت ابن حرام اخمط 😂
# اي بعدك تريد تخمط ترا من تخمط مراح تنجح


@ABH.on(admin_cmd(pattern="رفع زوجي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{VIPABH}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه زوجج بواسطة :** {my_mention} \n**᯽︙  يلا حبيبي امشي نخلف 🤤🔞**")
    

@ABH.on(admin_cmd(pattern="رفع زاحف(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{VIPABH}](tg://user?id={user.id}) \n**᯽︙  تـم رفع المتهم زاحف اصلي بواسطة :** {my_mention} \n**᯽︙  ها يلزاحف شوكت تبطل سوالفك حيوان 😂🐍**")

@ABH.on(admin_cmd(pattern="رفع كحبة(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{VIPABH}](tg://user?id={user.id}) \n**᯽︙  تـم رفع المتهم كحبة 👙 بواسطة :** {my_mention} \n**᯽︙  ها يلكحبة طوبز خلي انيجك/ج**")

@ABH.on(admin_cmd(pattern="رفع فرخ(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{VIPABH}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه فرخ الكروب بواسطة :** {my_mention} \n**᯽︙  لك الفرخ استر على خمستك ياهو اليجي يزورهاً 👉🏻👌🏻**")

@ABH.ar_cmd(
    pattern="رزله(?:\s|$)([\s\S]*)",
    command=("رزله", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"᯽︙ ولك [{tag}](tg://user?id={user.id}) \n᯽︙  هيو لتندك بسيادك لو بهاي 👞👈")

@ABH.on(admin_cmd(pattern="رفع حاته(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{VIPABH}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـها حاته الكروب 🤤😻 بواسطة :** {my_mention} \n**᯽︙  تعاي يعافيتي اريد حضن دافي 😽**")

@ABH.on(admin_cmd(pattern="رفع هايشة(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{VIPABH}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه المتهم هايشة 🐄 بواسطة :** {my_mention} \n**᯽︙  ها يلهايشة خوش بيك حليب تعال احلبك 😂**")

@ABH.on(admin_cmd(pattern="رفع صاك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{VIPABH}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه صاك 🤤 بواسطة :** {my_mention} \n**᯽︙  تعال يلحلو انطيني بوسة من رگبتك 😻🤤**")

@ABH.ar_cmd(
    pattern="مصه(?:\s|$)([\s\S]*)",
    command=("مصه", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"** ⣠⡶⠚⠛⠲⢄⡀\n⣼⠁      ⠀⠀⠀⠳⢤⣄\n⢿⠀⢧⡀⠀⠀⠀⠀⠀⢈⡇\n⠈⠳⣼⡙⠒⠶⠶⠖⠚⠉⠳⣄\n⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄\n⠀⠀⠀⠘⣆       ⠀⠀⠀⠀⠀⠈⠓⢦⣀\n⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤\n⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧\n⠀⠀⠀⠀⠀⠀⠀    ⠓⠦⠀⠀⠀⠀**\n**🚹 ¦ تعال مصه عزيزي ** [{tag}](tg://user?id={user.id})")
from telethon import events
import asyncio
from module_name import admin_cmd, edit_or_reply

@ABH.on(admin_cmd(pattern="سيد(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    await edit_or_reply(mention, "عليكم السلام , اهلا")
@ABH.on(admin_cmd(pattern="رفع ايجة(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{VIPABH}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه ايچة 🤤 بواسطة :** {my_mention} \n**᯽︙  ها يلأيچة تطلعين درب بـ$25 👙**")

@ABH.on(admin_cmd(pattern="رفع زبال(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{VIPABH}](tg://user?id={user.id}) \n**᯽︙  تـم رفعـه زبال الكروب 🧹 بواسطة :** {my_mention} \n**᯽︙  تعال يلزبال اكنس الكروب لا أهينك 🗑😹**")

@ABH.on(admin_cmd(pattern="رفع كواد(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{VIPABH}](tg://user?id={user.id}) \n**᯽︙  تـم رفعه كواد بواسطة :** {my_mention} \n**᯽︙  تعال يكواد عرضك مطشر اصير حامي عرضك ؟😎**")

@ABH.on(admin_cmd(pattern="رفع ديوث(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ المستخدم** [{VIPABH}](tg://user?id={user.id}) \n**᯽︙  تـم رفعه ديوث الكروب بواسطة :** {my_mention} \n**᯽︙  تعال يلديوث جيب اختك خلي اتمتع وياها 🔞**")

@ABH.on(admin_cmd(pattern="رفع مميز(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ الحلو** 「[{VIPABH}](tg://user?id={user.id})」 \n**᯽︙  تـم رفعه مميز بواسطة :** {my_mention}")

@ABH.on(admin_cmd(pattern="رفع ادمن(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ الحلو** 「[{VIPABH}](tg://user?id={user.id})」 \n**᯽︙  تـم رفعه ادمن بواسطة :** {my_mention}")

@ABH.on(admin_cmd(pattern="رفع منشئ(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ الحلو** 「[{VIPABH}](tg://user?id={user.id})」 \n**᯽︙  تـم رفعه منشئ بواسطة :** {my_mention}")

@ABH.on(admin_cmd(pattern="رفع مالك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1910015590:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    VIPABH = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙ الحلو** 「[{VIPABH}](tg://user?id={user.id})」 \n**᯽︙  تـم رفعه مالك الكروب بواسطة :** {my_mention}")

@ABH.on(admin_cmd(pattern="رفع مجنب(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    VIPABH = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f" ** ᯽︙  المستخدم => • ** [{VIPABH}](tg://user?id={user.id}) \n ☑️ **᯽︙  تم رفعه مجنب بواسطه  :**{my_mention} .\n**᯽︙  كوم يلمجنب اسبح مو عيب تضرب جلغ 😹** ")

@ABH.on(admin_cmd(pattern="رفع وصخ(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    VIPABH = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"** ᯽︙  المستخدم => • ** [{VIPABH}](tg://user?id={user.id}) \n ☑️ **᯽︙  تم رفعه وصخ الكروب 🤢 بواسطه  :**{my_mention} .\n**᯽︙  لك دكوم يلوصخ اسبح مو ريحتك كتلتنا 🤮 ** ")

@ABH.on(admin_cmd(pattern="زواج(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    VIPABH = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"᯽︙ ** لقد تم زواجك/ج من : **[{VIPABH}](tg://user?id={user.id}) 💍\n**᯽︙  الف الف مبروك الان يمكنك اخذ راحتك ** ")

@ABH.on(admin_cmd(pattern="طلاك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    VIPABH = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙  انتِ طالق طالق طالق 🙎🏻‍♂️ من  :**{my_mention} .\n**᯽︙  لقد تم طلاقها بلثلاث وفسخ زواجكما الان الكل حر طليق ** ")
lMl10l = [1374312239, 393120911, 1910015590, 5564802580]
@ABH.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.reply_to and event.sender_id in lMl10l:
       reply_msg = await event.get_reply_message()
       owner_id = reply_msg.from_id.user_id
       if owner_id == ABH.uid:
           if event.message.message == "منصب؟":
               await event.reply("**يب منصب ✓**")
           elif event.message.message == "منو فخر العرب؟":
               await event.reply("**الأمام علي عليه الصلاة والسلام ❤️**")
           elif event.message.message == "منو تاج راسك":
               await event.reply("** ابن هاشم تاج راسي ❤️**")
@ABH.on(admin_cmd(pattern="همسه(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    VIPABH = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    lMl10l = random.choice(rehu)
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙الهمسة من المستخدم [{VIPABH}](tg://user?id={user.id}) تم كشفها بنجاح ✓**\n**᯽︙  الهمسة هي : {lMl10l} ** ")

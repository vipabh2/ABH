
import asyncio
import time
from VIPABH import ABH
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from telethon.events import NewMessage
import requests
from telethon.tl.functions.users import GetFullUserRequest
from ..Config import Config
import re
from telethon import events
c = requests.session()
bot_username = '@EEObot'
bot_username2 = '@A_MAN9300BOT'
bot_username3 = '@MARKTEBOT'
bot_username4 = '@qweqwe1919bot'
bot_username5 = '@xnsex21bot'
bot_username6 = '@DamKombot'
bot_username8 = '@Bellllen192BOT'
VIPABH = ['yes']
ConsoleJoker = Config.T7KM
its_Reham = False
its_hussein = False
its_reda = False
its_joker = False
#اياثارات الحسين
#by Aljoker doesn't steal codes Please
@ABH.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("تجميع المليار") and str(event.sender_id) in ConsoleJoker:
        await event.reply("**᯽︙سيتم تجميع النقاط من بوت المليار , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await ABH.get_entity(bot_username)
        await ABH.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await ABH.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await ABH.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await ABH(GetHistoryRequest(peer=channel_entity, limit=1,
                                                offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ABH.send_message(event.chat_id, f"تم الانتهاء من التجميع")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ABH(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await ABH(ImportChatInviteRequest(bott))
                msg2 = await ABH.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await ABH.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await ABH.send_message(event.chat_id, "تم الانتهاء من التجميع")
@ABH.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in ConsoleJoker:
        await ABH.send_message(bot_username, "/start")
        await event.reply("** ᯽︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")
    
@ABH.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("تجميع ABH") and str(event.sender_id) in ConsoleJoker:
        await event.reply("**᯽︙سيتم تجميع النقاط من بوت ABH , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await ABH.get_entity(bot_username2)
        await ABH.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(2)
        msg0 = await ABH.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(2)
        msg1 = await ABH.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(2)

            list = await ABH(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ABH.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ABH(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await ABH(ImportChatInviteRequest(bott))
                msg2 = await ABH.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await ABH.send_message("me", f"تم الاشتراك في {chs} قناة")
            except Exception as er:
                await ABH.send_message(event.chat_id, f"**خطأ , ممكن تبندت**\n{er}")
        await ABH.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    #else:
        #await event.edit("يجب الدفع لاستعمال هذا الامر !")
@ABH.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("تجميع العقاب") and str(event.sender_id) in ConsoleJoker:
        await event.reply("**᯽︙سيتم تجميع النقاط من بوت العقاب , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await ABH.get_entity(bot_username3)
        await ABH.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(3)
        msg0 = await ABH.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(3)
        msg1 = await ABH.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(3)
            list = await ABH(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ABH.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ABH(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await ABH(ImportChatInviteRequest(bott))
                msg2 = await ABH.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await ABH.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await ABH.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
        await ABH.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    #else:
        #await event.edit("يجب الدفع لاستعمال هذا الامر !")
@ABH.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("تجميع المليون") and str(event.sender_id) in ConsoleJoker:
        await event.reply("**᯽︙سيتم تجميع النقاط من بوت المليون , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await ABH.get_entity(bot_username4)
        await ABH.send_message('@qweqwe1919bot', '/start')
        await asyncio.sleep(2)
        msg0 = await ABH.get_messages('@qweqwe1919bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(2)
        msg1 = await ABH.get_messages('@qweqwe1919bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(2)

            list = await ABH(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ABH.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ABH(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await ABH(ImportChatInviteRequest(bott))
                msg2 = await ABH.get_messages('@qweqwe1919bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await ABH.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await ABH.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
        await ABH.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

   # else:
     #   await event.edit("يجب الدفع لاستعمال هذا الامر !")

@ABH.on(admin_cmd(pattern="(تجميع المليار|تجميع مليار)"))
async def _(event):
    await event.edit("**᯽︙سيتم تجميع النقاط من بوت المليار , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await ABH.get_entity(bot_username)
    await ABH.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await ABH.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await ABH.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await ABH(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await ABH.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break

        url = msgs.reply_markup.rows[0].buttons[0].url

        try:
            try:
                await ABH(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await ABH(ImportChatInviteRequest(bott))
            msg2 = await ABH.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await ABH.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")

    await ABH.send_message(event.chat_id, "تم الانتهاء من التجميع")
        
@ABH.on(admin_cmd(pattern="(ايقاف التجميع|ايقاف تجميع)"))
async def cancel_collection(event):
    await ABH.send_message('@EEObot', '/start')
    await event.edit("** ᯽︙ تم الغاء التجميع من بوت المليار **")
    
@ABH.on(admin_cmd(pattern="(تجميع ABH|تجميع جوكر)"))
async def _(event):
    if VIPABH[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت ABH , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await ABH.get_entity(bot_username2)
        await ABH.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(2)
        msg0 = await ABH.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(2)
        msg1 = await ABH.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if VIPABH[0] == 'no':
                break
            await asyncio.sleep(2)

            list = await ABH(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ABH.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ABH(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await ABH(ImportChatInviteRequest(bott))
                msg2 = await ABH.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await ABH.send_message("me", f"تم الاشتراك في {chs} قناة")
            except Exception as er:
                await ABH.send_message(event.chat_id, f"**خطأ , ممكن تبندت**\n{er}")
        await ABH.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

  #  else:
    #    await event.edit("يجب الدفع لاستعمال هذا الامر !")
@ABH.on(admin_cmd(pattern="(تجميع العقاب|تجميع عقاب)"))
async def _(event):
    if VIPABH[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت العقاب , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await ABH.get_entity(bot_username3)
        await ABH.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(3)
        msg0 = await ABH.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(3)
        msg1 = await ABH.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if VIPABH[0] == 'no':
                break
            await asyncio.sleep(3)

            list = await ABH(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ABH.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ABH(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await ABH(ImportChatInviteRequest(bott))
                msg2 = await ABH.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await ABH.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await ABH.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
        await ABH.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

 #   else:
   #     await event.edit("يجب الدفع لاستعمال هذا الامر !")
@ABH.on(admin_cmd(pattern="(تجميع المليون|تجميع مليون)"))
async def _(event):
    if VIPABH[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت المليون , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await ABH.get_entity(bot_username4)
        await ABH.send_message('@qweqwe1919bot', '/start')
        await asyncio.sleep(2)
        msg0 = await ABH.get_messages('@qweqwe1919bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(2)
        msg1 = await ABH.get_messages('@qweqwe1919bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if VIPABH[0] == 'no':
                break
            await asyncio.sleep(2)

            list = await ABH(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ABH.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ABH(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await ABH(ImportChatInviteRequest(bott))
                msg2 = await ABH.get_messages('@qweqwe1919bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await ABH.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await ABH.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
        await ABH.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

#    else:
  #      await event.edit("يجب الدفع لاستعمال هذا الامر !")
@ABH.on(admin_cmd(pattern="(تجميع العرب|تجميع عرب)"))
async def _(event):
    await event.edit("**᯽︙سيتم تجميع النقاط من بوت العرب , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await ABH.get_entity(bot_username5)
    await ABH.send_message(bot_username5, '/start')
    await asyncio.sleep(4)
    msg0 = await ABH.get_messages(bot_username5, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await ABH.get_messages(bot_username5, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await ABH(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await ABH.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break

        url = msgs.reply_markup.rows[0].buttons[0].url

        try:
            try:
                await ABH(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await ABH(ImportChatInviteRequest(bott))
            msg2 = await ABH.get_messages(bot_username5, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await ABH.get_messages(bot_username5, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")

    await ABH.send_message(event.chat_id, "تم الانتهاء من التجميع")
@ABH.on(admin_cmd(pattern="تجميع دعمكم"))
async def _(event):
    await event.edit("**᯽︙سيتم تجميع النقاط من بوت دعمكم , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await ABH.get_entity(bot_username6)
    await ABH.send_message('@DamKombot', '/start')
    await asyncio.sleep(4)
    msg0 = await ABH.get_messages(bot_username6, limit=1)
    await msg0[0].click(1)
    await asyncio.sleep(4)
    msg1 = await ABH.get_messages(bot_username6, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await ABH(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات حالياً 🤍') != -1:
            await ABH.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        msg_text = msgs.message  # الكود تمت كتابتهُ من قبل سورس ABH 
        if "اشترك فالقناة @" in msg_text:
            aljoker_channel = msg_text.split('@')[1].split()[0]
            try:
                entity = await ABH.get_entity(aljoker_channel)
                if entity:
                    await ABH(JoinChannelRequest(entity.id))
                    await asyncio.sleep(4)
                    msg2 = await ABH.get_messages(bot_username6, limit=1)
                    await msg2[0].click(text='اشتركت ✅')
                    chs += 1
                    await event.edit(f"تم الانظمام الى القناة رقم {chs}")
            except:
                await ABH.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
                break

    await ABH.send_message(event.chat_id, "تم الانتهاء من التجميع")

@ABH.on(admin_cmd(pattern="(تجميع عراق|تجميع العراق)"))
async def _(event):
    await event.edit("**᯽︙سيتم تجميع النقاط من بوت العراق , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await ABH.get_entity(bot_username8)
    await ABH.send_message(bot_username8, '/start')
    await asyncio.sleep(4)
    msg0 = await ABH.get_messages(bot_username8, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await ABH.get_messages(bot_username8, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await ABH(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await ABH.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break

        url = msgs.reply_markup.rows[0].buttons[0].url

        try:
            try:
                await ABH(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await ABH(ImportChatInviteRequest(bott))
            msg2 = await ABH.get_messages(bot_username8, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await ABH.get_messages(bot_username8, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")

    await ABH.send_message(event.chat_id, "تم الانتهاء من التجميع")
    
@ABH.ar_cmd(pattern="راتب وعد(?:\s|$)([\s\S]*)")
async def hussein(event):
    global its_hussein
    await event.delete()
    if not its_hussein:
        its_hussein = True
        if event.is_group:
            await send_reham(event)
        else:
            await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")

async def send_reham(event):
    await event.respond('راتب')
    await asyncio.sleep(660)
    global its_hussein
    if its_hussein:
        await send_reham(event)  
@ABH.ar_cmd(pattern="ايقاف راتب وعد(?:\s|$)([\s\S]*)")
async def hussein(event):
    global its_hussein
    its_hussein = False
    await event.edit("**تم تعطيل راتب وعد بنجاح ✅**")
@ABH.ar_cmd(pattern="بخشيش وعد(?:\s|$)([\s\S]*)")
async def hussein(event):
    global its_joker
    await event.delete()
    if not its_joker:
        its_joker = True
        if event.is_group:
            await send_aljoker(event)
        else:
            await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")
async def send_aljoker(event):
    await event.respond('بخشيش')
    await asyncio.sleep(660)
    global its_joker
    if its_joker:
        await send_aljoker(event)  
@ABH.ar_cmd(pattern="ايقاف بخشيش وعد(?:\s|$)([\s\S]*)")
async def hussein(event):
    global its_joker
    its_joker = False
    await event.edit("**᯽︙ تم تعطيل بخشيش وعد بنجاح ✓ **")
@ABH.ar_cmd(pattern="سرقة وعد(?:\s|$)([\s\S]*)")
async def hussein(event):
    global its_reda
    await event.delete()
    if not its_reda:
        its_reda = True
        if event.is_group:
            message = event.pattern_match.group(1).strip()
            if message:
                await send_message(event, message)
            else:
                await event.edit("**يرجى كتابة ايدي الشخص مع الامر!**")

async def send_message(event, message):
    await event.respond(f"زرف {message}")
    await asyncio.sleep(660)
    global its_reda
    if its_reda:
        await send_message(event, message)

@ABH.ar_cmd(pattern="ايقاف سرقة وعد(?:\s|$)([\s\S]*)")
async def Reda(event):
    global its_reda
    its_reda = False
    await event.edit("** ᯽︙ تم ايقاف السرقة بنجاح ✓ **")
client = ABH

@ABH.ar_cmd(pattern="استثمار وعد")
async def w3d_joker(event):
    await event.delete()
    global its_Reham
    its_Reham = True
    while its_Reham:
        if event.is_group:
            await event.client.send_message(event.chat_id, "فلوسي")
            await asyncio.sleep(3)
            aljoker = await event.client.get_messages(event.chat_id, limit=1)
            aljoker = aljoker[0].message
            aljoker = ("".join(aljoker.split(maxsplit=2)[2:])).split(" ", 2)
            ABH = aljoker[0]
            if ABH.isdigit() and int(ABH) > 500000000:
                await event.client.send_message(event.chat_id,f"استثمار {ABH}")
                await asyncio.sleep(5)
                joker = await event.client.get_messages(event.chat_id, limit=1)
                await joker[0].click(text="اي ✅")
            else:
                await event.client.send_message(event.chat_id, f"استثمار {ABH}")
            await asyncio.sleep(1210)
        
        else:
            await event.edit("** ᯽︙ امر الاستثمار يمكنك استعماله في المجموعات فقط 🖤**")
@ABH.ar_cmd(pattern="ايقاف استثمار وعد")
async def disable_w3d(event):
    global its_Reham
    its_Reham = False
    await event.edit("**تم تعطيل عملية الاستثمار وعد.**")

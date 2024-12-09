import contextlib 
import os
import shutil

from telethon.errors.rpcerrorlist import MediaEmptyError
from JoKeRUB import l313l
from ..core.managers import edit_or_reply
from ..helpers.google_image_download import googleimagesdownload
from ..helpers.utils import reply_id

plugin_category = "misc"

@l313l.ar_cmd(
    pattern="صور(?: |$)(\d*)? ?([\s\S]*)",
    command=("صور", plugin_category),
    info={
        "header": "Google image search.",
        "description": "To search images in Google. By default, will send 3 images. You can get more images (up to 10) by changing the limit value as shown in usage and examples.",
        "usage": ["{tr}img <1-10> <query>", "{tr}img <query>"],
        "examples": [
            "{tr}img 10 catuserbot",
            "{tr}img catuserbot",
            "{tr}img 7 catuserbot",
        ],
    },
)
async def img_sampler(event):
    "Google image search."
    reply_to_id = await reply_id(event)
    
    # Check if the command is a reply and extract the query
    if event.is_reply and not event.pattern_match.group(2):
        query_message = await event.get_reply_message()
        query = str(query_message.message)
    else:
        query = str(event.pattern_match.group(2)).strip()
    
    # Check if the query is empty
    if not query:
        return await edit_or_reply(event, "**᯽︙ قم بكتابة النص مع الأمر أو الرد على النص.**")
    
    # Notify user that the search is in progress
    cat = await edit_or_reply(event, "**᯽︙ جارِ البحث عن الصور، انتظر قليلاً ✓**")
    
    # Determine the limit for images
    lim = event.pattern_match.group(1)
    if lim and lim.isdigit():
        lim = min(int(lim), 10)
    else:
        lim = 3
    
    # Prepare arguments for Google image search
    response = googleimagesdownload()
    arguments = {
        "keywords": query.replace(",", " "),
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory",
    }
    
    # Perform the image search
    try:
        paths = response.download(arguments)
    except Exception as e:
        return await cat.edit(f"خطأ: \n`{e}`")
    
    # Get the list of image paths
    lst = paths[0].get(query.replace(",", " "), [])
    
    # Send the images to the chat
    if not lst:
        return await cat.edit("᯽︙ لم يتم العثور على أي صور.")
    
    for i in lst:
        try:
            await event.client.send_file(event.chat_id, i, reply_to=reply_to_id)
        except MediaEmptyError:
            continue  # Skip if the file is empty
    
    # Cleanup the downloaded files
    try:
        shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    except Exception as e:
        print(f"خطأ أثناء حذف الملفات: {e}")

    await cat.delete()

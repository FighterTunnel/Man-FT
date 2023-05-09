# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" ft module for frying stuff. ported by @NeoMatrix90 """

import io
from random import randint, uniform

from PIL import Image, ImageEnhance, ImageOps

from ft import CMD_HANDLER as cmd
from ft import CMD_HELP
from ft.utils import check_media, edit_delete, edit_or_reply, man_cmd


@man_cmd(pattern="deepfry(?: |$)(.*)")
async def deepfryer(event):
    try:
        frycount = int(event.pattern_match.group(1))
        if frycount < 1:
            raise ValueError
    except ValueError:
        frycount = 1
    if event.is_reply:
        reply_message = await event.get_reply_message()
        data = await check_media(reply_message)
        if isinstance(data, bool):
            return await edit_delete(event, "`I can't deep fry that!`")
    else:
        return await edit_delete(
            event, "`Reply to an image or sticker to deep fry it!`"
        )
    # download last photo (highres) as byte array
    xx = await edit_or_reply(event, "`Downloading media…`")
    image = io.BytesIO()
    await event.client.download_media(data, image)
    image = Image.open(image)
    # fry the image
    await xx.edit("`Deep frying media…`")
    for _ in range(frycount):
        image = await deepfry(image)
    fried_io = io.BytesIO()
    fried_io.name = "image.jpeg"
    image.save(fried_io, "JPEG")
    fried_io.seek(0)
    await xx.delete()
    await event.send_file(event.chat_id, file=fried_io, reply_to=event.reply_to_msg_id)


async def deepfry(img: Image) -> Image:
    colours = (
        (randint(50, 200), randint(40, 170), randint(40, 190)),
        (randint(190, 255), randint(170, 240), randint(180, 250)),
    )

    img = img.copy().convert("RGB")

    # Crush image to hell and back
    img = img.convert("RGB")
    width, height = img.width, img.height
    img = img.resize(
        (int(width ** uniform(0.8, 0.9)), int(height ** uniform(0.8, 0.9))),
        resample=Image.LANCZOS,
    )
    img = img.resize(
        (int(width ** uniform(0.85, 0.95)), int(height ** uniform(0.85, 0.95))),
        resample=Image.BILINEAR,
    )
    img = img.resize(
        (int(width ** uniform(0.89, 0.98)), int(height ** uniform(0.89, 0.98))),
        resample=Image.BICUBIC,
    )
    img = img.resize((width, height), resample=Image.BICUBIC)
    img = ImageOps.posterize(img, randint(3, 7))

    # Generate colour overlay
    overlay = img.split()[0]
    overlay = ImageEnhance.Contrast(overlay).enhance(uniform(1.0, 2.0))
    overlay = ImageEnhance.Brightness(overlay).enhance(uniform(1.0, 2.0))

    overlay = ImageOps.colorize(overlay, colours[0], colours[1])

    # Overlay red and yellow onto main image and sharpen the hell out of it
    img = Image.blend(img, overlay, uniform(0.1, 0.4))
    img = ImageEnhance.Sharpness(img).enhance(randint(5, 300))

    return img


CMD_HELP.update(
    {
        "deepfry": f"**Plugin : **`deepfry`\
        \n\n  •  **Syntax :** `{cmd}deepfry` atau `.deepfry` [level(1-8)]\
        \n  •  **Function : **Deepfry foto atau sticker dari bot @image_deepfrybot.\
        \n\n  •  **Syntax :** `{cmd}deepfry` [level(1-5)]\
        \n  •  **Function : **Deepfry foto atau sticker.\
    "
    }
)

# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
from geopy.geocoders import Nominatim
from telethon.tl import types

from ft import CMD_HANDLER as cmd
from ft import CMD_HELP
from ft.utils import edit_or_reply, man_cmd


@man_cmd(pattern="gps(?: |$)(.*)")
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await event.edit("**Berikan Tempat Yang ingin Dicari**")
    xx = await edit_or_reply(event, "`Processing...`")
    geolocator = Nominatim(user_agent="Man")
    geoloc = geolocator.geocode(input_str)
    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.edit(
            input_str, file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon))
        )
        await xx.delete()
    else:
        await xx.edit("`Maaf Saya Tidak Dapat Menemukannya`")


CMD_HELP.update(
    {
        "gps": f"**Plugin : **`gps`\
        \n\n  •  **Syntax :** `{cmd}gps` <nama lokasi>\
        \n  •  **Function : **Untuk Mendapatkan Lokasi Map.\
    "
    }
)

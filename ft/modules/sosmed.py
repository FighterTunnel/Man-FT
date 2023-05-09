# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.messages import DeleteHistoryRequest

from ft import CMD_HANDLER as cmd
from ft import CMD_HELP
from ft.utils import edit_delete, edit_or_reply, man_cmd


@man_cmd(pattern="sosmed(?: |$)(.*)")
async def insta(event):
    xxnx = event.pattern_match.group(1)
    if xxnx:
        link = xxnx
    elif event.is_reply:
        link = await event.get_reply_message()
    else:
        return await edit_delete(
            event,
            "**Berikan Link Sosmed atau Reply Link Sosmed Untuk di Download**",
        )
    xx = await edit_or_reply(event, "`Processing Download...`")
    chat = "@SaveAsbot"
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, link)
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await event.client.send_message(chat, link)
            response = await response
        if response.text.startswith("Forward"):
            await xx.edit("Forward Private .")
        else:
            await xx.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await event.client(DeleteHistoryRequest(peer=chat, max_id=0))
            await xx.delete()


@man_cmd(pattern="dez(?: |$)(.*)")
async def DeezLoader(event):
    if event.fwd_from:
        return
    dlink = event.pattern_match.group(1)
    if ".com" not in dlink:
        await edit_delete(
            event, "`Mohon Berikan Link Deezloader yang ingin di download`"
        )
    else:
        await edit_or_reply(event, "`Sedang Mendownload Lagu...`")
    chat = "@DeezLoadBot"
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.get_response()
            await conv.send_message(dlink)
            details = await conv.get_response()
            song = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.get_response()
            await conv.send_message(dlink)
            details = await conv.get_response()
            song = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_file(event.chat_id, song, caption=details.text)
        await event.delete()


@man_cmd(pattern="tiktok(?: |$)(.*)")
async def _(event):
    xxnx = event.pattern_match.group(1)
    if xxnx:
        d_link = xxnx
    elif event.is_reply:
        d_link = await event.get_reply_message()
    else:
        return await edit_delete(
            event,
            "**Berikan Link Tiktok Pesan atau Reply Link Tiktok Untuk di Download**",
        )
    xx = await edit_or_reply(event, "`Video Sedang Diproses...`")
    chat = "@thisvidbot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            video = await conv.get_response()
            text = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            video = await conv.get_response()
            text = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_file(event.chat_id, video)
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, r.id, msg.id, details.id, video.id, text.id]
        )
        await xx.delete()


CMD_HELP.update(
    {
        "sosmed": f"**Plugin : **`sosmed`\
        \n\n  •  **Syntax :** `{cmd}sosmed` <link>\
        \n  •  **Function : **Download Media Dari Pinterest / Tiktok / Instagram.\
        \n\n  •  **Syntax :** `{cmd}dez` <link>\
        \n  •  **Function : **Download Lagu Via Deezloader\
    "
    }
)


CMD_HELP.update(
    {
        "tiktok": f"**Plugin : **`tiktok`\
        \n\n  •  **Syntax :** `{cmd}tiktok` <link>\
        \n  •  **Function : **Download Video Tiktok Tanpa Watermark\
    "
    }
)

# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from ft import CMD_HANDLER as cmd
from ft import CMD_HELP
from ft.utils import edit_delete, edit_or_reply, man_cmd


@man_cmd(pattern="logo(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await edit_delete(event, "**Silahkan Masukan Text Untuk Logo**")
    else:
        await edit_or_reply(event, "`Processing...`")
    chat = "@tdtapibot"
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(f"/logo {text}")
            response = await conv.get_response()
            logo = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            msg = await conv.send_message(f"/logo {text}")
            response = await conv.get_response()
            logo = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            logo,
            caption=f"Logo by [{aing.first_name}](tg://user?id={aing.id})",
        )
        await event.client.delete_messages(conv.chat_id, [msg.id, response.id, logo.id])
        await event.delete()


CMD_HELP.update(
    {
        "logo": f"**Plugin : **`logo`\
        \n\n  •  **Syntax :** `{cmd}logo` <text>\
        \n  •  **Function : **Membuat logo dari Teks yang diberikan\
    "
    }
)

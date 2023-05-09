# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

import os
from pathlib import Path

from ft import CMD_HELP
from ft.utils import edit_or_reply, load_module, man_cmd, remove_plugin, reply_id


@man_cmd(pattern="install$")
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            xx = await edit_or_reply(event, "`Installing Modules...`")
            downloaded_file_name = await event.client.download_media(
                await event.get_reply_message(),
                "ft/modules/",
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await xx.edit(
                    f"**Plugin** `{os.path.basename(downloaded_file_name)}` **Berhasil di install**"
                )

            else:
                os.remove(downloaded_file_name)
                await xx.edit("**Error!** Plugin ini sudah terinstall di ft.")
        except Exception as e:
            await xx.edit(str(e))
            os.remove(downloaded_file_name)


@man_cmd(pattern="psend ([\s\S]*)")
async def send(event):
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    the_plugin_file = f"./ft/modules/{input_str}.py"
    if os.path.exists(the_plugin_file):
        await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            thumb="ft/resources/logo.jpg",
            allow_cache=False,
            reply_to=reply_to_id,
            caption=f"➠ **Nama Plugin:** `{input_str}`",
        )
        await event.delete()
    else:
        await edit_or_reply(event, "**ERROR: Modules Tidak ditemukan**")


@man_cmd(pattern="uninstall (?P<shortname>\w+)")
async def uninstall(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    dir_path = f"./ft/modules/{shortname}.py"
    xx = await edit_or_reply(event, "`Processing...`")
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await xx.edit(f"**Berhasil Menghapus Modules** `{shortname}`")
    except OSError as e:
        await xx.edit(f"**ERROR:** `{dir_path}` : {e.strerror}")


CMD_HELP.update(
    {
        "core": "**Plugin : **`core`\
        \n\n  •  **Syntax :** `.install` <reply ke file module>\
        \n  •  **Function : **Untuk Menginstall module ft secara instan.\
        \n\n  •  **Syntax :** `.uninstall` <nama module>\
        \n  •  **Function : **Untuk Menguninstall / Menghapus module ft secara instan.\
        \n\n  •  **Syntax :** `.psend` <nama module>\
        \n  •  **Function : **Untuk Mengirim module ft secara instan.\
    "
    }
)

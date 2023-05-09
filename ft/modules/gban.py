# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#


from ft import DEVS, WHITELIST, blacklistman
from ft.events import register
from ft.utils import chataction, get_user_from_event, man_cmd


@chataction()
async def handler(tele):
    if not tele.user_joined and not tele.user_added:
        return
    try:
        from ft.modules.sql_helper.gmute_sql import is_gmuted

        guser = await tele.get_user()
        gmuted = is_gmuted(guser.id)
    except BaseException:
        return
    if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):
                chat = await tele.get_chat()
                admin = chat.admin_rights
                creator = chat.creator
                if admin or creator:
                    try:
                        await client.edit_permissions(
                            tele.chat_id, guser.id, view_messages=False
                        )
                        await tele.reply(
                            f"**Gbanned Spoted** \n"
                            f"**First Name :** [{guser.id}](tg://user?id={guser.id})\n"
                            f"**Action :** `Banned`"
                        )
                    except BaseException:
                        return


@man_cmd(pattern="gband(?: |$)(.*)")
@register(pattern=r"^\.cgband(?: |$)(.*)", sudo=True)
async def gben(ft):
    dc = ft
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if sender.id != me.id:
        dark = await dc.reply("`Gbanning...`")
    else:
        dark = await dc.edit("`Memproses Global Banned Jamet..`")
    await dark.edit("`Global Banned Akan Segera Aktif..`")
    a = b = 0
    if ft.is_private:
        user = ft.chat
        reason = ft.pattern_match.group(1)
    try:
        user, reason = await get_user_from_event(ft)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("**Gagal Global Banned :(**")
    if user:
        if user.id in DEVS:
            return await dark.edit("**Gagal Global Banned, dia adalah Pembuat Saya 🤪**")
        if user.id in WHITELIST:
            return await dark.edit(
                "**Gagal Global Banned, dia adalah admin @Sharingft 🤪**"
            )
        try:
            from ft.modules.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        testft = [
            d.entity.id
            for d in await ft.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testft:
            try:
                await ft.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await dark.edit(
                    r"\\**#GBanned_User**//"
                    f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})\n"
                    f"**User ID:** `{user.id}`\n"
                    f"**Action:** `Global Banned`"
                )
            except BaseException:
                b += 1
    else:
        await dark.edit("**Balas Ke Pesan Penggunanya Goblok**")
    try:
        if gmute(user.id) is False:
            return await dark.edit(
                "**#Already_GBanned**\n\nUser Already Exists in My Gban List.**"
            )

    except BaseException:
        pass
    return await dark.edit(
        r"\\**#GBanned_User**//"
        f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})\n"
        f"**User ID:** `{user.id}`\n"
        f"**Action:** `Global Banned by {me.first_name}`"
    )


@man_cmd(pattern=r"ungband(?: |$)(.*)")
@register(pattern=r"^\.cungband(?: |$)(.*)", sudo=True)
async def gunben(ft):
    dc = ft
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if sender.id != me.id:
        dark = await dc.reply("`Ungbanning...`")
    else:
        dark = await dc.edit("`Ungbanning....`")
    await dark.edit("`Membatalkan Perintah Global Banned`")
    a = b = 0
    if ft.is_private:
        user = ft.chat
        reason = ft.pattern_match.group(1)
    try:
        user, reason = await get_user_from_event(ft)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("**Gagal Ungbanned :(**")
    if user:
        if user.id in blacklistman:
            return await dark.edit(
                "**Gagal ungbanned, Karna dia ada di Blacklist Man**"
            )
        try:
            from ft.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        testft = [
            d.entity.id
            for d in await ft.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testft:
            try:
                await ft.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await dark.edit("`Membatalkan Global Banned...`")
            except BaseException:
                b += 1
    else:
        await dark.edit("`Balas Ke Pesan Penggunanya Goblok`")
    try:
        if ungmute(user.id) is False:
            return await dark.edit("**Error! Pengguna Sedang Tidak Di Global Banned.**")
    except BaseException:
        pass
    return await dark.edit(
        r"\\**#UnGbanned_User**//"
        f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})\n"
        f"**User ID:** `{user.id}`\n"
        f"**Action:** `UnGBanned by {me.first_name}`"
    )

# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

from covid import Covid

from ft import CMD_HANDLER as cmd
from ft import CMD_HELP
from ft.utils import edit_or_reply, man_cmd


@man_cmd(pattern="covid (.*)")
async def corona(event):
    xx = await edit_or_reply(event, "`Processing...`")
    country = event.pattern_match.group(1)
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text = f"`⚠️Confirmed   : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`☢️Active      : {country_data['active']}`\n"
        output_text += f"`🤕Critical    : {country_data['critical']}`\n"
        output_text += f"`😟New Deaths  : {country_data['new_deaths']}`\n\n"
        output_text += f"`⚰️Deaths      : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😔New Cases   : {country_data['new_cases']}`\n"
        output_text += f"`😇Recovered   : {country_data['recovered']}`\n"
        output_text += f"`🧪Total tests : {country_data['total_tests']}`\n\n"
        output_text += f"**Data provided by [Worldometer]**(https://www.worldometers.info/coronavirus/country/{country})"
    else:
        output_text = "No information yet about this country!"

    await xx.edit(f"**Corona Virus Info in {country}:**\n\n{output_text}")


@man_cmd(pattern="covid$")
async def coronaworld(event):
    xx = await edit_or_reply(event, "`Processing...`")
    country = "World"
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text = f"`⚠️Confirmed   : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`☢️Active      : {country_data['active']}`\n"
        output_text += f"`🤕Critical    : {country_data['critical']}`\n"
        output_text += f"`😟New Deaths  : {country_data['new_deaths']}`\n\n"
        output_text += f"`⚰️Deaths      : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😔New Cases   : {country_data['new_cases']}`\n"
        output_text += f"`😇Recovered   : {country_data['recovered']}`\n"
        output_text += "`🧪Total tests : N/A`\n\n"
        output_text += f"**Data provided by **[Worldometer](https://www.worldometers.info/coronavirus/country/{country})"
    else:
        output_text = "No information yet about this country!"

    await xx.edit(f"**Corona Virus Info in {country}:**\n\n{output_text}")


CMD_HELP.update(
    {
        "covid": f"**Plugin : **`covid`\
        \n\n  •  **Syntax :** `{cmd}covid`\
        \n  •  **Function : **Memberikan Informasi semua data COVID-19 dari semua negara.\
        \n\n  •  **Syntax :** `{cmd}covid` <nama negara>\
        \n  •  **Function : **Memberikan Informasi tentang data COVID-19 dari negara.\
    "
    }
)

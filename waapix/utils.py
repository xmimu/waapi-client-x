#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File:        utils.py
@Author:      lgx
@Contact:     1101588023@qq.com
@Time:        2024/01/30 13:30
@Description:
"""

import re
import json
import waapi


def get_functions():
    functions = []
    topics = []

    with waapi.WaapiClient() as client:
        result = client.call('ak.wwise.waapi.getFunctions')
        functions.append('# region Functions\n')
        for i in result['functions']:
            row = i.replace('.', '_') + f" = '{i}'\n"
            functions.append(row)
        functions.append('# endregion Functions\n\n')

        topics.append('# region Topics\n')
        result = client.call('ak.wwise.waapi.getTopics')
        for i in result['topics']:
            row = i.replace('.', '_') + f" = '{i}'\n"
            topics.append(row)
        topics.append('# endregion Topics\n')

    with open('constants/uri.py', 'w', encoding='utf-8') as f:
        f.writelines(functions + topics)


def get_commands():
    commands = []
    with waapi.WaapiClient() as client:
        result = client.call('ak.wwise.ui.commands.getCommands')
        for i in result['commands']:
            row = re.sub(r'[^\w]', '_', i).strip('_') + f" = '{i}'\n"
            commands.append(row)

    with open('constants/commands.py', 'w', encoding='utf-8') as f:
        f.writelines(commands)


def get_obj_types():
    w_obj_list = []
    with waapi.WaapiClient() as client:
        result = client.call('ak.wwise.core.object.getTypes')
        for i in result['return']:
            if i['type'] == 'WObject':
                name = i['name']
                row = name + f" = '{name}'\n"
                w_obj_list.append(row)

    with open('constants/object.py', 'w', encoding='utf-8') as f:
        f.writelines(w_obj_list)
    with open('constants/objects.json', 'w', encoding='utf-8') as f:
        text = json.dumps(result['return'], ensure_ascii=False, indent=2)
        f.write(text)


if __name__ == '__main__':
    # get_functions()
    # get_commands()
    get_obj_types()
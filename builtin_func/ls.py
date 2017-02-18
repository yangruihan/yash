#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
显示目录功能
"""

import os
from constants import *


def ls(args):
    """
    显示目录
    """
    file_list = os.listdir(os.getcwd())

    if '-A' in args:
        file_list.append('.')
        file_list.append('..')

    if '-a' not in args and '-A' not in args:
        file_list = list(filter(lambda x: not x.startswith('.'), file_list))

    for index, file in enumerate(file_list):
        if os.path.isdir(file):  # 如果是目录，则改变输出颜色并且添加/标识
            file_list[index] = CMD_COLOR_GREEN + file_list[index] + '/' + CMD_COLOR_DEFAULT
    file_list.sort()

    if '-l' in args:
        print('\n'.join(file_list))
    else:
        print('  '.join(file_list))

    return ShellStatus.RUN

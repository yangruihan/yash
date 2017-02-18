#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
常用命令
"""

import os
from constants import ShellStatus


def exit(args):
    """
    退出命令
    """
    return ShellStatus.STOP


def cd(args):
    """
    切换目录
    """
    try:
        os.chdir(args[0])
    except FileNotFoundError as _:
        print('系统找不到指定的路径。')

    return ShellStatus.RUN


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
        if os.path.isdir(file):
            file_list[index] += '/'

    file_list.sort()

    if '-l' in args:
        print('  '.join(file_list))
    else:
        print('  '.join(file_list))

    return ShellStatus.RUN

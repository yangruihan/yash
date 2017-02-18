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


def clear(args):
    """
    清空屏幕
    """
    os.system('cls')
    return ShellStatus.RUN

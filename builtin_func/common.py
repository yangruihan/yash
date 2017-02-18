#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
常用命令
"""

import os
from command import Command
from constants import *


def exit(cmd):
    """
    退出命令
    """
    return ShellStatus.STOP


def cd(cmd):
    """
    切换目录
    """
    try:
        os.chdir(cmd.cmd_args[0])
    except FileNotFoundError as _:
        print('系统找不到指定的路径。')

    return ShellStatus.RUN


def clear(cmd):
    """
    清空屏幕
    """
    os.system('cls')
    return ShellStatus.RUN


def echo(cmd):
    """
    输出用户的输入
    """
    print(cmd.raw_args)
    return ShellStatus.RUN

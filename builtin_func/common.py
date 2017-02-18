#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
常用命令
"""

import os
from constants import *
import fnmatch


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


def find(args):
    """
    查找方法
    """
    if len(args) <= 0:
        print('请输入要查询的文件名，并且可添加查找路径。')
        return ShellStatus.RUN
    elif len(args) == 1:
        file_name = args[0]
        path = os.getcwd()
    else:
        file_name = args[0]
        path = args[1]

    results = []

    try:
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, file_name):
                    results.append(os.path.join(root, CMD_COLOR_RED + name + CMD_COLOR_DEFAULT))
    except Exception as e:
        print(e)
        print('系统找不到指定的路径。')

    for res in results:
        print(res)

    return ShellStatus.RUN

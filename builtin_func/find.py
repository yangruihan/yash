#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
查找方法
"""

import os
import fnmatch
from builtin_func.builtin_func import BuiltinFunc
from constants import *


class FindFunc(BuiltinFunc):
    """
    查找方法
    """

    def __init__(self):
        BuiltinFunc.__init__(self, 'find')

    def execute(self, cmd):
        if len(cmd.cmd_args) <= 0:
            print('请输入要查询的文件名，并且可添加查找路径。')
            return ShellStatus.RUN
        elif len(cmd.cmd_args) == 1:
            file_name = cmd.cmd_args[0]
            path = os.getcwd()
        else:
            file_name = cmd.cmd_args[0]
            path = cmd.cmd_args[1]

        if not os.path.exists(path):
            print('查找路径错误。')
            return ShellStatus.RUN

        results = []

        try:
            for root, dirs, files in os.walk(path):
                for name in files:
                    if fnmatch.fnmatch(name, file_name):
                        results.append(os.path.join(
                            root, CMD_COLOR_RED + name + CMD_COLOR_DEFAULT))
        except Exception as e:
            print(e)
            print('系统找不到指定的路径。')

        for res in results:
            print(res)

        return ShellStatus.RUN

    def help(self):
        return '查找命令。'

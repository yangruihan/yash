#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
显示目录功能
"""

import os
from builtin_func.builtin_func import BuiltinFunc
from constants import *


class LsFunc(BuiltinFunc):
    """
    显示目录
    """

    def __init__(self):
        BuiltinFunc.__init__(self, 'ls')

    def execute(self, cmd):
        result = []

        if len(cmd.cmd_simple_args) > 0:
            for file in cmd.cmd_simple_args:
                if os.path.exists(file):
                    if os.path.isdir(file):
                        temp_s = file + ":\n" + \
                                 self._show_files_in_path(file, cmd) + '\n'
                        result.append(temp_s)
                    elif os.path.isfile(file):
                        result.append(file + '\n')
                else:
                    result.append(r"ls: 无法访问'" + file + r"': 没有该文件或目录。" + '\n')
        else:
            result.append(self._show_files_in_path(os.getcwd(), cmd) + '\n')

        print('\n'.join(result), end='')
        return ShellStatus.RUN

    def help(self):
        return '显示目录命令。'

    def _show_files_in_path(self, path, cmd):
        file_list = os.listdir(path)

        if 'A' in cmd.cmd_options:
            file_list.append('.')
            file_list.append('..')

        if 'a' not in cmd.cmd_options and 'A' not in cmd.cmd_options:
            file_list = list(filter(lambda x: not x.startswith('.'), file_list))

        for index, file in enumerate(file_list):
            if os.path.isdir(file):  # 如果是目录，则改变输出颜色并且添加/标识
                file_list[index] = CMD_COLOR_GREEN + \
                                   file_list[index] + '/' + CMD_COLOR_DEFAULT

        file_list.sort()

        if 'l' in cmd.cmd_options:
            return '\n'.join(file_list)
        else:
            return '  '.join(file_list)

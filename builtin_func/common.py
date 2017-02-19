#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
常用命令
"""

import os
from builtin_func.builtin_func import BuiltinFunc
from constants import *


class ExitFunc(BuiltinFunc):
    """
    退出命令
    """

    def __init__(self):
        BuiltinFunc.__init__(self, 'exit')

    def execute(self, cmd):
        return ShellStatus.STOP

    def help(self):
        return '退出 Yash 命令。'


class CdFunc(BuiltinFunc):
    """
    切换目录命令
    """

    def __init__(self):
        BuiltinFunc.__init__(self, 'cd')

    def execute(self, cmd):
        try:
            os.chdir(cmd.cmd_args[0])
            cmd.env['pwd'] = os.getcwd()
        except FileNotFoundError as _:
            print('系统找不到指定的路径。')

        return ShellStatus.RUN

    def help(self):
        return '切换目录命令。'


class ClearFunc(BuiltinFunc):
    """
    清空屏幕
    """

    def __init__(self):
        BuiltinFunc.__init__(self, 'clear')

    def execute(self, cmd):
        os.system('cls')
        return ShellStatus.RUN

    def help(self):
        return '清空屏幕命令。'


class EchoFunc(BuiltinFunc):
    """
    输出用户的输入
    """

    def __init__(self):
        BuiltinFunc.__init__(self, 'echo')

    def execute(self, cmd):
        print(cmd.raw_args)
        return ShellStatus.RUN

    def help(self):
        return '输出用户的输入命令。'


class HelpFunc(BuiltinFunc):
    """
    帮助命令
    """

    def __init__(self):
        BuiltinFunc.__init__(self, 'help')

    def execute(self, cmd):
        if len(cmd.cmd_simple_args) == 0:
            print('Builtin commands: ')
            for cmd_name in cmd.env['builtin_cmds'].keys():
                print('    %s' % cmd_name)
        else:
            result = []
            for cmd_name in cmd.cmd_simple_args:
                if cmd_name in cmd.env['builtin_cmds'].keys():
                    result.append(cmd_name + ": " + cmd.env['builtin_cmds'][cmd_name].help() + '\n')

            print('\n'.join(result), end='')

        return ShellStatus.RUN

    def help(self):
        return '帮助命令。'

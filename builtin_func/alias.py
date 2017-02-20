#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
别名功能
"""

from builtin_func.builtin_func import BuiltinFunc
from utils.file_helper import FileHelper
from constants import *


class AliasFunc(BuiltinFunc):
    """
    别名功能
    """

    def __init__(self):
        BuiltinFunc.__init__(self, 'alias')

    def execute(self, cmd):
        if len(cmd.cmd_simple_args) <= 1:
            print("alias: 命令参数个数错误")
            return ShellStatus.RUN

        cmd1 = cmd.cmd_simple_args[0]
        temp_cmd = cmd.raw_cmd[cmd.raw_cmd.index('alias') + len('alias'):].strip()
        cmd2 = temp_cmd[temp_cmd.index(cmd1) + len(cmd1):].strip()

        # 如果有 w 选项则将别名写入.yashrc
        if 'w' in cmd.cmd_options:
            content = '\nalias %s="%s"\n' % (cmd1, cmd2)
            FileHelper.write_file_from_string(cmd.env['runtime_config_file_name'], content, 'w+')

        cmd.env['alias'][cmd1] = cmd2

        return ShellStatus.RUN

    def help(self):
        return '别名功能命令'

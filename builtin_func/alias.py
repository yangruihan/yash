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
        if len(cmd.cmd_simple_args) <= 0 or len(cmd.cmd_simple_args) > 1:
            print("alias: 命令参数个数错误")
            return ShellStatus.RUN

        arg = cmd.cmd_simple_args[0].split('=')
        alias_cmd = arg[0]

        if '"' in cmd.raw_cmd:
            raw_cmd = cmd.raw_cmd[cmd.raw_cmd.index('"') + 1: cmd.raw_cmd.rfind('"')]
        else:
            raw_cmd = arg[1]

        # 如果有 w 选项则将别名写入.yashrc
        if 'w' in cmd.cmd_options:
            content = '\nalias %s="%s"\n' % (alias_cmd, raw_cmd)
            FileHelper.write_file_from_string(cmd.env['runtime_config_file_name'], content, 'w+')

        cmd.env['alias'][alias_cmd] = raw_cmd

        return ShellStatus.RUN

    def help(self):
        return '别名功能命令'

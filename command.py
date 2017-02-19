#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
命令类
"""

import shlex


class Command:
    """
    命令类
    """

    def __init__(self, cmd, ENV):
        self.raw_cmd = cmd.strip()  # 原始命令
        self.cmd_name = ''          # 命令名称
        self.cmd_args = []          # 命令参数
        self.cmd_raw_args = ''      # 命令原始参数
        self.cmd_options = []       # 命令选项
        self.cmd_simple_args = []   # 命令纯参数

        self.env = ENV              # 环境

        # 解析输入的命令
        self._parse()

    def _parse(self):
        """
        解析输入的命令
        """
        tokens = shlex.split(self.raw_cmd, posix=False)
        self.cmd_name = tokens[0].strip()
        self.cmd_args = tokens[1:]
        self.cmd_raw_args = self.raw_cmd.replace(self.cmd_name, '').lstrip()

        # 解析命令选项
        self._parse_options()

    def _parse_options(self):
        """
        解析命令选项
        """
        for arg in self.cmd_args:
            if arg[0] == '-':
                for option in arg[1:]:
                    self.cmd_options.append(option)
            else:
                self.cmd_simple_args.append(arg.strip())

    def __str__(self):
        s = 'Command:\n'
        s += '\traw cmd: ' + self.raw_cmd + '\n'
        s += '\tcmd name: ' + self.cmd_name + '\n'
        s += '\tcmd args: ' + str(self.cmd_args) + '\n'
        s += '\tcmd raw args: ' + self.cmd_raw_args + '\n'
        s += '\tcmd options: ' + str(self.cmd_options) + '\n'
        s += '\tcmd simple args: ' + str(self.cmd_simple_args) + '\n'
        return s

#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
命令类
"""

import shlex


class Command():
    """
    命令类
    """

    def __init__(self, cmd):
        self.raw_cmd = cmd          # 原始命令
        self.cmd_name = ''          # 命令名称
        self.cmd_args = []          # 命令参数
        self.cmd_raw_args = ''      # 命令原始参数
        self.cmd_options = []       # 命令选项
        self.cmd_simple_args = []   # 命令纯参数

        # 解析输入的命令
        self._parse()

    def _parse(self):
        """
        解析输入的命令
        """
        tokens = shlex.split(self.raw_cmd)
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
                self.cmd_simple_args.append(arg)

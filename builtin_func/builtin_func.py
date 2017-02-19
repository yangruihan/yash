#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
内置命令类
"""


class BuiltinFunc:
    """
    内置命令类
    """

    def __init__(self, name):
        self.name = name  # 命令名

    def execute(self, cmd):
        """
        执行方法
        """
        pass

    def help(self):
        """
        显示帮助
        """
        pass

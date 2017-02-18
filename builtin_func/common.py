#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
常用命令
"""

from constants import ShellStatus


def exit(*args):
    return ShellStatus.STOP

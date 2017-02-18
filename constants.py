#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
保存各种常量
"""

from enum import Enum


class ShellStatus(Enum):
    """
    Shell 状态
    """
    RUN = 0
    STOP = 1


CMD_PROMPT = '%s\n'

CMD_COLOR_RED = '\33[91m'
CMD_COLOR_GREEN = '\33[92m'
CMD_COLOR_DEFAULT = '\33[0m'

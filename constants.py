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


CMD_PROMPT_STYLE = '%s\n'  # 命令提示符样式

CMD_COLOR_RED = '\33[91m'  # 命令行红色
CMD_COLOR_GREEN = '\33[92m'  # 命令行绿色
CMD_COLOR_DEFAULT = '\33[0m'  # 命令行无样式

RUNTIME_CONFIG_FILE_NAME = '.yashrc'  # 运行时配置文件名
HISTORY_FILE_NAME = '.yash_history'  # 历史命令文件名

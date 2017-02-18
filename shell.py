#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Shell 入口
"""

import sys
import shlex
from command import Command
from builtin_func.common import *
from builtin_func.ls import *
from builtin_func.find import *


# HOME = os.getenv(key="HOME")
HOME = os.getcwd()  # HOME 路径
builtin_cmds = {}  # 内置命令
CMD_HISTORY = []  # 命令历史
history_file = None  # 命令历史文件


def init_runtime_config():
    """
    初始化运行时配置文件
    """
    runrc_path = os.path.join(HOME, RUNTIME_CONFIG_FILE_NAME)
    if not os.path.exists(runrc_path):
        f = open(runrc_path, 'w')
        f.close()


def init_history_file():
    """
    初始化历史命令文件
    """
    history_path = os.path.join(HOME, HISTORY_FILE_NAME)
    history_file = open(history_path, 'w+')


def register_builtin_cmd(name, func):
    """
    注册内置命令
    :param name: 命令名
    :param func: 处理方法
    """
    builtin_cmds[name] = func


def register_builtin_cmds():
    """
    注册内置命令
    """

    builtin_cmds.clear()

    register_builtin_cmd('exit', exit)  # 注册退出命令
    register_builtin_cmd('cd', cd)  # 注册切换目录命令
    register_builtin_cmd('ls', ls)  # 显示当前目录文件命令
    register_builtin_cmd('find', find)  # 查找文件


def show_cmd_prompt():
    """
    显示命令提示符
    """
    sys.stdout.write(CMD_PROMPT_STYLE % os.getcwd())
    sys.stdout.write('> ')
    sys.stdout.flush()


def get_input():
    """
    得到输入的命令
    :return: 输入的命令
    """
    return sys.stdin.readline()


def excute_cmd(cmd):
    """
    执行命令
    :param cmd 输入的命令
    :return: 执行结果
    """

    # 根据输入构造命令
    command = Command(cmd)

    # 如果是内置命令，则直接返回执行结果
    if command.cmd_name in builtin_cmds:
        return builtin_cmds[command.cmd_name](command)
    else:
        os.system(command.raw_cmd)
        return ShellStatus.RUN


def shell_init():
    """
    Shell 初始化
    """

    # 初始化运行时配置文件
    init_runtime_config()

    # 初始化历史命令文件
    init_history_file()

    # 注册内置命令
    register_builtin_cmds()


def shell_loop():
    """
    Shell 主循环
    """
    status = ShellStatus.RUN  # Shell 状态

    while status == ShellStatus.RUN:
        # 显示命令提示符
        show_cmd_prompt()

        # 读入命令
        cmd = get_input()

        # 记录输入的命令
        CMD_HISTORY.append(cmd.strip())

        # 执行命令
        status = ShellStatus(excute_cmd(cmd))

        print()


def main():
    # 初始化
    shell_init()

    # 主循环
    shell_loop()


if __name__ == '__main__':
    main()

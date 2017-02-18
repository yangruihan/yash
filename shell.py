#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Shell 入口
"""

import sys
import shlex
from builtin_func.common import *
from builtin_func.ls import *

builtin_cmds = {}  # 内置命令


def register_builtin_cmd(name, func):
    """
    注册内置命令
    :param name: 命令名
    :param func: 处理方法
    """
    builtin_cmds[name] = func


def show_cmd_prompt():
    """
    显示命令提示符
    """
    sys.stdout.write(CMD_PROMPT % os.getcwd())
    sys.stdout.write('> ')
    sys.stdout.flush()


def get_input():
    """
    得到输入的命令
    :return: 输入的命令
    """
    return sys.stdin.readline()


def parse_cmd(cmd):
    """
    解析输入的命令
    :param 命令字符串
    :return: cmd_name, cmd_args
        cmd_name: 命令名
        cmd_args：命令参数
    """
    tokens = shlex.split(cmd)
    return tokens[0], tokens[1:]


def excute_cmd(cmd):
    """
    执行命令
    :param cmd 输入的命令
    :return: 执行结果
    """

    # 解析命令名称和参数
    cmd_name, cmd_args = parse_cmd(cmd)

    # 如果是内置命令，则直接返回执行结果
    if cmd_name in builtin_cmds:
        return builtin_cmds[cmd_name](cmd_args)
    else:
        os.system(cmd)
        return ShellStatus.RUN


def shell_init():
    """
    Shell 初始化
    """
    builtin_cmds.clear()

    register_builtin_cmd('exit', exit)  # 注册退出命令
    register_builtin_cmd('cd', cd)  # 注册切换目录命令
    register_builtin_cmd('ls', ls)  # 显示当前目录文件命令


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

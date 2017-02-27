#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Shell 入口
"""

import sys
import shlex
from command import Command
from builtin_func.common import *
from builtin_func.ls import LsFunc
from builtin_func.find import FindFunc
from builtin_func.alias import AliasFunc
from utils.file_helper import FileHelper

ENV = {}  # 环境


def init_env():
    ENV['home'] = os.getcwd()  # HOME 路径
    ENV['builtin_cmds'] = {}  # 内置命令
    ENV['cmd_history'] = []  # 命令历史
    ENV['cmd_history_file'] = None  # 记录命令历史的文件
    ENV['pwd'] = os.getcwd()  # 当前路径
    ENV['alias'] = {}  # 命令别名
    ENV['runtime_config_file_name'] = RUNTIME_CONFIG_FILE_NAME  # 运行时配置文件名
    ENV['history_file_name'] = HISTORY_FILE_NAME  # 历史命令记录文件名


def init_runtime_config():
    """
    初始化运行时配置文件
    """
    runrc_path = os.path.join(ENV['home'], RUNTIME_CONFIG_FILE_NAME)
    if not os.path.exists(runrc_path):
        FileHelper.create_empty_file(runrc_path)


def init_history_file():
    """
    初始化历史命令文件
    """
    history_path = os.path.join(ENV['home'], HISTORY_FILE_NAME)
    history_file = open(history_path, 'w+')  # 命令历史文件

    ENV['cmd_history_file'] = history_file


def register_builtin_cmd(name, func):
    """
    注册内置命令
    :param name: 命令名
    :param func: 处理方法
    """
    ENV['builtin_cmds'][name] = func


def register_builtin_cmds():
    """
    注册内置命令
    """

    ENV['builtin_cmds'].clear()

    register_builtin_cmd('exit', ExitFunc())  # 注册退出命令
    register_builtin_cmd('cd', CdFunc())  # 注册切换目录命令
    register_builtin_cmd('clear', ClearFunc())  # 清空屏幕
    register_builtin_cmd('ls', LsFunc())  # 显示当前目录文件命令
    register_builtin_cmd('find', FindFunc())  # 查找文件
    register_builtin_cmd('help', HelpFunc())  # 帮助命令
    register_builtin_cmd('alias', AliasFunc())  # 别名命令


def show_cmd_prompt():
    """
    显示命令提示符
    """
    sys.stdout.write(CMD_PROMPT_STYLE % ENV['pwd'])
    sys.stdout.write('yash> ')
    sys.stdout.flush()


def get_input():
    """
    得到输入的命令
    :return: 输入的命令
    """
    return sys.stdin.readline()


def pre_handle_cmd(cmd):
    """
    命令预处理
    """
    # 进行别名替换
    op = shlex.split(cmd, posix=False)[0].strip()

    if op in list(ENV['alias'].keys()):
        cmd = cmd.replace(op, ENV['alias'][op])

    return cmd


def excute_cmd(cmd):
    """
    执行命令
    :param cmd 输入的命令
    :return: 执行结果
    """

    # 根据输入构造命令
    command = Command(cmd, ENV)

    # print(command)

    # 如果是内置命令，则直接返回执行结果
    if command.cmd_name in ENV['builtin_cmds']:
        return ENV['builtin_cmds'][command.cmd_name].execute(command)
    else:
        # 尝试用 python 解析
        try:
            eval(command.raw_cmd)
        except Exception as _:
            # 如果 python 解析失败，则尝试用系统内置命令执行
            os.system(command.raw_cmd)

        return ShellStatus.RUN


def shell_init():
    """
    Shell 初始化
    """
    # 初始化环境
    init_env()

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
        STDIN = get_input()

        # 记录输入的命令
        ENV['cmd_history'].append(STDIN.strip())

        # 命令预处理
        pre_cmd = pre_handle_cmd(STDIN)

        # 执行命令
        status = ShellStatus(excute_cmd(pre_cmd))

        print()


def main():
    # 初始化
    shell_init()

    # 主循环
    shell_loop()


if __name__ == '__main__':
    main()

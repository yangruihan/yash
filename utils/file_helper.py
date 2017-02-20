#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
文件操作帮助
"""

import os
from constants import *


class FileHelper:
    """
    文件操作帮助类
    """

    @staticmethod
    def read_from_file_to_list(filename):
        file_content = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                file_content = f.readlines()
        else:
            if DEBUG:
                print("FileHelper.read_from_file_to_list error: 没有这个文件")

        return file_content

    @staticmethod
    def write_file_from_list(filename, file_list, mode='w'):
        if isinstance(file_list, list):
            with open(filename, mode) as f:
                f.write('\n'.join(file_list))
        else:
            if DEBUG:
                print("FileHelper.write_file_from_list error: 传入参数不为list")

    @staticmethod
    def create_empty_file(filename):
        if not os.path.exists(filename):
            f = open(filename, 'w')
            f.close()
        else:
            if DEBUG:
                print("FileHelper.create_empty_file error: 该文件已存在")

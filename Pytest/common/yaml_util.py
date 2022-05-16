# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：yaml_util.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/11 17:10
"""
import os

import yaml


# 获取项目的根目录
def get_obj_path():
    return os.path.dirname(__file__).split('common')[0]


# 读取yaml
def read_yaml(yaml_path):
    with open(get_obj_path() + yaml_path, mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value

#
# if __name__ == '__main__':
#     print(read_yaml('testcases/user_manage/get_token.yaml'))

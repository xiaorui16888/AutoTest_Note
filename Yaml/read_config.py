# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：read_config.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/15 13:14
"""
import yaml


class ReadConfig:
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def read_yaml(self):
        with open(self.yaml_file, encoding='utf-8') as f:
            file_dict = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
            print(file_dict)

    def write_yaml(self, data):
        with open(self.yaml_file, encoding='utf-8', mode='w') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)


if __name__ == '__main__':
    # rc = ReadConfig('config.yaml')
    # rc.read_yaml()
    # rc.write_yaml({'User': {'name': '小睿', 'age': 24}})

    api_config = ReadConfig('api.yaml')
    api_config.read_yaml()

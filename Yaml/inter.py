# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：inter.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/15 13:31
"""
import json
import unittest

import requests
from ddt import ddt, file_data


@ddt
class Inter(unittest.TestCase):
    @file_data('api.yaml')
    def test_01_get_token(self, **kwargs):
        print(kwargs)
        url = kwargs['request']['url']
        params = kwargs['request']['params']
        headers = kwargs['request']['headers']
        resp = requests.get(url, params=params, headers=headers)
        print(resp.text)
        result_dict = json.loads(resp.text)
        # 预期结果
        # 'assert': {'eq': {'expires_in': 7200}}
        self.assertEqual(kwargs['assert']['eq']['expires_in'], result_dict['expires_in'])


if __name__ == '__main__':
    unittest.main()

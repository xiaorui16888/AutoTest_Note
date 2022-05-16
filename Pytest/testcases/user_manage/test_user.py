# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：test_user.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/11 17:07
"""
import json

import pytest

from Pytest.common.requests_util import send_request
from Pytest.common.yaml_util import read_yaml


class TestUser:
    access_token = ""

    @pytest.mark.smoke
    def test_user(self):
        print('test_user')

    @pytest.mark.weixin
    @pytest.mark.parametrize('caseInfo', read_yaml('testcases/user_manage/get_token.yaml'))
    def test_01_get_token(self, caseInfo):
        print('获取统一接口鉴权码：', caseInfo)
        method = caseInfo['request']['method']
        url = caseInfo['request']['url']
        data = caseInfo['request']['data']
        resp = send_request(method=method, url=url, data=data)
        result = resp.json()
        print(result)
        TestUser.access_token = result['access_token']
        assert 'access_token' in result

    @pytest.mark.weixin
    @pytest.mark.parametrize('caseInfo', read_yaml('testcases/user_manage/edit_menu.yaml'))
    def test_03_edit_menu(self, caseInfo):
        print('编辑菜单接口：', caseInfo)
        method = caseInfo['request']['method']
        url = caseInfo['request']['url'] + TestUser.access_token
        data = caseInfo['request']['data']
        resp = send_request(method=method, url=url,
                            data=json.dumps(data, ensure_ascii=False).encode('utf-8'))
        result = resp.json()
        print(result)


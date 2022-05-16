# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：requests_util.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/12 14:57
"""
import requests


class RequestUtil:
    session = requests.session()


def send_request(method, url, data, **kwargs):
    method = str(method).lower()
    resp = ''
    if method == 'get':
        resp = RequestUtil.session.request(method, url, params=data, **kwargs)
    elif method == 'post':
        resp = RequestUtil.session.request(method, url, data=data, **kwargs)
    return resp

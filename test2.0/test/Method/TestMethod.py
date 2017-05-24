#coding = utf-8

"""
Author:Monica
"""
import requests
import json


class TestApi:
    def __init__(self, method, url, data, file=None, cookie=None):
        self.method = method
        self.url = url
        self.data = data
        self.file = file
        self.cookie = cookie
        self.query = None

    @property
    def test_api(self):
        try:
            if self.query:
                return self.query
            r = None
            url = self.url
            data = json.loads(self.data)
            if self.method == 'post':
                r = requests.post(url=url, json=data, cookies=self.cookie)
            elif self.method == 'get':
                r = requests.get(url=url, params=data, cookies=self.cookie)
            elif self.method == 'put':
                r = requests.put(url=url, json=data, cookies=self.cookie)
            elif self.method == 'delete':
                r = requests.delete(url=url, json=data, cookies=self.cookie)
            elif self.method == 'multipart/form-data':
                r = requests.post(url=url, data=data, files=self.file, cookies=self.cookie)
            self.query = r
            return r
        except Exception as e:
            print(e.args)
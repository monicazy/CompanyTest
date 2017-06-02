# coding = utf-8

import requests
import configparser
import os

config = configparser.ConfigParser()
basedir = os.path.abspath(os.path.dirname(__file__))
static_file_path = os.path.join(basedir, 'config.ini')
config.read(static_file_path)
cookieUrl = config.get('url', 'cookieUrl')
data = config.get('data', 'data')
r = requests.post(url=cookieUrl,data=data)
cookie = requests.post(url=cookieUrl, data=data).cookies
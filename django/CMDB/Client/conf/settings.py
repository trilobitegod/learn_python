# -*- coding:utf-8 -*-

import os


Params = {
    'server': '192.168.43.40',
    'port': '8000',
    'url': '/assets/report/',
    'request_timeout': 30,
}

PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmdb.log')
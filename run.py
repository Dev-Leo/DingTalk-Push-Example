# -*- coding: utf-8 -*-
#!/usr/bin/python3

import requests
import json

def message():
    test="success"
    message="花生酱"+test
    return message

def run():
    post_url = "你的API地址"
    msg= message()
    headers = {'Content-Type': 'application/json'}
    data =  {
    "msgtype": "text",
     "text": {
         "content":msg
    }
    }
    requests.post(post_url, data=json.dumps(data), headers=headers)

run()

import time

import requests

url = 'http://localhost'
name = '2b'

session = requests.Session()
resp = session.post(url, data={'driver': name, 'steering_control': '0', 'throttle': '0'})
hint = resp.text

for i in range(10):
    time.sleep(0)
    t = time.time()
    if '弯道向左' in hint:
        ctrl = '-1'
    elif '弯道向右' in hint:
        ctrl = '1'
    else:
        ctrl = '0'

    if '抓地力太小了' in hint:
        gas = '0'
    elif '抓地力太大了' in hint:
        gas = '2'
    else:
        gas = '1'
    print(str(t - time.time()))
    print(str(ctrl), str(gas))

    t = time.time()
    resp = session.post(url, data={'driver': name, 'steering_control': ctrl, 'throttle': gas})
    hint = resp.text

    print(str(t - time.time()))
    print(any(x in hint for x in ['太慢了', '失误了']))

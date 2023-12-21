import sys
import json
import requests

msg = sys.stdin.readline()
msg_array = msg.split(',')
url_log = 'http://192.168.50.168:25926/inference'
json_inputs = json.dumps({'input': [msg_array[0], msg_array[1], msg_array[2], msg_array[3], msg_array[4],
                                    msg_array[5], msg_array[6]]})
response = requests.post(url_log, json=json_inputs)
if response.json().index(max(response.json())) == 0:
    print(0)
else:
    print(1)
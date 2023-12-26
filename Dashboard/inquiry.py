import sys
import json
import requests

msg = sys.stdin.readline()
msg_array = msg.split(',')
url_log = 'http://192.168.50.168:25926/inference_1'
json_inputs = json.dumps({'input': [int(msg_array[0]), int(msg_array[1]), int(msg_array[2]), int(msg_array[3]),
                                    float(msg_array[4]), float(msg_array[5])]})
try:
    response = requests.post(url_log, json=json_inputs)
    if response.json().index(max(response.json())) == 0:
        print(0)
    else:
        print(1)

except:
    print(-1)
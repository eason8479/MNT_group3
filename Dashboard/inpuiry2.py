import sys
import json
import requests

msg = sys.stdin.readline()
msg_array = msg.split(',')
url_log = 'http://192.168.50.168:25926/inference_2'
json_inputs = json.dumps({'input': [float(msg_array[0]), float(msg_array[1]), float(msg_array[2]),
                                    float(msg_array[3])]})
try:
    response = requests.post(url_log, json=json_inputs)
    if response.json().index(max(response.json())) == 0:
        print(True)
    else:
        print(False)

except:
    print(-1)
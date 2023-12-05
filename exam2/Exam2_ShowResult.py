#create Flask Client
import requests
import time
import mpu6050
import json

url_log = 'http://192.168.50.168:25926/inference'
mpu = mpu6050(0x68)

try:
    while(True) :
        time.sleep(1)
        accel_data = mpu.get_accel_data()
        gyro_data = mpu.get_gyro_data()
        json_inputs = json.dumps({ 'input':[accel_data['x'], accel_data['y'], accel_data['z'], gyro_data['x'], gyro_data['y'], gyro_data['z']]})
        response = requests.post(url_log, json = json_inputs)
        if response.json().index(max(response.json())) == 0:
            print("System is Functioning Properly")
        else:
            print("SYSTEM IS VIBRATING!!!")
finally:
    print("System Shutdown")
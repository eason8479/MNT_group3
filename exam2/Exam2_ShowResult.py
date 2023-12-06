#create Flask Client
import requests
import time
from mpu6050 import *
import json
import Jetson.GPIO as GPIO

url_log = 'http://192.168.50.168:25926/inference'
mpu = mpu6050(0x68)
count=0
t=0
pre=0

# set mode (BOARD/BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# sensor out
input_pin = 18
GPIO.setup(input_pin, GPIO.IN)

input_pin2 = 6
GPIO.setup(input_pin2, GPIO.OUT)
try:
    while(True) :
        time.sleep(0.002)
        t=t+1
        s = GPIO.input(input_pin)
        if pre!=s:
            count=count+1
        pre=s
        if t ==1000:
            t=0
            accel_data = mpu.get_accel_data()
            gyro_data = mpu.get_gyro_data()
            json_inputs = json.dumps({ 'input':[accel_data['x'], accel_data['y'], accel_data['z'], gyro_data['x'], gyro_data['y'], gyro_data['z'],count/40]})
            count=0
            response = requests.post(url_log, json = json_inputs)
            print(response.json())
            if response.json().index(max(response.json())) == 0:
                print("System is Functioning Properly\n")
                GPIO.output(input_pin2,GPIO.LOW)
            else:
                print("\nSYSTEM IS VIBRATING!!!\n")
                GPIO.output(input_pin2,GPIO.HIGH)
finally:
    print("System Shutdown")
import sys
sys.path.insert(0, "..")
import time
from mpu6050 import mpu6050
from mlx90614 import MLX90614
import json
import requests
import Jetson.GPIO as GPIO

from opcua import ua, Server

def showResult():
    json_inputs = json.dumps({'input': [angle_data['x'], angle_data['y'], nozzle_data, plate_data]})
    response = requests.post(url_log, json=json_inputs)
    if response.json().index(max(response.json())) == 0:
        GPIO.output(output_pin, GPIO.LOW)
        predict_data.set_value(True)
    else:
        GPIO.output(output_pin, GPIO.HIGH)
        predict_data.set_value(False)

if __name__ == "__main__":

    url_log = 'http://192.168.50.168:25926/inference_2'

    # set mode (BOARD/BCM)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # sensor out
    output_pin = 18
    GPIO.setup(output_pin, GPIO.OUT)

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/Team3/")

    # setup our own namespace, not really necessary but should as spec
    uri = "https://ncueeclass.ncu.edu.tw/course/23174"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj_angle = objects.add_object(idx, "angle")
    angle_x = myobj_angle.add_variable(idx, "angle_x", 0.1)
    angle_y = myobj_angle.add_variable(idx, "angle_y", 0.1)
    myobj_temp = objects.add_object(idx, "temp")
    nozzle_temp = myobj_temp.add_variable(idx, "nozzle_temp", 0.1)
    plate_temp = myobj_temp.add_variable(idx, "plate_temp", 0.1)
    myobj_predict = objects.add_object(idx, "predict")
    predict_data = myobj_predict.add_variable(idx, "isSuccessfully", True)
    angle_x.set_writable()
    angle_y.set_writable()
    nozzle_temp.set_writable()
    plate_temp.set_writable()
    predict_data.set_writable()

    # starting!
    server.start()

    try:
        mpu = mpu6050(0x68)
        sensor = MLX90614(1, address=0x5A)
        plateSensor = MLX90614(0, address=0x5A)
        sensor.linear_adjustment(215, 15)
        plateSensor.linear_adjustment(215, 15)
        while (True):
            time.sleep(2)
            angle_data = mpu.get_angle_data()
            nozzle_data = sensor.get_obj_temp()
            plate_data = plateSensor.get_obj_temp()
            angle_x.set_value(angle_data['x'])
            angle_y.set_value(angle_data['y'])
            nozzle_temp.set_value(nozzle_data)
            plate_temp.set_value(plate_data)
            showResult()

    finally:
        # close connection, remove subcsriptions, etc
        server.stop()
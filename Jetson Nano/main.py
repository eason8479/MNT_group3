import sys
sys.path.insert(0, "..")
import time
from mpu6050 import mpu6050
from mlx90614 import MLX90614

from opcua import ua, Server

if __name__ == "__main__":

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
    angle_x.set_writable()
    angle_y.set_writable()
    nozzle_temp.set_writable()
    plate_temp.set_writable()

    # starting!
    server.start()

    try:
        mpu = mpu6050(0x68)
        sensor = MLX90614(1, address=0x5A)
        plateSensor = MLX90614(0, address=0x5A)
        sensor.linear_adjustment(215, 215)
        plateSensor.linear_adjustment(70, 70)
        while (True):
            time.sleep(2)
            angle_data = mpu.get_angle_data()
            angle_x.set_value(angle_data['x'])
            angle_y.set_value(angle_data['y'])
            nozzle_temp.set_value(sensor.get_obj_temp())
            plate_temp.set_value(plateSensor.get_obj_temp())

    finally:
        # close connection, remove subcsriptions, etc
        server.stop()
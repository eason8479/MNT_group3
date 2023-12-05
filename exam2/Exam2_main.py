import sys
sys.path.insert(0, "..")
import time
import mpu6050

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
    myobj_accel = objects.add_object(idx, "accel")
    accel_x = myobj_accel.add_variable(idx, "accel_x", 0.1)
    accel_y = myobj_accel.add_variable(idx, "accel_y", 0.1)
    accel_z = myobj_accel.add_variable(idx, "accel_z", 0.1)
    myobj_gyro = objects.add_object(idx, "gyro")
    gyro_x = myobj_gyro.add_variable(idx, "gyro_x", 0.1)
    gyro_y = myobj_gyro.add_variable(idx, "gyro_y", 0.1)
    gyro_z = myobj_gyro.add_variable(idx, "gyro_z", 0.1)
    accel_x.set_writable()
    accel_y.set_writable()
    accel_z.set_writable()
    gyro_x.set_writable()
    gyro_y.set_writable()
    gyro_z.set_writable()

    # starting!
    server.start()

    try:
        mpu = mpu6050(0x68)
        while (True):
            time.sleep(1)
            accel_data = mpu.get_accel_data()
            gyro_data = mpu.get_gyro_data()
            accel_x.set_value(accel_data['x'])
            accel_y.set_value(accel_data['y'])
            accel_z.set_value(accel_data['z'])
            gyro_x.set_value(gyro_data['x'])
            gyro_y.set_value(gyro_data['y'])
            gyro_z.set_value(gyro_data['z'])

    finally:
        # close connection, remove subcsriptions, etc
        server.stop()
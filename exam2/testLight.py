import Jetson.GPIO as GPIO
import time
# set mode (BOARD/BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

    # sensor out
input_pin = 6
GPIO.setup(input_pin, GPIO.OUT)
while True:
    GPIO.output(input_pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(input_pin,GPIO.LOW)
    time.sleep(1)
    print("ing")

import RPi.GPIO as GPIO
import time
import random
import Adafruit_BMP.BMP085 as BMP085
from bmp_internal import Internal_BMPS;


sensor = None
switch_bmp = True
enabled = True
relative_height = False
temperature = 0
average_altitude = 0
average_pressure = 0
starting_altitude = 0

"""""
def LEFT_SELECT():
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(25,GPIO.LOW)


def RIGHT_SELECT():
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(25,GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT) 
GPIO.setup(25, GPIO.OUT)
sensor = BMP085.BMP085()
"""""

sensor = Internal_BMPS()



while(True):
    sensor.run_sensors()
    print(sensor.average_altitude)
    time.sleep(1)
        #GPIO.cleanup()
    



        

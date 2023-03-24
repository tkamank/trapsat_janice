import RPi.GPIO as GPIO
import time
import random
import Adafruit_BMP.BMP085 as BMP085


def LEFT_SELECT():
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(22,GPIO.LOW)


def RIGHT_SELECT():
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(22,GPIO.LOW)


def toggle_bmp():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT) 
    GPIO.setup(22, GPIO.OUT)

    sensor = BMP085.BMP085()
    switch_bmp = True
    while(1):
        if(switch_bmp):
            LEFT_SELECT
        else:
            RIGHT_SELECT
        print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
        print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
        print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
        print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))
        time.sleep(1)
        switch_bmp = not switch_bmp
    GPIO.cleanup()
 

#Init XCLR pins 
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) 
GPIO.setup(22, GPIO.OUT)


#Establish baseline by subtracting (current - inital).

#Turn one BMP off and the other on
LEFT_SELECT
sensor = BMP085.BMP085()

#Can be used to capture inital values.
print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))
time.sleep(1)
RIGHT_SELECT
#Alternate signals. Alternating the power output in this way allows for two BMP sensors to use the I2C line.


print('\n')
print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))
GPIO.cleanup()


        

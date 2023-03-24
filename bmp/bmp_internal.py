import RPi.GPIO as GPIO
import time
import random
import Adafruit_BMP.BMP085 as BMP085


class Internal_BMPS:
    sensor = None
    switch_bmp = True
    enabled = True
    temperature = 0
    average_altitude = 0
    average_pressure = 0
    def __init__(self):
        self.sensor = BMP085.BMP085()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(18, GPIO.OUT) 
        GPIO.setup(22, GPIO.OUT)

    def LEFT_SELECT():
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(22,GPIO.LOW)


    def RIGHT_SELECT():
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(22,GPIO.LOW)

    def run_sensors(self):
        while(self.enabled):
            if(switch_bmp):
                self.LEFT_SELECT()
            else:
                self.RIGHT_SELECT()
            self.temperature = self.sensor.read_temperature()
            self.average_pressure = self.sensor.read_pressure()
            self.average_altitude = self.sensor.read_altitude()
            #print('Temp = {0:0.2f} *C'.format(self.sensor.read_temperature()))
            #print('Pressure = {0:0.2f} Pa'.format(self.sensor.read_pressure()))
            #print('Altitude = {0:0.2f} m'.format(self.sensor.read_altitude()))
            #print('Sealevel Pressure = {0:0.2f} Pa'.format(self.sensor.read_sealevel_pressure()))
            time.sleep(1)
            switch_bmp = not switch_bmp
        GPIO.cleanup()
    



        

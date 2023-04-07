import RPi.GPIO as GPIO
import time
import random
import Adafruit_BMP.BMP085 as BMP085


class Single_BMP:
    sensor = None
    switch_bmp = True
    enabled = True
    relative_height = False
    temperature = 0
    average_altitude = 0
    average_pressure = 0
    starting_altitude = 0



    def __init__(self):
        #One sensor must be de-selected, else code throws an I/O trying to read both devices
        self.sensor = BMP085.BMP085()
        

    def captureStartingHeight(self):
        self.starting_altitude = self.sensor.read_altitude()
        self.switch_bmp = not self.switch_bmp
        

    def run_sensors(self):
        if(self.relative_height):
            self.temperature = self.sensor.read_temperature()
            self.average_pressure = self.sensor.read_pressure()
            self.average_altitude = self.sensor.read_altitude() - self.starting_altitude
        else:
            self.temperature = self.sensor.read_temperature()
            self.average_pressure = self.sensor.read_pressure()
            self.average_altitude = self.sensor.read_altitude()
        self.switch_bmp = not self.switch_bmp
        #GPIO.cleanup()
    



        

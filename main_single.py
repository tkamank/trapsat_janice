import time
import shutil
from random import *
from datetime import datetime;
from servo.servo_internal import Internal_Servo;
from Camera.camera_internal import Internal_Camera;
from bmp.bmp_internal import Internal_BMPS;
from single_bmp.singleBMP import Single_BMP;
from csv_printing.csv_file import write_csv_data;

#Written by Tariq Amankwah and Charis Houston

#run sudo pigpiod to start pigpiod in terminal
#BMPs need to be initialized before running main.py, run bmp_toggle first

#Capture current filesystem disk size
file_path = "/home/trapsat/Desktop/Janus_Photos"
free_space = shutil.disk_usage(file_path).free

min_space = 20523622912
servo1 = Internal_Servo()
camera1 = Internal_Camera()
#bmp1 = Internal_BMPS()
bmp_single = Single_BMP()

door_opened = False
monitor_value = True

# These values will need to change to meters 15240m and 16764m
door_open_height = 15240
door_close_height = 16764

#test for servo height at meters 
#door_open_height = 14 
#door_close_height = 16

#Capture current time
previous_time = int(datetime.now().strftime("%Y%m%d%H%M%S"))

#Enable relative_height setting: Captures first altitude reading as baseline
#Open at 50,000 close at 55,000
#pass pulse width, NOT angle!
bmp_single.relative_height = False
bmp_single.captureStartingHeight()
#Data file vars
file_prefix = "sensor_data"
file_timestamp = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
file_extension = ".txt"
file_title = "sensor_data{}.csv"
#Create file
write_csv_data("/home/trapsat/Desktop/Janus_Data/" + file_title.format(file_timestamp), ['Timestamp','Temperature (C)','Pressure (Pa)','Altitude (m)'])
#Set door closed
servo1.setAngle(500)
while(bmp_single.enabled and free_space > min_space):
    free_space = shutil.disk_usage(file_path).free
    current_time = int(datetime.now().strftime("%Y%m%d%H%M%S"))
    if(monitor_value == True):
        if ((bmp_single.average_altitude >= door_open_height) and (door_opened == False)):
            print("Target Value Reached, opening door")
            servo1.setAngle(1500)
            door_opened = True
        elif((bmp_single.average_altitude >= door_open_height and bmp_single.average_altitude <= door_close_height) and door_opened == True):
            if(abs(current_time - previous_time) >= 900):
                print('Taking picture...')
                camera1.take_picture()
                previous_time = int(datetime.now().strftime("%Y%m%d%H%M%S"))
        elif ((bmp_single.average_altitude >= door_close_height) and door_opened == True):
            print('Height limit exceeded, closing door.')
            servo1.setAngle(500)
            servo1.close()
            monitor_value = False
    
    bmp_single.run_sensors()
    print('Temp = {0:0.2f} *C'.format(bmp_single.temperature))
    print('Pressure = {0:0.2f} Pa'.format(bmp_single.average_pressure))
    print('Altitude = {0:0.2f} m'.format(abs(bmp_single.average_altitude)))
    write_csv_data(file_title.format(file_timestamp), [datetime.now(), bmp_single.temperature, bmp_single.average_pressure,bmp_single.average_altitude])
    print('Assigned to CSV')
    time.sleep(3)

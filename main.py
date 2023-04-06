import time
import shutil
from random import *
from datetime import datetime;
from servo.servo_internal import Internal_Servo;
from Camera.camera_internal import Internal_Camera;
from bmp.bmp_internal import Internal_BMPS;
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
bmp1 = Internal_BMPS()

door_opened = False
monitor_value = True
door_open_height = 50000
door_close_height = 55000
#Enable relative_height setting: Captures first altitude reading as baseline
#Open at 50,000 close at 55,000
#pass pulse width, NOT angle!
bmp1.relative_height = False
bmp1.captureStartingHeight()
#Data file vars
file_prefix = "sensor_data"
file_timestamp = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
file_extension = ".txt"
file_title = "sensor_data{}.csv"
#Create file
write_csv_data("/home/trapsat/Desktop/Janus_Data/" + file_title.format(file_timestamp), ['Timestamp','Temperature','Pressure','Altitude'])
#Set door closed
servo1.setAngle(500)
while(bmp1.enabled and free_space > min_space):
    free_space = shutil.disk_usage(file_path).free
    if(monitor_value == True):
        if ((bmp1.average_altitude >= door_open_height) and (door_opened == False)):
            print("Target Value Reached, opening door")
            servo1.setAngle(1500)
            door_opened = True
        elif((bmp1.average_altitude >= door_open_height and bmp1.average_altitude <= door_close_height) and door_opened == True):
            print('Taking picture...')
            camera1.take_picture()
        elif ((bmp1.average_altitude >= door_close_height) and door_opened == True):
            time.sleep(900000) #Wait 15 minutes
            print('Height limit exceeded, closing door.')
            servo1.setAngle(500)
            servo1.close()
            monitor_value = False
    
    bmp1.run_sensors()
    print('Temp = {0:0.2f} *C'.format(bmp1.temperature))
    print('Pressure = {0:0.2f} Pa'.format(bmp1.average_pressure))
    print('Altitude = {0:0.2f} m'.format(abs(bmp1.average_altitude)))
    write_csv_data(file_title.format(file_timestamp), [datetime.now(), bmp1.temperature, bmp1.average_pressure,bmp1.average_altitude])
    print('Assigned to CSV')
    time.sleep(3)

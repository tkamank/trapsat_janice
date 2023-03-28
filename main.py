import time
from servo.servo_internal import Internal_Servo;
from Camera.camera_internal import Internal_Camera;
from bmp.bmp_internal import Internal_BMPS;

#sudo pigpio

#BMPs need to be initialized before running main.py, run bmp_toggle first

#camera_1 = Internal_Camera()
#camera_1.take_picture()

servo1 = Internal_Servo()
camera1 = Internal_Camera()
bmp1 = Internal_BMPS()
door_opened = False
door_open_height = 1.00
door_close_height = 3.00
#Enable relative_height setting: Captures first altitude reading as baseline
#Open at 50,000 close at 55,000
#pass pulse width, NOT angle!

bmp1.relative_height = True
bmp1.captureStartingHeight()
servo1.setAngle(500)
f = open("sensor_data.txt","w")
while(bmp1.enabled):
    if(bmp1.average_altitude >= door_open_height and door_opened == False):
        print("Target Value Reached, opening door")
        servo1.setAngle(1500)
        door_opened = True
    elif ((bmp1.average_altitude >= door_close_height) and door_opened == True):
        servo1.setAngle(500)
        servo1.close()


    bmp1.run_sensors()
    print('Temp = {0:0.2f} *C'.format(bmp1.temperature))
    print('Pressure = {0:0.2f} Pa'.format(bmp1.average_pressure))
    print('Altitude = {0:0.2f} m'.format(abs(bmp1.average_altitude)))
    #print('Sealevel Pressure = {0:0.2f} Pa'.format(bmp1.read_sealevel_pressure()))
    ##Write to file##
    f.write('Temp = {0:0.2f} *C'.format(bmp1.temperature) + '\n')
    f.write('Pressure = {0:0.2f} Pa'.format(bmp1.average_pressure) + '\n')
    f.write('Altitude = {0:0.2f} m'.format(abs(bmp1.average_altitude)) + '\n')
    camera1.take_picture()
    time.sleep(3)
f.close()

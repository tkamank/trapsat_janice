import time
from servo.servo_internal import Internal_Servo;
from Camera.camera_internal import Internal_Camera;
from bmp.bmp_internal import Internal_BMPS;

camera_1 = Internal_Camera()
camera_1.take_picture()
""""
i = 0
while i < 20:
    camera_1.take_picture()
    i += 1
time.sleep(15)
servo_1 = Internal_Servo()
servo_1.setAngle(0)
servo_1.setAngle(135)
servo_1.setAngle(0)
servo_1.close()
"""


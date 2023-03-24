#Example Servo Code
#Control the angle of a 
#Servo Motor with Raspberry Pi

# free for use without warranty
# www.learnrobotics.org

import RPi.GPIO as GPIO
from time import sleep

#USES BCM DUE TO CAMERA MODULE
class Internal_Servo:
    pwm = None
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        self.pwm=GPIO.PWM(17, 50)
        self.pwm.start(0)

    def setAngle(self,angle):
        duty = angle / 18 + 2
        GPIO.output(17, True)
        self.pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(17, False)
        self.pwm.ChangeDutyCycle(duty)

    def close(self):
        self.pwm.stop()
        GPIO.cleanup()

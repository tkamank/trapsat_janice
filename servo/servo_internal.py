#Example Servo Code
#Control the angle of a 
#Servo Motor with Raspberry Pi

# free for use without warranty
# www.learnrobotics.org

import RPi.GPIO as GPIO
from time import sleep
import pigpio

#USES BCM DUE TO CAMERA MODULE
class Internal_Servo:
    pwm = None
    servo = 17
    def __init__(self):
        self.pwm=pigpio.pi()
        self.pwm.set_mode(self.servo, pigpio.OUTPUT)

    def setAngle(self,pulsewidth):
        self.pwm.set_servo_pulsewidth(self.servo, pulsewidth)
        sleep(3)


    def close(self):
        self.pwm.set_PWM_dutycycle(self.servo, 0)
        self.pwm.set_PWM_dutycycle(self.servo, 0)

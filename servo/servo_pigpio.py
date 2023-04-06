import RPi.GPIO as GPIO
import pigpio
import time
servo = 17

pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)

pwm.set_servo_pulsewidth(servo, 2500)
time.sleep(3)
pwm.set_servo_pulsewidth(servo, 2000)
time.sleep(3)
pwm.set_servo_pulsewidth(servo, 2500)
time.sleep(3)

pwm.set_PWM_dutycycle(servo, 0)
pwm.set_PWM_dutycycle(servo, 0)
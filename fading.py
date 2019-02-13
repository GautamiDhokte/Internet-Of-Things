import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
led_pin=18
GPIO.setup(led_pin,GPIO.OUT)
pwm =GPIO.PWM(led_pin,100)
pwm.start(0)
while True:
    for x in  range (0,100,5):
        pwm.ChangeDutyCycle(x)
        time.sleep(0.03)
    for x in  range (100,0,-5):
        pwm.ChangeDutyCycle(x)
        time.sleep(0.03)

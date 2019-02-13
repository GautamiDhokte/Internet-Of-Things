import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.IN)
GPIO.setup(35,GPIO.OUT)
try:
    while True:
        i=GPIO.input(3)
        if i==0:
            print('Obstacle not found')
            GPIO.output(35,GPIO.LOW)
            time.sleep(3)
        elif i==1:
            print('Obstacle found')
            GPIO.output(35,GPIO.HIGH)
            time.sleep(3)
        
except KeyboardInterrupt:
    GPIO.cleanup()

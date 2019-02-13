import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
while True:
    print('LED ON 18')
    GPIO.output(18,GPIO.HIGH)
    time.sleep(0.1)
    print('LED OFF 18')
    GPIO.output(18,GPIO.LOW)
    time.sleep(0.1)

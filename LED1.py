import RPi.GPIO as GPIO
import time
import dht11
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
dhtPin = dht11.DHT11(pin=38)
while dhtValue.temperature > 22:
       dhtValue = dhtPin.read()
       print('LED ON 18')
       GPIO.output(18,GPIO.HIGH)
       time.sleep(1.0)
       print('LED off 18 ')
       GPIO.output(18,GPIO.LOW)
       time.sleep(1.0)
       clear()

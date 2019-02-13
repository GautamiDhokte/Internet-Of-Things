import dht11
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40,GPIO.OUT)





while True:
    read1=dht11.DHT11(pin=12).read()
    if read1.is_valid():
        print (read1.temperature)
        print (read1.humidity)
        if read1.temperature>20 and read1.humidity>50:
            GPIO.output(40,GPIO.HIGH)
    time.sleep(1)    
    

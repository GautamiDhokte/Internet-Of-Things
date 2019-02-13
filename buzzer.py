import time
from RPi import GPIO

PIN = 22
BUZZER_REPETITIONS = 200
BUZZER_DELAY = 0.001
PAUSE_TIME = 0.3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

while True:
    for _ in xrange(BUZZER_REPETITIONS):
        for value in [True, False]:
            GPIO.output(PIN, value)
            time.sleep(BUZZER_DELAY)
    time.sleep(PAUSE_TIME)

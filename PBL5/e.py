import time
import random
import RPi.GPIO as GPIO

random.seed()
test_pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(test_pin, GPIO.IN)
GPIO.setup(40, GPIO.OUT)

def detect(channel):
    # rLen = random.randrange(20, 50, 1)
    # rf = random.randrange(2, 4, 1)
    # print('Detection led', rf, 'time for', end='')
    # print(' {:4.2f}'.format(rLen/31.4), end='')
    # print('second')
    # for flash in range(0, rf):
    #     GPIO.output(40, True)
    #     time.sleep(rLen/31.4)
    #     GPIO.output(40, False)
    #     time.sleep(rLen/31.4)

    
    return

GPIO.add_event_detect(test_pin, GPIO.RISING, callback=detect, bouncetime=200)
time.sleep(1)
print('System active')
for x in range(0, 1200):
    time.sleep(0.5)
time.sleep(5)
GPIO.output(40, False)
GPIO.remove_event_detect(test_pin)
GPIO.cleanup()
print('End')

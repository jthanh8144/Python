# import RPi.GPIO as GPIO
# import time

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(11, GPIO.IN)  # Read output from PIR motion sensor
# GPIO.setup(3, GPIO.OUT)  # LED output pin
# while True:
#     i = GPIO.input(11)
#     if i == 0:  # When output from motion sensor is LOW
#         print("No intruders", i)
#         GPIO.output(3, 0)  # Turn OFF LED
#         time.sleep(0.1)
#     elif i == 1:  # When output from motion sensor is HIGH
#         print("Intruder detected", i)
#         GPIO.output(3, 1)  # Turn ON LED
#         time.sleep(0.1)

import RPi.GPIO as GPIO
import time
import signal

GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)


def signal_handler(sig, frame):
    print("Quit")
    GPIO.cleanup()

def MOTION(PIR_PIN):
    print("Motion Detected!")


print("PIR Module Test (CTRL+C to exit)")
time.sleep(2)
print("Ready")

GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
# while 1:
#     time.sleep(100)

signal.signal(signal.SIGINT, signal_handler)
signal.pause()

# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM)

# pirPin = 4
# GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)

# while True:
#     if GPIO.input(pirPin) == GPIO.LOW:
#         print("Motion detected!")
#     else:
#         print("No motion")
#     time.sleep(0.5)
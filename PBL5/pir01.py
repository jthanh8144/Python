import RPi.GPIO as GPIO
import time
from picamera import PiCamera
import signal

def signal_handler(sig, frame):
    print("Quit")
    GPIO.cleanup()

def MOTION(PIN):
    if GPIO.input(pirPin) == GPIO.LOW:
        print("Motion")
        try: 
            camera.start_preview()
            # time.sleep(1)
            camera.capture('image%s.jpg' % counter)
            counter = counter + 1
            camera.stop_preview()
            time.sleep(2)
        except:
            camera.stop_preview()
    time.sleep(1)

GPIO.setmode(GPIO.BCM)

pirPin = 4
GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)
camera = PiCamera()
counter = 1

# while True:
#     if GPIO.input(pirPin) == GPIO.LOW:
#         print("Motion")
#         try: 
#             camera.start_preview()
#             # time.sleep(1)
#             camera.capture('image%s.jpg' % counter)
#             counter = counter + 1
#             camera.stop_preview()
#         except:
#             camera.stop_preview()
#     time.sleep(0.5)
GPIO.add_event_detect(pirPin, GPIO.RISING, callback=MOTION)

signal.signal(signal.SIGINT, signal_handler)
signal.pause()
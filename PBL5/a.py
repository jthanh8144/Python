import signal
import sys
import RPi.GPIO as GPIO


PIR_GPIO = 13
LED_GPIO = 14


def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


def button_callback(channel):
    print(GPIO.input(PIR_GPIO))
    if GPIO.input(PIR_GPIO):
        GPIO.output(LED_GPIO, GPIO.LOW)
    else:
        GPIO.output(LED_GPIO, GPIO.HIGH)



GPIO.setmode(GPIO.BCM)

GPIO.setup(PIR_GPIO, GPIO.IN)
GPIO.setup(LED_GPIO, GPIO.OUT)
GPIO.add_event_detect(PIR_GPIO, GPIO.BOTH,
                        callback=button_callback, bouncetime=50)

signal.signal(signal.SIGINT, signal_handler)
signal.pause()

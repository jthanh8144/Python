import time
import RPi.GPIO as GPIO
from gpiozero import AngularServo
import io
import socket
import struct
import picamera
import signal
from _thread import *
import warnings

warnings.filterwarnings("ignore")

isDoorOpen = False

pir_pin = 11
servo_pin = 18
ir_pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(ir_pin, GPIO.IN)
servo = AngularServo(servo_pin, min_pulse_width=0.0006, max_pulse_width=0.0023)

# close is -90, open is 70
def controlServo(angle):
    servo.angle = angle

controlServo(-90)

def detect(channel):
    print('co chuyen dong!')
    start_new_thread(send_to_server, (5, ))
    return


def signal_handler(sig, frame):
    print("Quit")
    GPIO.cleanup()


def send_to_server(num_of_image):
    count = 0
    
    connection = client_socket.makefile('wb')
    try:
        with picamera.PiCamera() as camera:
            camera.resolution = (1024, 768)
            camera.start_preview()
            time.sleep(2)

            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg'):
                connection.write(struct.pack('<L', stream.tell()))
                connection.flush()
                stream.seek(0)
                count += 1
                connection.write(stream.read())
                if count == num_of_image:
                    print('chup xong!')
                    camera.stop_preview()
                    camera.close()
                    return
                stream.seek(0)
                stream.truncate()
                print('Done!')

                time.sleep(1)
        connection.write(struct.pack('<L', 0))
    except:
        print('Something is error')

def receive_request():
    global isDoorOpen
    while True:
        data = client_socket.recv(1024)
        if data != b'':
            if ('open-door' in data.decode('utf-8')):
                print('success')
                controlServo(70)
                isDoorOpen = True
                print(isDoorOpen)
            elif ('re-identify' in data.decode('utf-8')):
                start_new_thread(send_to_server, (5, ))

def auto_close_door(check_time):
    global isDoorOpen
    isDoorOpen = True
    while True:
        if (GPIO.input(ir_pin) == 0 and isDoorOpen == True):
            print(GPIO.input(ir_pin))
            for i in range (check_time):
                time.sleep(1)
                if (GPIO.input(ir_pin) != 0):
                    break
            if (GPIO.input(ir_pin) == 0):
                print('auto close the door')
                controlServo(-90)
                isDoorOpen = False

server_ip = '192.168.1.4'
server_port = 9000
client_socket = socket.socket() # socket.AF_INET, socket.SOCK_STREAM
client_socket.connect((server_ip, server_port))
print('connected')

start_new_thread(receive_request, ())
start_new_thread(auto_close_door, (5, ))

GPIO.add_event_detect(pir_pin, GPIO.RISING, callback=detect, bouncetime=15000)
signal.signal(signal.SIGINT, signal_handler)
signal.pause()

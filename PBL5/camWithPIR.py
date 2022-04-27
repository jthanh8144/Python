import time
import RPi.GPIO as GPIO
import io
import socket
import struct
import picamera
import signal
from _thread import *
import warnings

warnings.filterwarnings("ignore")

test_pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(test_pin, GPIO.IN)
# GPIO.setup(40, GPIO.OUT)


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
    while True:
        data = client_socket.recv(1024)
        if data != b'':
            if ('success' in data.decode('utf-8')):
                print('do something')
            if ('fail' in data.decode('utf-8')):
                print('block something')

server_ip = '192.168.1.2'
server_port = 9000
client_socket = socket.socket() # socket.AF_INET, socket.SOCK_STREAM
client_socket.connect((server_ip, server_port))
print('connected')

start_new_thread(receive_request, ())

GPIO.add_event_detect(test_pin, GPIO.RISING, callback=detect, bouncetime=15000)
signal.signal(signal.SIGINT, signal_handler)
signal.pause()

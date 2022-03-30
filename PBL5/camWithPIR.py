import io
import time
import socket
import struct
import signal
import picamera
import RPi.GPIO as GPIO

test_pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(test_pin, GPIO.IN)


def detect(channel):
    print('co chuyen dong!')
    send_to_server(10)
    return


def signal_handler(sig, frame):
    print("Quit")
    GPIO.cleanup()


def send_to_server(time_out):
    server_ip = '192.168.1.5'
    server_port = 9000
    start_time = time.time()

    client_socket = socket.socket()
    client_socket.connect((server_ip, server_port))
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
                connection.write(stream.read())
                if time.time() - start_time > time_out:
                    print('chup xong!')
                    connection.close()
                    client_socket.close()
                    stream.seek(0)
                    stream.truncate()
                    return
                stream.seek(0)
                stream.truncate()
                print('Done!')

                time.sleep(1)
        connection.write(struct.pack('<L', 0))
    finally:
        connection.close()
        client_socket.close()


GPIO.add_event_detect(test_pin, GPIO.RISING, callback=detect, bouncetime=15000)
signal.signal(signal.SIGINT, signal_handler)
signal.pause()

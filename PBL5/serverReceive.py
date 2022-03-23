import io
import socket
import struct
from PIL import Image
from _thread import *

def thread_client(connection):
    while True:
        cnn = connection.read(4)
        if cnn != b'':
            image_len = struct.unpack('<L', cnn)[0]

            image_stream = io.BytesIO()
            image_stream.write(connection.read(image_len))

            image_stream.seek(0)
            image = Image.open(image_stream)
            print('Image is %dx%d' % image.size)

            image.save('abc.jpeg')
        else:
            break
    connection.close()

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 9000))
server_socket.listen(0)

while True:
    connection = server_socket.accept()[0].makefile('rb')
    start_new_thread(thread_client, (connection, ))

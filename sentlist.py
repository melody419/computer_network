import socket
import json
import os


s = socket.socket()

s.bind(('', 12345))

s.listen(5)

while True:

    c, addr = s.accept()

    list_to_send = [f for f in os.listdir('.') if os.path.isfile(
        f) and (f.endswith('.Mjpeg') or f.endswith('.mjpeg'))]

    list_to_send_json = json.dumps(list_to_send)

    c.send(list_to_send_json.encode())

    c.close()

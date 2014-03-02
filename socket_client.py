# Royce Pope
# Feb 28 2014
# Socket Client

import socket

HOST = '127.0.0.1'
PORT = 50005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b"Hello World")
data = s.recv(1024)
s.close()
print ("Recieved", repr(data))

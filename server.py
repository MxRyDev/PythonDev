# Royce Pope
# Python 2.7

import socket
import time
import sys
from thread import *
 
HOST = ''   # All Interfaces
PORT = 8888 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print '====================SOCKET CREATED====================\n'

time.sleep(1)
print "               =====Binding Ports=====" 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
time.sleep(2)
print '              >-[                   ]-<'
time.sleep(.3)
print '              >--[                 ]--<'
time.sleep(.3)
print '              >---[               ]---<'
time.sleep(.3)
print '              >----[             ]----<'
time.sleep(.3)
print '              >-----[           ]-----<'
time.sleep(.3)
print '              >------[         ]------<'
time.sleep(.3)
print '              >-------[       ]-------<'
time.sleep(.3)
print '              >--------[     ]--------<'
time.sleep(.3)
print '              >---------[   ]---------<'   
time.sleep(.3)
print '              >----------[ ]----------<'
time.sleep(.3)
print '              >----------[=]----------<\n'
time.sleep(.5)
print '=================Socket Bind Complete=================\n'
time.sleep(1)
print "          ===Starting Listening Sequence===\n" 
def waitingthread(s):
    while True:
        for i in range(10):
            print("Listening" + "." * i)
            sys.stdout.write("\033[F") # Cursor up one line
            time.sleep(1)
        if i == 9:
            #sys.stdout.write("\033[F")
            sys.stdout.write("                   ")
            i = 0
            waitingthread(s)

        
s.listen(10)
print 'Socket now listening\n'
start_new_thread(waitingthread,(s,))
 
#Function for handling connections.
def clientthread(conn):
    conn.send('Welcome to the server. Type something and hit enter\n')
    
    while True:
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data: 
            break
     
        conn.sendall(reply)

    conn.close()

 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread: conn = the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
    
 
s.close()
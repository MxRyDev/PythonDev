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

s.bind((HOST, PORT))

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
            
            sys.stdout.write("                   ")
            i = 0
            waitingthread(s)

        
s.listen(10)
print 'Socket now listening\n'
start_new_thread(waitingthread,(s,))
 
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept() 
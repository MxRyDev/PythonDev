import sys
import time


print ('==================TCP LOCK INITIATED==================\n')

def spinner(delay):
    for char in '/-\|':        
      sys.stdout.write("                           "+char)
      sys.stdout.flush()
      sys.stdout.write("\b" * 28)
      time.sleep(delay)
      
      
print ("                   'ENTER'to lock\n")
lock = 1
spinner(.3)
lock = input()
lock = 2
spinner(.3)
lock = input()
lock = 3
spinner(.3)
lock = input()
lock = 4
spinner(.3)
lock = input()
lock = 5
if lock == 5:
    for x in range(0,10):
        spinner(.05)
    print ("                           \/\n")
    print ("========================LOCKED========================")

   

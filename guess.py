# Royce Pope
# Feb 28 2014
# Guessing Game

import time
import random
from random import randint

print """
***********************************
*                                 *
*          WELCOME TO             *
*     Royce's Guessing Game       *
*                                 *
***********************************
"""
print """Rules: Try to guess the number that is
       randomly generated by the CPU!
            """
ready = raw_input("Ready?(Y/N)> ")

if ready == "Y":
    print "GO!"
    print "*"
    time.sleep(.5)
    print "*" * 2
    time.sleep(.5)
    print "*" * 3
    time.sleep(.5)
    print "*" * 4
    time.sleep(.5)
    print "*" * 5
    time.sleep(.5)
    print "*" * 6
    
else:
    print "Fine! don't play!"
time.sleep(1)

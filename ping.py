# Royce Pope
# March 6 2014
# Ping Program

import subprocess
import time

netID = '10.10.0.'  # Set the Network ID here.
host_start = 1      # Set the Host start here.
host_end = 4        # Set the Host end here.

for host in range(host_start, host_end):
    address = netID + str(host)
    response = subprocess.call(["ping", "-c", "1", "-n", "-W", "2", address])
    if response == 0:
        print (address, "===ONLINE===\n")
        time.sleep(.5)
    elif response == 2:
        print (address, "===OFFLINE===\n")
        time.sleep(.5)
    else:
        print ("PING FAILED!")
        
for host in range(100,103):
    address = netID + str(host)
    response = subprocess.call(["ping", "-c", "1", "-n", "-W", "2", address])
    if response == 0:
        print (address, "===ONLINE===\n")
        time.sleep(.5)
    elif response == 2:
        print (address, "===OFFLINE===\n")
        time.sleep(.5)
    else:
        print ("PING FAILED!")
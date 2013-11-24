#!/usr/bin/python

import bluetooth
import time

print "In/Out Board"

while True:
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())

    result = bluetooth.lookup_name('E8:3E:B6:F6:B4:32', timeout=5)
    if (result != None):
        print "Adam Playbook: in"
    else:
        print "Adam Playbook: out"


    result = bluetooth.lookup_name('AC:22:0B:60:39:E2', timeout=5)
    if (result != None):
        print "Bob Nexus: in"
    else:
        print "Bob Nexus: out"

    result = bluetooth.lookup_name('40:7A:80:B0:4F:35', timeout=5)
    if (result != None):
        print "Bob Windows Phone: in"
    else:
        print "Bob Windows Phone: out"


    result = bluetooth.lookup_name('C0:18:85:FC:7B:48', timeout=5)
    if (result != None):
        print "Bob Laptop: in"
    else:
        print "Bob Laptop: out"


    time.sleep(60)


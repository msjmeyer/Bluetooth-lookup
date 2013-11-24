#!/usr/bin/python

import bluetooth
import time

print "In/Out Board"

while True:
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())

    result = bluetooth.lookup_name('E8:3E:B6:F6:B4:32', timeout=5)
    if (result != None):
        print "Ma Playbook: in"
    else:
        print "Ma Playbook: out"


    result = bluetooth.lookup_name('AC:22:0B:60:39:E2', timeout=5)
    if (result != None):
        print "Marthinus Nexus: in"
    else:
        print "Marthinus Nexus: out"

    result = bluetooth.lookup_name('40:7A:80:B0:4F:35', timeout=5)
    if (result != None):
        print "Marthinus Windows Phone: in"
    else:
        print "Marthinus Windows Phone: out"


    result = bluetooth.lookup_name('C0:18:85:FC:7B:48', timeout=5)
    if (result != None):
        print "Marthinus Laptop: in"
    else:
        print "Marthinus Laptop: out"


    time.sleep(60)


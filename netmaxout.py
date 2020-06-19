#!/usr/bin/env python
import Netmaxiot
from time import sleep
Netmaxiot.pinMode(2,"OUTPUT")
Netmaxiot.pinMode(3,"OUTPUT")
Netmaxiot.pinMode(4,"OUTPUT")
while 1:
	print "Shield Pins 2,3,4 high"
	Netmaxiot.digitalWrite(2,1)
	Netmaxiot.digitalWrite(3,1)
	Netmaxiot.digitalWrite(4,1)
	sleep(0.05)
	Netmaxiot.digitalWrite(2,0)
	Netmaxiot.digitalWrite(3,0)
	Netmaxiot.digitalWrite(4,0)
	print "Shield Pins 2,3,4 low"
	sleep(0.05)
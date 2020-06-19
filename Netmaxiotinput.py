import time
import Netmaxiot
x = 5
Netmaxiot.pinMode(x,"INPUT")
try:
	while True:
		lx=Netmaxiot.digitalRead(x)
		print "the value of our input is=%d" %lx
		time.sleep(0.2)
except IOError:
	print ("Error")
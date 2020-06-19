import Netmaxiot
from time import sleep
while 1:
	read=Netmaxiot.analogRead(0)
	light=read/1000
	light=light*100
	print "The light from LDR == %d Percent " %light
	sleep(1)
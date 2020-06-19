import Netmaxiot
from time import sleep
while 1:
	read=Netmaxiot.analogRead(0)
	voltage=read*4.887
	print "our voltage is == %0.3f mv " %voltage
	light=voltage/5000
	light=light*100
	print "The light from LDR == %0.3f Percent " %light
	sleep(1)
import Netmaxiot
from time import sleep
while 1:
	read=Netmaxiot.analogRead(0)
	read1=Netmaxiot.analogRead(1)
	voltage=read*4.887
	voltage1=read1*4.887
	print "our voltage is == %0.3f mv " %voltage
	light=voltage/5000
	light=light*100
	temp=voltage1/10
	print "The light from LDR == %0.3f Percent " %light
	print "The temp from ln35sensor is == %0.3f celcius " %temp
	sleep(2)
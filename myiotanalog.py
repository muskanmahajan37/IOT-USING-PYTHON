import Netmaxiot
from time import sleep
while 1:
	read=Netmaxiot.analogRead(0)
	read1=Netmaxiot.analogRead(1)
	read2=Netmaxiot.analogRead(2)
	read3=Netmaxiot.analogRead(3)
	
	voltage=read*4.887
	voltage1=read1*4.887
	voltage2=read2*4.887
	voltage3=read3*4.887
	print "------------------"
	print "the value of voltage1 is %0.2f" %voltage
	print "------------------"
	print "the value of voltage2 is %0.2f" %voltage1
	print "------------------"
	print "the value of voltage3 is %0.2f" %voltage2
	print "------------------"
	print "the value of voltage4 is %0.2f" %voltage3
	sleep(1)
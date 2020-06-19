import Netmaxiot
from time import sleep
while 1:
	read1=Netmaxiot.analogRead(2)
	read2=Netmaxiot.analogRead(3)
	voltage1=read1*4.887
	voltage2=read2*4.887
	temp=voltage2/10
	light=(voltage1/5000)*100
	print "our light is == %0.1f percent " %light
	print "The temp is  == %0.1f degree " %temp
	sleep(1)
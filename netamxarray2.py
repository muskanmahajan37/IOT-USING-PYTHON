import Netmaxiot
from time import sleep
pins=[2,3,4,5,6,7]
for i in range(0,6):
	Netmaxiot.pinMode(pins[i],"OUTPUT")
while True:
	for i in range(0,6):
		Netmaxiot.digitalWrite(pins[i],1)
		sleep(0.1)
		print i
	for i in range(5,-1,-1):
		Netmaxiot.digitalWrite(pins[i],0)
		sleep(0.1)
		print i	
	sleep(2)
	for i in range(5,-1,-1):
		Netmaxiot.digitalWrite(pins[i],1)
		sleep(0.1)
		print i
	for i in range(0,6):
		Netmaxiot.digitalWrite(pins[i],0)
		sleep(0.1)
		print i	
	sleep(2)	
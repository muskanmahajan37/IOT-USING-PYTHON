from time import sleep
import Netmaxiot
Netmaxiot.pinMode(3,"OUTPUT")
Netmaxiot.pinMode(5,"OUTPUT")
Netmaxiot.pinMode(6,"OUTPUT")
Netmaxiot.digitalWrite(2,0)
Netmaxiot.digitalWrite(3,0)
Netmaxiot.digitalWrite(4,0)
Netmaxiot.digitalWrite(5,0)
Netmaxiot.digitalWrite(6,0)
i = 0
while True:
	i=0
	for x in range(0,255):
		print (i)
		Netmaxiot.analogWrite(3,i)
		Netmaxiot.analogWrite(5,i)
		Netmaxiot.analogWrite(6,i)
		i = i + 10
		sleep(0.2)
		if i > 255:
			i = 0
	i=255    	
	for x in range(255,0,-1):
		print (i)
		Netmaxiot.analogWrite(3,i)
		Netmaxiot.analogWrite(5,i)
		Netmaxiot.analogWrite(6,i)
		i = i - 10
		sleep(0.2)
		if i > 255:
			i = 0        

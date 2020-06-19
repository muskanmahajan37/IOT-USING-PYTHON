from time import sleep
import Netmaxiot
s1 = 5
s2 = 6
Netmaxiot.pinMode(s1,"INPUT")
Netmaxiot.pinMode(s2,"INPUT")
Netmaxiot.pinMode(2,"OUTPUT")
Netmaxiot.pinMode(3,"OUTPUT")
Netmaxiot.pinMode(4,"OUTPUT")
try:
	while True:
		x=Netmaxiot.digitalRead(s1)
		y=Netmaxiot.digitalRead(s2)
		if x==0:
			Netmaxiot.digitalWrite(2,1)
			Netmaxiot.digitalWrite(3,1)
			Netmaxiot.digitalWrite(4,1)
			sleep(0.2)
			Netmaxiot.digitalWrite(2,0)
			Netmaxiot.digitalWrite(3,0)
			Netmaxiot.digitalWrite(4,0)
			print "Switch 1 pressed"
			sleep(0.2)
		elif y==0:
			Netmaxiot.digitalWrite(2,1)
			Netmaxiot.digitalWrite(3,1)
			Netmaxiot.digitalWrite(4,0)
			sleep(0.2)
			Netmaxiot.digitalWrite(2,0)
			Netmaxiot.digitalWrite(3,1)
			Netmaxiot.digitalWrite(4,1)
			print "Switch 2  pressed"
			sleep(0.2)			
		else:
			Netmaxiot.digitalWrite(2,1)
			Netmaxiot.digitalWrite(3,0)
			Netmaxiot.digitalWrite(4,1)
			sleep(0.4)
			Netmaxiot.digitalWrite(2,0)
			Netmaxiot.digitalWrite(3,1)
			Netmaxiot.digitalWrite(4,0)
			print "Switch Not pressed"
			sleep(0.4)			

		sleep(0.1)

except IOError:
	print ("Error")
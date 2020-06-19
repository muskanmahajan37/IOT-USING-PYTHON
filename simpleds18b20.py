from w1thermsensor import W1ThermSensor
from time import sleep
sensor = W1ThermSensor()
while 1:
	x= sensor.get_temperature()
	y=round(x,2)
	print y
	sleep(1)


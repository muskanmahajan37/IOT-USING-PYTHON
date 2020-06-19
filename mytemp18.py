from w1thermsensor import W1ThermSensor
import time
sensor=W1ThermSensor()
while 1:
	tempds=sensor.get_temperature()
	y=round(tempds,2)
	print y
	time.sleep(1)
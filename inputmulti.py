import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)## Use board pin numbering
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(24,GPIO.IN)
GPIO.setup(23,GPIO.IN)
while 1:
	if GPIO.input(24)==0:
		GPIO.output(17,1)
		GPIO.output(27,1)
		GPIO.output(22,0)
		print "Switch 1 is on :)"
		sleep(0.5)
		GPIO.output(17,0)
		GPIO.output(27,1)
		GPIO.output(22,1)
		print "Switch 1 is on :)"
		sleep(0.5)
	elif GPIO.input(23)==0:
		GPIO.output(17,1)
		GPIO.output(27,0)
		GPIO.output(22,1)
		print "Switch 2 == is on :)"
		sleep(0.2)
		GPIO.output(17,0)
		GPIO.output(27,1)
		GPIO.output(22,0)
		print "Switch 2 == is on :)"
		sleep(0.2)		
	else:
		GPIO.output(17,1)
		GPIO.output(27,1)
		GPIO.output(22,1)
		print "Switch is off"
		sleep(1)
		GPIO.output(17,0)
		GPIO.output(27,0)
		GPIO.output(22,0)
		print "Switch is off"
		sleep(1)

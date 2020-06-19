import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
#############################
GPIO.output(17,0)
GPIO.output(27,0)
GPIO.output(22,0)
GPIO.output(5,0)
GPIO.output(6,0)
GPIO.output(13,0)
GPIO.output(19,0)
try:
	for i in range(0,100):
		print i
		GPIO.output(17,1)
		GPIO.output(27,0)
		GPIO.output(22,1)
		time.sleep(0.2)
		print "please check pins 17,27,22,5,6,13,19"
		GPIO.output(17,0)
		GPIO.output(27,1)
		GPIO.output(22,0)
		time.sleep(0.2)
except KeyboardInterrupt:
	print " "
	print "KeyboardInterrupt"
	GPIO.output(17,0)
	GPIO.output(27,0)
	GPIO.output(22,0)
	print "bye bye"

import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17,GPIO.OUT)
#############################
pins=[17,27,22,5,6,13,19]
for i in range(0,7):
	GPIO.setup(pins[i],GPIO.OUT)
for i in range(0,7):
		GPIO.output(pins[i],0)	
###############################		
x = GPIO.PWM(17,1000) #1 khz
x.start(10)
y = GPIO.PWM(27,1000) #1 khz
y.start(10)
z = GPIO.PWM(22,1000) #1 khz
z.start(10)
while 1:
	for i in range(0,100,2):
		print "pwm dutycycle is %d"%i    
		sleep(0.2)
		x.ChangeDutyCycle(i)
		y.ChangeDutyCycle(i)
		z.ChangeDutyCycle(i)
	for i in range(99,0,-2):
		print "pwm dutycycle is %d"%i    
		sleep(0.2)
		x.ChangeDutyCycle(i)
		y.ChangeDutyCycle(i)
		z.ChangeDutyCycle(i)

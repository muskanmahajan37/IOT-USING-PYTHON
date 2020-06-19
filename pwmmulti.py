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
print "hi pwm start with 10 % --dutycycles"                            
sleep(5)

while 1:
	print "pwm inside loop"    
	sleep(0.3)
	x.ChangeDutyCycle(90)
	y.ChangeDutyCycle(90)
	print "pwm is 90"
	sleep(0.3)
	x.ChangeDutyCycle(80)
	y.ChangeDutyCycle(80)
	print "pwm is 80"
	sleep(0.3)
	x.ChangeDutyCycle(70)
	y.ChangeDutyCycle(70)
	print "pwm is 70"
	sleep(0.3)
	x.ChangeDutyCycle(60)
	print "pwm is 60"
	sleep(0.3)
	x.ChangeDutyCycle(50)
	print "pwm is 50"
	sleep(0.3)
	x.ChangeDutyCycle(40)
	print "pwm is 40"
	sleep(0.3)
	x.ChangeDutyCycle(30)
	print "pwm is 30"
	sleep(0.3)
	x.ChangeDutyCycle(20)
	print "pwm is 20"
	sleep(0.3)
	x.ChangeDutyCycle(10)
	print "pwm is 10"
	sleep(0.3)
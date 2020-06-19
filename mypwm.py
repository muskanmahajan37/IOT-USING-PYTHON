import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
#############################
pins=[17,27,22,5,6,13,19]
for i in range(0,7):
	GPIO.setup(pins[i],GPIO.OUT)
	GPIO.output(pins[i],0)	
###############################		
mypwm = GPIO.PWM(17,1000) #1 khz
mypwm.start(10)
print "hi pwm start with 10 % --dutycycles"                            
sleep(5)

while 1:
	print "pwm inside loop"    
	sleep(0.3)
	mypwm.ChangeDutyCycle(90)
	print "pwm is 90"
	sleep(0.3)
	mypwm.ChangeDutyCycle(80)
	print "pwm is 80"
	sleep(0.3)
	mypwm.ChangeDutyCycle(70)
	print "pwm is 70"
	sleep(0.3)
	mypwm.ChangeDutyCycle(60)
	print "pwm is 60"
	sleep(0.3)
	mypwm.ChangeDutyCycle(50)
	print "pwm is 50"
	sleep(0.3)
	mypwm.ChangeDutyCycle(40)
	print "pwm is 40"
	sleep(0.3)
	mypwm.ChangeDutyCycle(30)
	print "pwm is 30"
	sleep(0.3)
	mypwm.ChangeDutyCycle(20)
	print "pwm is 20"
	sleep(0.3)
	mypwm.ChangeDutyCycle(10)
	print "pwm is 10"
	sleep(0.3)
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pins=[17,27,22,5,6,13,19]
for i in range(0,7):
	GPIO.setup(pins[i],GPIO.OUT)
	print "GPIO PIN %d output " %i
while True:
	for i in range(0,7):
		GPIO.output(pins[i],1)
		print "LED's %d ON "%i
		print i
		time.sleep(1)
		GPIO.output(pins[i],0)
		print "LED's off.."
		time.sleep(0.3)
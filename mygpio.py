import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
#############################
GPIO.output(17,0)
GPIO.output(27,0)
GPIO.output(22,0)
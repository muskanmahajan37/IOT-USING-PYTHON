#!/usr/bin/python
import Adafruit_DHT
import time
import requests
sensor = Adafruit_DHT.DHT11
pin =24

def myfunction():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print humidity
    print temperature
    time.sleep(3)
    payload = {'mytemp':temperature, 'myhumdity':humidity}
    return payload

while 1:
        try:
            r = requests.post('http://things.ubidots.com/api/v1.6/devices/rasp/?token=A1E-ToN1xlIF989YzJc1LkB2XBxXeLyD27', data=myfunction())
            print('sending our values to ubi dots ')
            print(myfunction())
        except:
            pass
            print "sadi values ubi dots teh nahin gayi wires check karo"          
        time.sleep(10)

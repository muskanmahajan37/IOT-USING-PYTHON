#!/usr/bin/env python
import time
import Netmaxiot
Netmaxiot.pinMode(2,"OUTPUT")
Netmaxiot.pinMode(3,"OUTPUT")
Netmaxiot.pinMode(4,"OUTPUT")
Netmaxiot.pinMode(5,"OUTPUT")
Netmaxiot.pinMode(6,"OUTPUT")
time.sleep(1)
i = 0
try:
    Netmaxiot.digitalWrite(2,0)
    Netmaxiot.digitalWrite(3,0)
    Netmaxiot.digitalWrite(4,0)

    Netmaxiot.analogWrite(3,255)
    time.sleep(2)
    Netmaxiot.analogWrite(3,128)
    time.sleep(2)
    while True:
        print (i)
        Netmaxiot.analogWrite(3,i)
        Netmaxiot.analogWrite(5,i)
        Netmaxiot.analogWrite(6,i)
        i = i + 5

        time.sleep(0.05)
        if i > 255:
            i = 0        
except KeyboardInterrupt:
    Netmaxiot.analogWrite(3,0)
except IOError:
    print ("Error")
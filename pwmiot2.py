from time import sleep
import Netmaxiot
Netmaxiot.pinMode(3,"OUTPUT")
Netmaxiot.pinMode(5,"OUTPUT")
Netmaxiot.pinMode(6,"OUTPUT")
i = 0
while True:
    print (i)
    Netmaxiot.analogWrite(3,i)
    Netmaxiot.analogWrite(5,i)
    Netmaxiot.analogWrite(6,i)
    i = i + 10
    sleep(0.2)
    if i > 255:
        i = 0        

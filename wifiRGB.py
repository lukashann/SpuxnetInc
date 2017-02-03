import machine
import tcs34725
from machine import Pin, I2C
import time
import network
from umqtt.simple import MQTTClient

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
sensor = tcs34725.TCS34725(i2c)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
while sta_if.isconnected() == False:
	sta_if.connect('EEERover', 'exhibition')
	time.sleep(5)
	
client = MQTTClient(machine.unique_id(),'192.168.0.10')
client.connect()
client.publish('esys/SpuxnetInc', bytes('Stuxnet Virus!', 'utf-8'))
data = sensor.read(True)
print(data)
int1, int2, int3, int4 = data

stringData = str(data)

#stringData = struct.pack(int1, int2)

print(data[0])
print("stringData: " + stringData)

#client.publish('esys/SpuxnetInc', payload=int1)
client.publish('esys/SpuxnetInc', bytes(stringData, 'utf-8'))

client.publish('esys/SpuxnetInc', bytes('Stuxnet Virus Finished!', 'utf-8'))

client.disconnect()
sta_if.disconnect()

#i2c = I2C(scl=Pin(4), sda=Pin(5), freq=100000)
# address of RGB color sensor is 0x29
#i2c.writeto(0x29, '0')
#print(i2c.readfrom(0x29, 3))





#from machine import I2C, Pin
#i2c = I2C(Pin(5), Pin(4))
#print(i2c.scan())

print(sensor.read(True))

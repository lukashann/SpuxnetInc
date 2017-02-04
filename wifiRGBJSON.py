import machine
import json
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

print("stringData: " + str(data))

payload = json.dumps({'red':data[0], 'green':data[1], 'blue':data[2], 'clear':data[3]})
print(payload)

client.publish('esys/SpuxnetInc', bytes(payload, 'utf-8'))

client.publish('esys/SpuxnetInc', bytes('Stuxnet Virus Finished!', 'utf-8'))

client.disconnect()
sta_if.disconnect()




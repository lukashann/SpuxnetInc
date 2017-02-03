import machine
from machine import Pin, I2C
import time
import network
from umqtt.simple import MQTTClient

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
while sta_if.isconnected() == False:
	sta_if.connect('EEERover', 'exhibition')
	time.sleep(5)
	
client = MQTTClient(machine.unique_id(),'192.168.0.10')
client.connect()
client.publish('esys/SpuxnetInc', bytes('hello world!', 'utf-8'))

client.disconnect()
sta_if.disconnect()

i2c = I2C(scl=Pin(4), sda=Pin(5), freq=100000)
# address of RGB color sensor is 0x29
i2c.writeto(0x29, '0')
print(i2c.readfrom(0x29, 3))


import machine
import time
import network
from umqtt.simple import MQTTClient

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
sta_if = network.WLAN(network.STA_IF)


if sta_if.isconnected() == False:
	sta_if.active(True)
	sta_if.connect('EEERover', 'exhibition')
	
client = MQTTClient(machine.unique_id(),'192.168.0.10')
client.connect()
client.publish('esys/SpuxnetInc', bytes('hello world!', 'utf-8'))

client.disconnect()
sta_if.disconnect()




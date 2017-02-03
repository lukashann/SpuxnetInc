from umqtt.simple import MQTTClient
import network
import machine


ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
sta_if = network.WLAN(network.STA_IF)
sta_if.connect('EEERover', 'exhibition')


BROKER_ADDRESS = 192.168.0.10
CLIENT_ID = machine.unique_id()

client = MQTTClient(CLIENT_ID,BROKER_ADDRESS)
client.connect()

TOPIC = ' esys/stuxnet_inc/hello_world'
data = 'Stuxnet rip'
client.publish(TOPIC,bytes(data,'utf-8'))


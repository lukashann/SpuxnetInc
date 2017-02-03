import machine
import time
import network
from umqtt.simple import MQTTClient


class WifiBroker(object):

    def __int__(self, BROKER_ADDRESS='192.168.0.10', TOPIC='esys/SpuxnetInc'):
        self.BROKER_ADDRESS = BROKER_ADDRESS
        self.CLIENT_ID = machine.unique_id()
        self.TOPIC = TOPIC

    def connect_to_broker(self):
        self.ap_if = network.WLAN(network.AP_IF)
        self.ap_if.active(False)

        self.sta_if = network.WLAN(network.STA_IF)
        self.sta_if.active(True)

        while not self.sta_if.isconnected():
            self.sta_if.connect('EEERover', 'exhibition')
            time.sleep(5)

        self.client = MQTTClient(machine.unique_id(), '192.168.0.10')
        self.client.connect()

    def pub_message(self, msg):
        self.client.publish(self.TOPIC, bytes(msg, 'utf-8'))

    def disconnect(self):
        self.client.disconnect()
        self.sta_if.disconnect()

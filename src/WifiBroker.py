import machine
import time
import network
from umqtt.simple import MQTTClient


class WifiBroker(object):

    def __init__(self):
        self.BROKER_ADDRESS = '192.168.0.10'
        self.CLIENT_ID = machine.unique_id()
        self.TOPIC = 'esys/SpuxnetInc'
        self.essid = 'EEERover'
        self.pw = 'exhibition'
        self.client = MQTTClient(self.CLIENT_ID, self.BROKER_ADDRESS)
        self.ap_if = network.WLAN(network.AP_IF)
        self.sta_if = network.WLAN(network.STA_IF)

    def connect_to_broker(self):
        self.ap_if.active(False)
        self.sta_if.active(True)
        print('test')

        while not self.sta_if.isconnected():
            self.sta_if.connect(self.essid, self.pw)
            time.sleep(5)

        self.client.connect()
        print('Connected')

    def publish_msg(self, msg):
        print(msg)
        self.client.publish(self.TOPIC, bytes(msg, 'utf-8'))

    def disconnect(self):
        print('Disconnect')
        self.client.disconnect()
        self.sta_if.disconnect()

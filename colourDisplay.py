import tkinter
import time
import uuid
import json
import paho.mqtt.client as client

class MQTT_Broker(object):
	'''Class for connecting computer to the broker.'''

	def __init__(self, w):
		self.BROKER_ADDRESS = '192.168.0.10'
		self.CLIENT_ID = "P1"
		self.TOPIC = 'esys/SpuxnetInc'
		self.client = client.Client(self.CLIENT_ID)
		self.widget = w

	def connect_to_broker(self):
		'''Connect to the broker'''
		self.client.connect(self.BROKER_ADDRESS)
		self.client.loop_start()
		print('Connected')

	def subscribe(self):
		self.client.subscribe(self.TOPIC)

	def on_message(self, on_message_func):
		self.client.on_message = on_message_func

def update_widget(name, red, green, blue):
	global widget_colour
	global widget_text
	ct_hex = '%02x%02x%02x' % (red, green, blue)
	bg_colour = '#' + ''.join(ct_hex)
	widget_colour = bg_colour
	widget_text = name

def on_message(client, userdata, message):
	data = json.loads(str(message.payload.decode("utf-8")))
	update_widget(data['name'], data['red'], data['green'], data['blue'])

broker = MQTT_Broker(w)
broker.connect_to_broker()
broker.subscribe()
broker.on_message(on_message)


root = tkinter.Tk()

init_ct_hex = '%02x%02x%02x' % (0, 0, 0)
init_bg_colour = '#' + ''.join(init_ct_hex)

w = tkinter.Label(root, text='Press Button to identify Colour', bg=init_bg_colour, fg='white', font=('Helvetica', 30))
w.pack(padx=50, pady=100, side=tkinter.LEFT)


global widget_colour
global widget_text

widget_colour = init_bg_colour
widget_text = 'Press Button to identify Colour'

while True:
	w.configure(bg=widget_colour)
	w.configure(text=widget_text)
	w.update_idletasks()
	w.update()
	time.sleep(1)


import tkinter
import time
import uuid
import paho.mqtt.client as client

class MQTT_Broker(object):
	'''Class for connecting computer to the broker.'''

	def __init__(self):
		self.BROKER_ADDRESS = '192.168.0.10'
		self.CLIENT_ID = "P1"
		self.TOPIC = 'esys/SpuxnetInc'
		self.client = client.Client(self.CLIENT_ID)

	def connect_to_broker(self):
		'''Connect to the broker.'''
		self.client.connect(self.BROKER_ADDRESS)
		self.client.loop_start()
		print('Connected')

	def subscribe(self):
		self.client.subscribe(self.TOPIC)

	def on_message(self, on_message_func):
		self.client.on_message = on_message_func

def update_widget(name, red, green, blue):
	red = 112
	blue = 53
	green = 9
	ct_hex = '%02x%02x%02x' % (red, green, blue)
	bg_colour = '#' + ''.join(ct_hex)
	w.configure(bg=bg_colour)
	w.configure(text = name)

def on_message(client, userdata, message):
	print("message received  "  ,str(message.payload.decode("utf-8")))
	data = json.loads(str(message.payload.decode("utf-8")))
	update_widget(data['name'], data['red'], data['green'], data['blue'])


broker = MQTT_Broker()
broker.connect_to_broker()
broker.subscribe()
broker.on_message(on_message)

root = tkinter.Tk()

init_ct_hex = '%02x%02x%02x' % (0, 0, 0)
init_bg_colour = '#' + ''.join(init_ct_hex)

w = tkinter.Label(root, text='Press Button to identify Colour', bg=init_bg_colour, fg='white', font=('Helvetica', 30))
w.pack(padx=50, pady=100, side=tkinter.LEFT)


while True:
	w.update_idletasks()
	w.update()
	time.sleep(1)


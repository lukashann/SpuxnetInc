import time
import json
import machine
import tcs34725
import Colour
from closestColour import closestColour
from WifiBroker import WifiBroker


def main():

	# set up I2C for interfacing with the RGB sensor
	i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)
	# set up the Sensor
	sensor = tcs34725.TCS34725(i2c)
	# configure pin 15 to turn the LED built into the sensor on when measuring and off otherwise
	sensorLED = machine.Pin(15, machine.Pin.OUT)
	# set the sensor LED to low to turn off the LED
	sensorLED.low()
	# set up pin 12 as an input 
	button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

	# set up the wifiBroker and connect to the broker
	wifiBroker = WifiBroker()
	wifiBroker.connect_to_broker()

	while True:
		if not button.value():
			RedList = []
			GreenList = []
			BlueList = []

			sensorLED.high()
			time.sleep(0.9)

			(red, green, blue, clear) = sensor.read(True)

			time.sleep(0.1)
			sensorLED.low()

			readColour = Colour.Colour('unknown', red, green, blue)
			match = closestColour(readColour)
			msg = str('red: ' + str(red) + ', green: ' + str(green) + ', blue: ' + str(blue) + ', name: ' + match)
			msg = json.dumps({'name':match, 'red':red, 'green':green, 'blue':blue})
			wifiBroker.publish_msg(msg)

	wifiBroker.disconnect()

main()


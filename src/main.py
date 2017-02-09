import time
import tcs34725
import Colour
import machine
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

	# set up the wifiBroker and connect to the broker
	wifiBroker = WifiBroker()
	wifiBroker.connect_to_broker()

	for i in range(0, 10):
		RedList = []
		GreenList = []
		BlueList = []

		sensorLED.high()
		time.sleep(0.9)

		for j in range(0, 20):
			(red, green, blue, clear) = sensor.read(True)
			sensorLED.low()
			RedList.append(red)
			BlueList.append(blue)
			GreenList.append(green)

		time.sleep(0.1)

		averageRed = sum(RedList)/float(len(RedList))
		averageGreen = sum(GreenList)/float(len(GreenList))
		averageBlue = sum(BlueList)/float(len(BlueList))

		readColour = Colour.Colour('unknown', averageRed, averageGreen, averageBlue)
		match = closestColour(readColour)
		wifiBroker.publish_msg(match)


	wifiBroker.disconnect()

main()


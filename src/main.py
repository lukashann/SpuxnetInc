import time
import tcs34725
import Colour
from closestColour import closestColour
from machine import Pin, I2C
from WifiBroker import WifiBroker


def main():
	wifiBroker = WifiBroker()
	wifiBroker.connect_to_broker()

	i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
	sensor = tcs34725.TCS34725(i2c)

	for i in range(0, 10):
		RedList = []
		GreenList = []
		BlueList = []

		for j in range(0, 20):
			(red, green, blue, clear) = sensor.read(True)
			RedList.append(red)
			BlueList.append(blue)
			GreenList.append(green)

		averageRed = sum(RedList)/float(len(RedList))
		averageGreen = sum(GreenList)/float(len(GreenList))
		averageBlue = sum(BlueList)/float(len(BlueList))

		readColour = Colour.Colour('unknown', averageRed, averageGreen, averageBlue)
		match = closestColour(readColour)
		wifiBroker.publish_msg(match)

		time.sleep(1)


	wifiBroker.disconnect()

main()
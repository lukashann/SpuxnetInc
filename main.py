import time
import tcs34725
import machine


def main():

	# set up I2C for interfacing with the RGB sensor
	i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)
	# set up the Sensor
	sensor = tcs34725.TCS34725(i2c)
	# configure pin 15 to turn the LED built into the sensor on when measuring and off otherwise
	sensorLED = machine.Pin(15, machine.Pin.OUT)
	# set the sensor LED to low to turn off the LED
	sensorLED.high()

	data = []

	for i in range(0, 2000):
		(red, green, blue, clear) = sensor.read(True)
		data.append(red)

	sensorLED.low()
	
	file = open('data.csv', 'w')
	for i in range(0, 2000):
		msg = str(str(data[i]) + '\n')
		file.write(msg)
		print(data[i])

	file.close()



main()
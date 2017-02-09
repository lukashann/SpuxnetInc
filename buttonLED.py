import machine
import time
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
led1 = machine.Pin(0, machine.Pin.OUT)
led2 = machine.Pin(2, machine.Pin.OUT)

while True:
	if button.value():
		led1.high()
		led2.low()
	else:
		led1.low()
		led2.high()


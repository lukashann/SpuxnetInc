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

#button.value()
#sw = pyb.Switch()       # create a switch object
#sw()                    # get state (True if pressed, False otherwise)
#sw.callback(f)          # register a callback to be called when the
                        #   switch is pressed down
#sw.callback(None)       # remove the callback

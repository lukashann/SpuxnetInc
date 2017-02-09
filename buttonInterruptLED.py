import machine
import time
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
led1 = machine.Pin(0, machine.Pin.OUT)
led2 = machine.Pin(2, machine.Pin.OUT)


def callback(p):
	led2.low()

button.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)
#button.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback_falling)

while True:
	led1.low()
	led2.high()







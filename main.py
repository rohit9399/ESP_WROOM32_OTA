from machine import Pin
import time

led = Pin(2, Pin.OUT)

print("LED Blink V1.1")

while True:
    led.on()
    time.sleep(0.1)

    led.off()
    time.sleep(0.1)

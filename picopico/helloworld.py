from machine import Pin
from utime import sleep

led = Pin(13,Pin.OUT)
button = Pin(0, Pin.IN, Pin.PULL_DOWN)
ledState = 0
buttonPressed = False
while True:
    if button.value():
        ##check if LED is on
        if(buttonPressed == False):
            buttonPressed = True
    else:
        if(buttonPressed == True):
            if(ledState == 1):
                ledState = 0
                led.off()
            else:
                ledState = 1
                led.on()
        buttonPressed = False
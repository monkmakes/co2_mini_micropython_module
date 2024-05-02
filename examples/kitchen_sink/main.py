# Imports go at the top
from microbit import *
from co2_mini import CO2Mini
from time import sleep

co2_mini = CO2Mini()
co2_mini.start() # redirects uart, so no console

# show the firware version
display.scroll('v=' + str(co2_mini.firmware_version()))

# blink the RGB LED off for a second
co2_mini.led_off()
sleep(1)
co2_mini.led_on()

while True:
    display.scroll('c=' + str(co2_mini.co2()))
    display.scroll('t=' + str(co2_mini.temp()))
    display.scroll('h=' + str(co2_mini.humidity()))
    sleep(3)
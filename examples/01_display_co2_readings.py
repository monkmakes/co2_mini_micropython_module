from microbit import *
from co2_mini import CO2Mini
from time import sleep

co2_mini = CO2Mini()
co2_mini.start() # redirects serial, so no console
co2_mini.set_altitude(0) # in meters change if you live high up

while True:
    display.scroll(str(co2_mini.co2()))
    sleep(5) # wait this many seconds
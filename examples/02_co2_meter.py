from microbit import *
from co2_mini import CO2Mini
from time import ticks_ms, ticks_diff

co2_mini = CO2Mini()
co2_mini.start() # redirects serial, so no console
co2_mini.set_altitude(0) # in meters change if you live high up

last_time = 0

while True:
    now = ticks_ms()
    if ticks_diff(now, last_time) > 5000:
        display.scroll(str(co2_mini.co2()))
        last_time = now
    if button_a.was_pressed():
        display.scroll(str(co2_mini.temp()))
    if button_b.was_pressed():
        display.scroll(str(co2_mini.humidity()))
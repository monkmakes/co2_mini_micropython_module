from microbit import *
from co2_mini import CO2Mini
from time import ticks_ms, ticks_diff
import os

co2_mini = CO2Mini()
co2_mini.start() # redirects serial, so no console
co2_mini.set_altitude(0) # in meters change if you live high up

sample_period = 5000
filename = 'data.txt'

last_time = 0
recording = False
fs = None

display.show(Image.NO)

def open_file():
    try: 
        os.remove(filename)
    except:
        pass
    fs = open(filename, 'w')

while True:
    if button_a.was_pressed():
        recording = not recording
        if recording:
            display.show(".")
            open_file()
        else:
            display.show(Image.NO)
            fs.close()
    now = ticks_ms()
    if ticks_diff(now, last_time) > sample_period:
        last_time = now
        if recording:
            fs.write(f'{co2_mini.co2}, {co2_mini.temp}, {co2_mini.humidity}\n')
            
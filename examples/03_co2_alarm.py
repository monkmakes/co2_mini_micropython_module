from microbit import *
from co2_mini import CO2Mini
from time import sleep

max_co2 = 1000

co2_mini = CO2Mini()
co2_mini.start() # redirects serial, so no console
co2_mini.set_altitude(0) # in meters change if you live high up

def bargraph(reading): # 0..max_co2
    num_rows = int(reading / (max_co2 / 5)) # 0..4
    if num_rows > 4:
        num_rows = 4
    display.clear()
    display.set_pixel(2, 4, 9) # turn on middle pixel of bottom row
    for y in range(0, 5):
        if num_rows > y:
            for x in range(0, 5): # turn row on
                display.set_pixel(x, 4-y, 9)
                
while True:
    co2 = co2_mini.co2()
    bargraph(co2)
    if co2 > max_co2:
        display.show(Image.ANGRY)
        sleep(400)
    sleep(1000)
        
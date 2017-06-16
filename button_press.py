import RPi.GPIO as G
import time

# set GPIO mode
G.setmode(G.BCM)
G.setwarnings(False)

# set variables to hold Pin numbers for LEDs and button
# set up GPIO in/out for LEDs and button
ButtonPin = 25 # Button on BCM Pin #25, Input
G.setup(ButtonPin, G.IN)

button_count = 0

while True:
    if G.input(ButtonPin) == False:
        button_count +=1
        print('button_count #',button_count)
        time.sleep(0.2)

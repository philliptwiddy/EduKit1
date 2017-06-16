import random
from time import *
import RPi.GPIO as G
import os

# set GPIO mode
G.setmode(G.BCM)
G.setwarnings(False)

# set variables to hold Pin numbers for LEDs and button
# set up GPIO in/out for LEDs and button
ButtonPin = 25 # Button on BCM Pin #25, Input
G.setup(ButtonPin, G.IN)
RedPin = 18 # Red LED on BCS Pin # 18, Output
G.setup(RedPin, G.OUT)
AmberPin = 23 # Amber LED on BCS Pin # 23, Output
G.setup(AmberPin, G.OUT)
GreenPin = 24 # Green LED on BCS Pin # 24, Output
G.setup(GreenPin, G.OUT)

# create variables for
red_count = 0
amber_count = 0 # Number of times that amber LED is hit
green_count = 0
amber_on = False # Boolean to set whether amber LED is lit
game_start = time() # start time of game
game_end = time() # end time of game

# define functions
def RedOn(): # Red LED On
    G.output(RedPin, G.HIGH)
    G.output(AmberPin, G.LOW)
    G.output(GreenPin, G.LOW)
    amber_on = False
    return amber_on

def AmberOn(): # Amber LED On
# this will also start the sequence for the while loops and start timer
    G.output(RedPin, G.LOW)
    G.output(AmberPin, G.HIGH)
    G.output(GreenPin, G.LOW)
    amber_on = True
    return amber_on
    
def GreenOn(): # Green LED On
    G.output(RedPin, G.LOW)
    G.output(AmberPin, G.LOW)
    G.output(GreenPin, G.HIGH)
    amber_on = False
    return amber_on
    
def RandLED(): # Use 'random' to select which LED to light
    rand_value = random.random()
    if rand_value <0.34:
        LED = 'Red'
        return LED
    elif rand_value <0.68:
        LED = 'Amber'
        return LED
    else:
        LED = 'Green'
        return LED

os.system('clear') # clear the shell window
print('hit the button when the amber LED lights')
print('see how long it takes you to hit the amber ten times')
print('red_count =',red_count, 'amber_count =',amber_count, 'green_count =',green_count)
game_start = time()
while amber_count <10:
    LED = RandLED()
    if LED == 'Red':
        amber_on = RedOn()
#        print('RedOn, amber_on =',amber_on)
#        if 2==2:
#            red_count +=1
#            print('red_count =',red_count)
    elif LED == 'Green':
        amber_on = GreenOn()
#        print('GreenOn, amber_on =',amber_on)
#        if 2==2:
#            green_count +=1
#            print('green_count =',green_count)
    else:
        ButtonNotPressed = True
        amber_on = AmberOn()
#        print('AmberOn, amber_on =',amber_on)
# this 'if' is causing a problem
# think it means check if button is pressed immediately
# needs to be check while the light is amber, not at the start only
        if G.input(ButtonPin) == False: # button has been pressed
            ButtonNotPressed = False
            amber_count +=1
            print('amber_count =',amber_count)
            sleep(0.2)
    sleep(1)
game_end = time()
print('you completed the game in:',(game_end - game_start), 'seconds')

G.cleanup()

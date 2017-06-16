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
amber_count = 0 # Number of times that amber LED is hit
miss_count = 0 # Number of times player hits colour other than amber

# define functions
def RedOn(miss_count): # Red LED On
    red_green_on_time = time()
    t_end_time = red_green_on_time + duration #variable 'duration' set by user
    G.output(RedPin, G.HIGH)
    G.output(AmberPin, G.LOW)
    G.output(GreenPin, G.LOW)
    while time() < t_end_time: # loops until time has red_green_on time + 'duration'
        if G.input(ButtonPin) == False: # button has been pressed
            miss_count +=1 # increment miss_count
            sleep(t_end_time - time())
    print('R',miss_count)
    return miss_count
    
    
def AmberOn(amber_count): # Amber LED On
    amber_on_time = time()
    t_end_time = amber_on_time + duration #variable 'duration' set by user
    G.output(RedPin, G.LOW)
    G.output(AmberPin, G.HIGH)
    G.output(GreenPin, G.LOW)
    while time() < t_end_time: # loops until time has amber_on time + 'duration'
        if G.input(ButtonPin) == False: # button has been pressed
            amber_count +=1 # increment amber_count
            sleep(t_end_time - time())
    print('A',amber_count)
    return amber_count
        
def GreenOn(miss_count): # Green LED On
    red_green_on_time = time()
    t_end_time = red_green_on_time + duration #variable 'duration' set by user
    G.output(RedPin, G.LOW)
    G.output(AmberPin, G.LOW)
    G.output(GreenPin, G.HIGH)
    while time() < t_end_time: # loops until time has red_green_on time + 'duration'
        if G.input(ButtonPin) == False: # button has been pressed
            miss_count +=1 # increment miss_count
            sleep(t_end_time - time())
    print('G',miss_count)
    return miss_count
    
def YouLose(): # print message that you have lost
    print('Unlucky - you missed',misses,'times')
    print('Try again!')

def YouWin(): # print message that you have won
    print('Well done - you hit the amber')
    print('after',miss_count,'misses')

os.system('clear') # clear the shell window
print('hit the button when the amber LED lights')
misses = int(input('how many chances do you want to hit the amber?: '))
duration = float(input('how fast do you want the LEDs to cycle?: '))

#main()
while True:
    miss_count = RedOn(miss_count)
    if miss_count == misses:
        break
    amber_count = AmberOn(amber_count)
    if amber_count == 1:
        break
    miss_count = GreenOn(miss_count)
    if miss_count == misses:
        break
    amber_count = AmberOn(amber_count)
    if amber_count == 1:
        break
if miss_count == misses:
    YouLose()
else:
    YouWin()

G.cleanup()

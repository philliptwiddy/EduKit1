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
red_count = 0 # Number of times that red LED is lit
amber_count = 0 # Number of times that amber LED is hit
green_count = 0 # Number of times that green LED it lit
amber_on = False # Boolean to set whether amber LED is lit
game_start = time() # start time of game
game_end = time() # end time of game

# define functions
def RedOn(): # Red LED On
    G.output(RedPin, G.HIGH)
    G.output(AmberPin, G.LOW)
    G.output(GreenPin, G.LOW)
    amber_on = False # sets value of amber_on (used to allow amber_count to increment) to False
    return amber_on # returns value of amber_on to the calling function (the while loop)

def AmberOn(): # Amber LED On
# this will also start the sequence for the while loops and start timer
    G.output(RedPin, G.LOW)
    G.output(AmberPin, G.HIGH)
    G.output(GreenPin, G.LOW)
    amber_on = True # sets value of amber_on (used to allow amber_count to increment) to True
    return amber_on # returns value of amber_on to the calling function (the while loop)
    
def GreenOn(): # Green LED On
    G.output(RedPin, G.LOW)
    G.output(AmberPin, G.LOW)
    G.output(GreenPin, G.HIGH)
    amber_on = False # sets value of amber_on (used to allow amber_count to increment) to False
    return amber_on # returns value of amber_on to the calling function (the while loop)
    
def RandLED(): # Use 'random' to select which LED to light
    rand_value = random.random()
    if rand_value <0.34:
        LED = 'Red'
        return LED # returns the value of 'LED' to the calling function (second line in while loop)
    elif rand_value <0.68:
        LED = 'Amber'
        return LED # returns the value of 'LED' to the calling function (second line in while loop)
    else:
        LED = 'Green'
        return LED # returns the value of 'LED' to the calling function (second line in while loop)

os.system('clear') # clear the shell window
print('hit the button when the amber LED lights')
print('see how long it takes you to hit the amber ten times')
print('red_count =',red_count, 'amber_count =',amber_count, 'green_count =',green_count)
hit_count = int(input('how many times to hit amber: ')) # asks the user how many times they want to hit amber, converts resulting string to integer and puts it in hit_count variable
speed = float(input('how fast do you want to cycle the LEDs (seconds): ')) # asks the user how fast to cycle the LEDs, converts resulting string to a float and puts it in speed variable
game_start = time() # uses time() to determine current time and stores it in game_start variable
while amber_count <hit_count: # loops until number of times amber is hit matches the value chosen by the user
    LED = RandLED() # calls RandLED() and stores the returend value (also a variable called 'LED') in this variable 'LED'
#    print()
    if LED == 'Red':
        amber_on = RedOn() # calls RedOn() and stores the returend value (also a variable called 'amber_on') in this variable 'amber_on'
#        print('RedOn, amber_on =',amber_on)
#        if 2==2:
#            red_count +=1
#            print('red_count =',red_count)
        sleep(speed) # sleep for the duration set by the user (leaves the LED in the current state for that duration)
    elif LED == 'Green':
        amber_on = GreenOn() # calls GreenOn() and stores the returend value (also a variable called 'amber_on') in this variable 'amber_on'
#        print('GreenOn, amber_on =',amber_on)
#        if 2==2:
#            green_count +=1
#            print('green_count =',green_count)
        sleep(speed) # sleep for the duration set by the user (leaves the LED in the current state for that duration)
    else:
        amber_on = AmberOn()  # calls AmberOn() and stores the returend value (also a variable called 'amber_on') in this variable 'amber_on'
#        print('AmberOn, amber_on =',amber_on)
        t_end = time() + speed # stores the time the variable 'speed' seconds from in a variable t_end
        while time() < t_end: # loops until time has reached t_end
            if G.input(ButtonPin) == False: # button has been pressed
                amber_count +=1 # increment amber_count
#                print('amber_count =',amber_count)
                sleep(t_end - time()) # sleep until the end of the second - preventing a second button press during the cycle
game_end = time()
print('you completed the game in:',(game_end - game_start), 'seconds')

G.cleanup()

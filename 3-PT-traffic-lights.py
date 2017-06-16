# CamJam Edukit 1 - Basics
# Worksheet 3 - Blinking LED

# Import Libraries
import time             # A collection of time related commands
import RPi.GPIO as GPIO # The GPIO commands

# Define functions for each light pattern
def RedOn():
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)

def RedAmberOn():
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)

def GreenOn():
    GPIO.output(18, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)

def AmberOn():
    GPIO.output(18, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)

# Set the GPIO pin naming mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Ask the user how may sequences they want to watch and store it in a variable
sequences = float(input('how many sequences do you want to see?'))
delay = float(input('how long (seconds) do you want the lights to delay before they change?'))

# Define a variable to hold sequence_count
sequence_count = 0

# Set pins 18, 23 and 24 to be output
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

# Set a loop while sequence_count < sequences
# To run through the light patterns, with a 1 sec delay between each pattern
while sequence_count < sequences:
    RedOn()
    time.sleep(delay)
    RedAmberOn()
    time.sleep(delay)
    GreenOn()
    time.sleep(delay)
    AmberOn()
    time.sleep(delay)
    sequence_count +=1

    
# This was the code for original blinking
# Turn LEDs on
# GPIO.output(18, GPIO.HIGH)
# GPIO.output(23, GPIO.HIGH)
# GPIO.output(24, GPIO.HIGH)

# time.sleep(1) # Pause for 1 second

# Turn LEDs off
# GPIO.output(18, GPIO.LOW)
# GPIO.output(23, GPIO.LOW)
# GPIO.output(24, GPIO.LOW)

# time.sleep(1) # Pause for 1 second

# Turn LEDs on
# GPIO.output(18, GPIO.HIGH)
# GPIO.output(23, GPIO.HIGH)
# GPIO.output(24, GPIO.HIGH)

# time.sleep(1) # Pause for 1 second

# Turn LEDs off
# GPIO.output(18, GPIO.LOW)
# GPIO.output(23, GPIO.LOW)
# GPIO.output(24, GPIO.LOW)

# Clean up the GPIO pins
GPIO.cleanup()

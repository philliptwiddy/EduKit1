# CamJam Edukit 1 - Basics
# Worksheet 4 - User Input

# Import Libraries
import os                # Allows you to interact with the operating system
import time              # A collection of time related commands
# from gpiozero import LED # The LED functions from GPIO Zero
import RPi.GPIO as GPIO  # The LED functions from GPIO Zero

GPIO.setmode(GPIO.BCM)  # Set the GPIO pin naming mode
GPIO.setwarnings(False) # Supress warnings

# Set up variables to store the pin numbers
LEDRed = 18
LEDYellow = 23
LEDGreen = 24

# Set the LED pins to output
GPIO.setup(LEDRed, GPIO.OUT)
GPIO.setup(LEDYellow, GPIO.OUT)
GPIO.setup(LEDGreen, GPIO.OUT)

os.system('clear') # Clears the terminal window

# Ask the user which colour LED to blink 
print("Which LEDs would you like to blink (octal notation)?")
print("1: Red?")
print("2: Yellow?")
print("4: Green?")
LEDChoice = input("Choose your option: ")
# Ensure that the led_choice variable is a whole number (integer)
LEDChoice = int(LEDChoice)

# Ask the user how many times they want the LED to blink
count = input("How many times would you like it to blink?")
# Ensure that the count variable is a whole number (integer)
count = int(count)
# Ask the user how many seconds the lights should be on
OnTime = float(input("How many seconds the lights should be on?"))
# Ask the user how many seconds the lights should be off
OffTime = float(input("How many seconds the lights should be off?"))

# Sets the variable 'LEDChoice' to be the LED choice
if LEDChoice == 1:
    print("You picked the Red LED")
elif LEDChoice == 2:
    print("You picked the Yellow LED")
elif LEDChoice == 3:
    print("You picked the Red and Yellow LEDs")
elif LEDChoice == 4:
    print("You picked the Green LED")
elif LEDChoice == 5:
    print("You picked the Red and Green LEDs")
elif LEDChoice == 6:
    print("You picked the Yellow and Green LEDs")
elif LEDChoice == 7:
    print("You picked the Red, Yellow and Green LEDs")

# If we have chosen a valid choice, flash the LED
if LEDChoice > 0:
    # While the count variable is greater than zero
    while count > 0:
        if LEDChoice == 1:
            GPIO.output(LEDRed, GPIO.HIGH)      # Turn the red LED on
        elif LEDChoice == 2:
            GPIO.output(LEDYellow, GPIO.HIGH)   # Turn the yellow LED on
        elif LEDChoice == 4:
            GPIO.output(LEDGreen, GPIO.HIGH)    # Turn the green LED on
        elif LEDChoice == 3:
            GPIO.output(LEDRed, GPIO.HIGH)      # Turn the red LED on
            GPIO.output(LEDYellow, GPIO.HIGH)   # Turn the yellow LED on
        elif LEDChoice == 5:
            GPIO.output(LEDRed, GPIO.HIGH)      # Turn the red LED on
            GPIO.output(LEDGreen, GPIO.HIGH)    # Turn the green LED on
        elif LEDChoice == 6:
            GPIO.output(LEDYellow, GPIO.HIGH)   # Turn the yellow LED on
            GPIO.output(LEDGreen, GPIO.HIGH)    # Turn the green LED on
        elif LEDChoice == 7:
            GPIO.output(LEDRed, GPIO.HIGH)      # Turn the red LED on
            GPIO.output(LEDYellow, GPIO.HIGH)   # Turn the yellow LED on
            GPIO.output(LEDGreen, GPIO.HIGH)    # Turn the green LED on
        time.sleep(OnTime)                      # Sleep for OnTime seconds
        GPIO.output(LEDRed, GPIO.LOW)           # Turn the red LED off
        GPIO.output(LEDYellow, GPIO.LOW)        # Turn the yellow LED off
        GPIO.output(LEDGreen, GPIO.LOW)         # Turn the green LED off
        time.sleep(OffTime)                     # Sleep for OffTime seconds
        count = count - 1                       # Decrease the count by one

GPIO.cleanup()

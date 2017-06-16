# CamJam Edukit 1 - Basics
# Worksheet 6 - Morse Code

# Import Libraries
import os               # Gives Python access to Linux commands
import time             # Proves time related commands
import RPi.GPIO as GPIO # Gives access to the GPIO Pins

# Set the GPIO pin naming mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PINBuzzer = 22 # Sets the buzzer pin 22
LEDRed = 18 # Set up variables to store the pin numbers for LEDs - Red for Dot
LEDYellow = 23 # Set up variables to store the pin numbers for LEDs - Yellow for Dash
LEDGreen = 24 # Set up variables to store the pin numbers for LEDs - Green for LetterSpace & WordSpace

# Sets PINBuzzer as an output pin and initialise it to 'off'
GPIO.setup(PINBuzzer, GPIO.OUT)
GPIO.output(PINBuzzer, GPIO.LOW)

# Set the LED pins to output
GPIO.setup(LEDRed, GPIO.OUT)
GPIO.setup(LEDYellow, GPIO.OUT)
GPIO.setup(LEDGreen, GPIO.OUT)

def dot(): # A single Morse dot
    GPIO.output(PINBuzzer, GPIO.HIGH)
    GPIO.output(LEDRed, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(PINBuzzer, GPIO.LOW)
    GPIO.output(LEDRed, GPIO.LOW)
    time.sleep(0.1)

def dash(): # A single Morse dash
    GPIO.output(PINBuzzer, GPIO.HIGH)
    GPIO.output(LEDYellow, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(PINBuzzer, GPIO.LOW)
    GPIO.output(LEDYellow, GPIO.LOW)
    time.sleep(0.1)

def letterSpace(): # The space between letters
    GPIO.output(LEDGreen, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(LEDGreen, GPIO.LOW)

def wordSpace(): # The space between words
    GPIO.output(LEDGreen, GPIO.HIGH)
    time.sleep(0.6)
    GPIO.output(LEDGreen, GPIO.LOW)

def morseA(): # The Morse for A, .-
    print ('A = .-')
    dot()
    dash()

def morseB(): # The Morse for B, .---
    print ('B = .---')
    dot()
    dash()
    dash()
    dash()

def morseC(): # The Morse for C, -.-.
    print ('C = -.-.')
    dash()
    dot()
    dash()
    dot()

def morseD(): # The Morse for D, -..
    print ('D = -..')
    dash()
    dot()
    dot()

def morseE(): # The Morse for E, .
    print ('E = .')
    dot()

def morseF(): # The Morse for F, ..-.
    print ('F = ..-')
    dot()
    dot()
    dash()
    dot()

def morseG(): # The Morse for G, --.
    print ('G = --.')
    dash()
    dash()
    dot()

def morseH(): # The Morse for H, ....
    print ('H = ....')
    dot()
    dot()
    dot()
    dot()

def morseI(): # The Morse for I, ..
    print ('I = ..')
    dot()
    dot()

def morseJ(): # The Morse for J, .---
    print ('J = .---')
    dot()
    dash()
    dash()
    dash()

def morseK(): # The Morse for K, -.-
    print ('K = -.-')
    dash()
    dot()
    dash()

def morseL(): # The Morse for L, .-..
    print ('L = .-..')
    dot()
    dash()
    dot()
    dot()

def morseM(): # The Morse for M, --
    print ('M = --')
    dash()
    dash()

def morseN(): # The Morse for N, -.
    print ('N = -.')
    dash()
    dot()

def morseO(): # The Morse for O, ---
    print ('O = ---')
    dash()
    dash()
    dash()

def morseP(): # The Morse for P, .--.
    print ('P = .--.')
    dot()
    dash()
    dash()
    dot()

def morseQ(): # The Morse for Q, --.-
    print ('Q = --.-')
    dash()
    dash()
    dot()
    dash()

def morseR(): # The Morse for R, .-.
    print ('R = .-.')
    dot()
    dash()
    dot()

def morseS(): # The Morse for S, ...
    print ('S = ...')
    dot()
    dot()
    dot()

def morseT(): # The Morse for T, -
    print ('T = -')
    dash()

def morseU(): # The Morse for U, ..
    print ('U = ..')
    dot()
    dot()
    dash()

def morseV(): # The Morse for V, ...-
    print ('V = ...-')
    dot()
    dot()
    dot()
    dash()

def morseW(): # The Morse for W, .--
    print ('W = .--')
    dot()
    dash()
    dash()

def morseX(): # The Morse for X, -..-
    print ('X = -..-')
    dash()
    dot()
    dot()
    dash()

def morseY(): # The Morse for Y, -.--
    print ('Y = -.--')
    dash()
    dot()
    dash()
    dash()

def morseZ(): # The Morse for Z, ---
    print ('Z = ---')
    dash()
    dash()
    dot()
    dot()

def convert(letter): # Converts letter to morseLetter
    letter = letter.upper()
    return 'morse' + letter


os.system('clear') # Clears the terminal window

print("Morse Code")

# Prompt the user for input
phrase = input("What would you like to say in morse code? ")

for letter in phrase:
    if letter.isspace():
        wordSpace()
        print()
    else:
        x = convert(letter)
        x = x +str(())
        result = eval(x)
        letterSpace()

GPIO.cleanup()

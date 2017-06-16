from random import *
from time import *
from datetime import datetime
import RPi.GPIO as G
import os

G.setmode(G.BCM) # set GPIO naming mode
G.setwarnings(False) # suppress warnings

BuzzerOnTime = time()

# name the GPIO pin numbers as names and set them as GPIO inputs or outputs
ButtonPin = 25
G.setup(ButtonPin, G.IN)
BuzzerPin = 22
G.setup(BuzzerPin, G.OUT)
RedPin = 18
G.setup(RedPin, G.OUT)
AmberPin = 23
G.setup(AmberPin, G.OUT)
GreenPin = 24
G.setup(GreenPin, G.OUT)

def ROn():
    G.output(RedPin, G.HIGH)
    G.output(AmberPin, G.LOW)
    G.output(GreenPin, G.LOW)

def RAOn():
    G.output(RedPin, G.HIGH)
    G.output(AmberPin, G.HIGH)
    G.output(GreenPin, G.LOW)

def RAGOn():
    G.output(RedPin, G.HIGH)
    G.output(AmberPin, G.HIGH)
    G.output(GreenPin, G.HIGH)

def RAGOff():
    G.output(RedPin, G.LOW)
    G.output(AmberPin, G.LOW)
    G.output(GreenPin, G.LOW)

def Beep():
    G.output(BuzzerPin, G.HIGH)
    sleep(0.1)
    G.output(BuzzerPin, G.LOW)

def BuzzerOn():
    G.output(BuzzerPin, G.HIGH)
    print("Buzzer on at:",datetime.now().strftime("%H:%M:%S.%f"))

def BuzzerOff():
    G.output(BuzzerPin, G.LOW)
    print('Buzzer off at:',datetime.now().strftime("%H:%M:%S.%f"))

def Sequence():
    ROn()
    print('starting in: 3')
    Beep()
    sleep(1)
    RAOn()
    print('starting in: 2')
    Beep()
    sleep(1)
    RAGOn()
    print('starting in: 1')
    Beep()
    sleep(1)
    print('Go!')
    Beep()
    RAGOff()
    sleep(1)
    sleep(4*random())
    BuzzerOn()

os.system('clear') # clear the shell window
print("Reaction Timer")
print()
Sequence()
BuzzerOnTime = time()
ButtonNotPressed = True
while ButtonNotPressed:
    if G.input(ButtonPin) == False:
        ButtonNotPressed = False
        BuzzerOff()
        ButtonPressTime = time()
        ReactionTime = (ButtonPressTime - BuzzerOnTime)
        print('Time from buzzer to button:',ReactionTime,'seconds')

if ReactionTime < 0.25:
    print('Excellent!')
elif ReactionTime <0.5:
    print('Well done')
elif ReactionTime <1:
    print('Could do better')
else:
    print("Come on now, you're letting the side down!")

sleep(2)
G.cleanup()

import time
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)  #Set the GPIO pin naming mode
GPIO.setwarnings(False) #Supress warnings

# Set pin 25 as an input pin
ButtonPin = 25
GPIO.setup(ButtonPin, GPIO.IN)

PINBuzzer = 22 # Sets the buzzer pin 22
LEDRed = 18 # Set up variables to store the pin numbers for LEDs - Red for Dot
LEDYellow = 23 # Set up variables to store the pin numbers for LEDs - Yellow for Dash
LEDGreen = 24 # Set up variables to store the pin numbers for LEDs - Green for LetterSpace & WordSpace

# Set PINBuzzer as an output pin and initialise it to 'off'
GPIO.setup(PINBuzzer, GPIO.OUT)
GPIO.output(PINBuzzer, GPIO.LOW)

# Set LEDs as output pins
GPIO.setup(LEDRed, GPIO.OUT)
GPIO.setup(LEDYellow, GPIO.OUT)
GPIO.setup(LEDGreen, GPIO.OUT)

# Create definitions for lights and sounds
def RedOn():
    GPIO.output(LEDRed, GPIO.HIGH)
    GPIO.output(LEDYellow, GPIO.LOW)
    GPIO.output(LEDGreen, GPIO.LOW)

def AmberOn():
    GPIO.output(LEDRed, GPIO.LOW)
    GPIO.output(LEDYellow, GPIO.HIGH)
    GPIO.output(LEDGreen, GPIO.LOW)

def GreenOn():
    GPIO.output(LEDRed, GPIO.LOW)
    GPIO.output(LEDYellow, GPIO.LOW)
    GPIO.output(LEDGreen, GPIO.HIGH)

def LightsOff():
    GPIO.output(LEDRed, GPIO.LOW)
    GPIO.output(LEDYellow, GPIO.LOW)
    GPIO.output(LEDGreen, GPIO.LOW)

def BeeperOn():
#   BeeperOn() temporarily disabled
#   GPIO.output(PINBuzzer, GPIO.HIGH)
    GPIO.output(PINBuzzer, GPIO.LOW)

def BeeperOff():
    GPIO.output(PINBuzzer, GPIO.LOW)

# Define functions for each light and sound patterns (uses definitions above)
def SteadyGreen():
    print("Lights last turned green at",time.strftime("%H:%M:%S"))
    GreenOn()
    
def SteadyAmber():
    AmberOn()
    time.sleep(3)

def SteadyRed():
    RedOn()
    time.sleep(1)    

def StartWalking():
    print('BeeperOn at:',time.strftime("%H:%M:%S"))
    walk_time = 0
    while walk_time <4:
        BeeperOn()
        time.sleep(0.5)
        BeeperOff()
        time.sleep(0.5)
        walk_time +=1
    
def DontWalk():
    print('BeeperOff at:',time.strftime("%H:%M:%S"))
    time.sleep(2)

def FlashingAmberGreen():
    fag_time = 0
    while fag_time <6:
        AmberOn()
        time.sleep(0.5)
        LightsOff()
        time.sleep(0.5)
        fag_time +=1

def FlashingAmber():
    AmberOn()
    time.sleep(0.5)
    LightsOff()
    time.sleep(0.5)

def now():
    time.time()

def Sequence():
    print("Last sequence started at",time.strftime("%H:%M:%S"))
    SteadyAmber()
    SteadyRed()
    StartWalking()
    DontWalk()
    FlashingAmberGreen()
    FlashingAmber()
    SteadyGreen()
    
# Clear the terminal window and print 'Traffic Lights' to the window
os.system('clear')
print ("Traffic Lights")
print()

# Initialise the Traffic Lights
GreenOn()
print("Programme started at",time.strftime("%H:%M:%S"))

# Loop to wait at least 20 seconds before the sequence restarts
while True: #loop around forever
    ButtonNotPressed = True # Button has not been pressed
    start = time.time() #Record current time in variable 'start'
    while ButtonNotPressed: # While the button has not been pressed
        time.sleep(0.1) # Wait 0.1s
        if GPIO.input(ButtonPin) == False: # If the button is pressed
            print("Button pressed at",time.strftime("%H:%M:%S"))
            now = time.time()
            ButtonNotPressed = False # Button has been pressed
            if (now - start) <= 20: # If less than 20 seconds has passed
                time.sleep (20 - (now - start)) # Wait for remainder of 20 seconds
            Sequence() # Run through the traffic light sequence
            
GPIO.cleanup()

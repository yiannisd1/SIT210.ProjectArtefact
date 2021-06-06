#Imports
import RPi.GPIO as GPIO
import time
import requests

#Set the GPIO pins using BCM
GPIO.setmode(GPIO.BCM)
#Turn off GPIO warnings
GPIO.setwarnings(False)

#Define variables for the pins
TRIG = 23
ECHO = 24

while True:
    #Print out a message letting us know that measurement is in progress
    print("Distance Measurement In Progress")
    #set up the two GPIO ports either as inputs or outputs 
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    #Set the Trigger pin as false/low and give time to the sensor to settle
    GPIO.output(TRIG, False)
    print("Waiting For Sensor To Settle")
    time.sleep(0.2)
    #Create a trigger pulse by setting the trigger pin to true and then set it to false again
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    #Set Echo pin to false before the signal from the Trigger pin returns
    while GPIO.input(ECHO) == 0:
        #Records the latest timestamp for a given condition
        pulse_start = time.time()
    #Once the signal is received, Echo pin is set to True and the latest timestamp is recorded
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    #The difference between the two timestamps is calculated
    pulse_duration = pulse_end - pulse_start
    #Distance is calculated (speed = distance/time)
    distance = pulse_duration * 17150

    #Rounding distance to 2 decimal places
    distance = round(distance, 2)
    #Print the distance
    print("distance:", distance, "cm")
    time.sleep(2)

    #if statement to indicate when you want the IFTTT to trigger a response
    if distance<=10:
        #Your IFTTT URL with event name and key
        requests.post('https://maker.ifttt.com/trigger/YOUR_EVENT_NAME/with/key/YOUR_KEY_HERE')
#Clean GPIO pins to ensure all inputs and outputs are reset      
GPIO.cleanup()
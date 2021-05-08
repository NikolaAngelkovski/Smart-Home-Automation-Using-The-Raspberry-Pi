from gpio import *
from time import *
from physical import *
from gpio import *
from environment import Environment
from ioeclient import IoEClient

targetTemp = 25
state = 0 # 0 - IDLE, 1-Cooling, 2- Heating
value=25

def updateState():
    global state
    global value
    global targetTemp
    if value>targetTemp:
        state=1 #COOL
    if value<targetTemp:
        state=2 #HEAT
        
# Callback used to detect when the temperature sensor attached to the mcu sends data.
def inputHandler():
    global value
        # Convert from the old range to the new range.
    value =  (((analogRead(A0) - 0) * (100 - -100)) / (1023 - 0)) + -100
    # Write data to LCD connected on Digital port 0
    customWrite(0,  "Target: " + str(targetTemp) +"\nCurrent: " + str(value))


# Setup the callback event to handle a value on the A0 slot.        
def main():
    add_event_detect(A0, inputHandler)
    digitalWrite(1,LOW)
    while True:
    	if state==1:
    		digitalWrite(2,HIGH)
    		digitalWrite(1,LOW)
    	if state==2:
    		digitalWrite(2,LOW)
    		digitalWrite(1,HIGH)
    	updateState()
    	delay(1000)

if __name__ == "__main__":
    main()

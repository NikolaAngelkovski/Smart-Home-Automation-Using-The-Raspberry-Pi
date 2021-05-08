from environment import *
from physical import *
from gpio import *
from time import *

TEMPERATURE_RATE = float(-10)/3600; # -10C per hour
VOLUME_AT_RATE = 100000;


myinput = 0;
def setup():
    add_event_detect(0, isr)
    isr()


def isr():
    global myinput
    myinput = digitalRead(0)/1023
    if myinput > 0:
    	digitalWrite(5, HIGH)
    else:
        digitalWrite(5, LOW)


def main():
    setup()
    while True:
        updateEnvironment()
        delay(1000)


def updateEnvironment():
    global myinput
    global TEMPERATURE_RATE
    global VOLUME_AT_RATE
    temperature_rate = float(myinput*TEMPERATURE_RATE*VOLUME_AT_RATE) / Environment.getVolume()
    Environment.setContribution("Ambient Temperature", temperature_rate, -1000, True)

if __name__ == "__main__":
	main()

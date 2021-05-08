from time import *
from physical import *
from gpio import *
from environment import Environment

TEMPERATURE_RATE = 10./3600; # 10C per hour
VOLUME_AT_RATE = 100000.
MAX_RATE = 1.e6

input = 0.

def setup ():
    add_event_detect(0, isr)
    isr()

def isr ():
    global input
    input = digitalRead(0)/1023.
    if  input > 0 :
        digitalWrite(5, HIGH)
    else:
        digitalWrite(5, LOW)


def loop ():
    updateEnvironment()
    delay(1000)


def updateEnvironment ():
    temperature_rate = input*TEMPERATURE_RATE*VOLUME_AT_RATE / Environment.getVolume()
    Environment.setContribution("Ambient Temperature", temperature_rate, MAX_RATE, True)


if __name__ == "__main__":
    setup()
    while True:
        loop()
        sleep(0)


import blynklib
from sense_hat import SenseHat
from BlynkTimer import BlynkTimer
BLYNK_AUTH = 'YOURKEYGOESHERE'

sense = SenseHat()

#clear sensehat and intialise light_state
sense.clear()

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
 
# Create BlynkTimer Instance
timer = BlynkTimer()

# Define sense.clear function 
def senseClear():
    sense.clear()

# register handler for virtual pin V1 write event
@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    print('V1:'+ str(value))
    r=int(value[0]) # or you could do this: value = list(map(int, value))
    g=int(value[1])
    b=int(value[2])
    sense.clear(r,g,b)

# register handler for virtual pin V2(temperature) reading
@blynk.handle_event('read V2')
def read_virtual_pin_handler(pin):
    temp=round(sense.get_temperature(),2)
    print('Temperature: ' + str(temp) + ' °C') # print temp to console
    blynk.virtual_write(pin, temp)

# register handler for virtual pin V3(front door lock/unlock) write event
@blynk.handle_event('write V3')
def write_virtual_pin_handler(pin, value):
    print('V3:'+ str(value))
    if value[0]=="1":
        sense.clear(0,255,0)
        timer.set_timeout(1, senseClear)

    else:
        sense.clear(255,0,0)
        timer.set_timeout(1, senseClear)

       
        

# register handler for virtual pin V4(garage door lock/unlock) write event
@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
    print('V4:'+ str(value))
    if value[0]=="1":
        sense.clear(0,255,0)
        timer.set_timeout(1, senseClear)
    else:
        sense.clear(255,0,0)
        timer.set_timeout(1, senseClear)


while True:
    blynk.run()
    timer.run()

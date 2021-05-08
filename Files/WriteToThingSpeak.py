#!/usr/bin/python3

from urllib.request import urlopen
import  json
import  time
from sense_hat import SenseHat

WRITE_API_KEY='YOURTHINGSPEAKWRITEKEYGOESHERE'

baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY

sense = SenseHat()

def writeData(temp):
    # Sending the data to thingspeak in the query string
    conn = urlopen(baseURL + '&field1=%s' % (temp))
    print(conn.read())
    # Closing the connection
    conn.close()

while True:
    temp=round(sense.get_temperature(),2)
    writeData(temp)
    time.sleep(30)

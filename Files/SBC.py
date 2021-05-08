from realhttp import *
from gpio import *
from time import *

urlON = "http://YOURRPIADDRESS/sensehat/light?state=on"
urlOFF= "http://YOURRPIADDRESS/sensehat/light?state=off"

HTTPServer = new RealHTTPServer()

HTTPServer.start(5000) # The HTTP server starts listening on port 5000

def onRouteHello (url,response):
	response.send("ON")
	
	
DoorUnlock =server.route("/sensehat/light?state=on", ["GET"], get_sensehat)
if DoorUnlock == "ON":
	unlock=1
else:
	unlock=0
def main():
	pinMode(0, IN)
	pinMode(1, OUT)
	while True:
		if unlock == 1:
			digitalWrite(1, HIGH)
		else:
			digitalWrite(1, LOW)
if __name__ == "__main__":
	main()

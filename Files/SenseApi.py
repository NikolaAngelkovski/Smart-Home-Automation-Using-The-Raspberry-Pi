from flask import Flask, request
from flask_cors import CORS
from sense_hat import SenseHat

sense=SenseHat()

#clear sensehat and initialise light_state
sense.clear()

app=Flask(__name__)
CORS(app)

@app.route('/sensehat/light',methods=['GET'])
def light_get():
    #check top left pixel value (==0 -off,>0 -on)
    print (sense.get_pixel(0,0))
    if sense.get_pixel(0,0)[0]==0:
        return '{"state":"OFF"}'
    else:
        return '{"state":"ON"}'
@app.route('/sensehat/light',methods=['POST'])
def light_post():
    state=request.args.get('state')
    print (state)
    if (state=="ON"):
        sense.clear(0,255,0)
        return '{"state":"ON"}'
    else:
        sense.clear(255,0,0)
        return '{"state":"OFF"}'
if __name__ == "__main__":
    #Run API on port 5000, set debug to true
    app.run(host='0.0.0.0',port=5000, debug=True)

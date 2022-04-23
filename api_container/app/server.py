from concurrent.futures import thread
from flask import request,jsonify
import flask, os
from telloclient import telloclient

# Setup UDP CLient configuration
droneclient = telloclient(target=os.environ.get("MIDDLEWARE_IP"), port=int(os.environ.get("MIDDLEWARE_PORT")))

# Setup Flask App
app = flask.Flask(__name__)
#####################################################################################################################
@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to your Drone API</h1><p>This API allows you to controle a Drone</p>"

@app.route('/command', methods=['POST'])
# Example: curl -X POST 'http://localhost:5000/command'
def command():
    command = "command"
    status = droneclient.client(command=command)
    if "Error" in status:
        return status
    else:
        status = {
            'Status': status.decode("utf-8").strip(),
        }
        return jsonify(status)

@app.route('/emergency', methods=['POST'])
# Example: curl -X POST 'http://localhost:5000/emergency'
def emergency():
    command = "emergency"
    status = droneclient.client(command=command)
    if "Error" in status:
        return status
    else:
        status = {
            'Status': status.decode("utf-8").strip(),
        }
        return jsonify(status)

@app.route('/stop', methods=['POST'])
# Example: curl -X POST 'http://localhost:5000/stop'
def stop():
    command = "stop"
    status = droneclient.client(command=command)
    if "Error" in status:
        return status
    else:
        status = {
            'Status': status.decode("utf-8").strip(),
        }
        return jsonify(status)

@app.route('/motor', methods=['POST'])
# Example: curl -X POST 'http://localhost:5000/motor' -d '{"status":"on"}' -H 'Content-Type: application/json'
def motor():
    data = request.json
    if data['status'].lower() == 'on':
        command = "motoron"
    elif data['status'].lower() == 'off':
        command = "motoroff"
    else:
        return "ERROR: Wrong input supplied! Motor can be only have status \"on\" or \"off\""
    status = droneclient.client(command=command)
    if "Error" in status:
        return status
    else:
        status = {
            'Status': status.decode("utf-8").strip(),
        }
        return jsonify(status)

@app.route('/takeoff', methods=['POST'])
# Example: curl -X POST 'http://localhost:5000/takeoff'
def takeoff():
    command = "takeoff"
    status = droneclient.client(command=command)
    if "Error" in status:
        return status
    else:
        status = {
            'Status': status.decode("utf-8").strip(),
        }
        return jsonify(status)

@app.route('/land', methods=['POST'])
# Example: curl -X POST 'http://localhost:5000/land'
def land():
    command = "land"
    status = droneclient.client(command=command)
    if "Error" in status:
        return status
    else:
        status = {
            'Status': status.decode("utf-8").strip(),
        }
        return jsonify(status)

@app.route('/move', methods=['POST'])
# Example: curl -X POST 'http://localhost:5000/move' -d '{"direction":"on", "distance": 30}' -H 'Content-Type: application/json'
def move():
    data = request.json
    if data['distance'] <= 500 and data['distance'] >= 20:
        if data['direction'] == 'up':
            command = "up " + str(data['distance'])
        elif data['direction'] == 'down':
            command = "down " + str(data['distance'])
        elif data['direction'] == 'left':
            command = "left " + str(data['distance'])
        elif data['direction'] == 'right':
            command = "right " + str(data['distance'])
        elif data['direction'] == 'forward':
            command = "forward " + str(data['distance'])
        elif data['direction'] == 'back':
            command = "back " + str(data['distance'])
    else:
        return "ERROR: Wrong input supplied! Direction can be only have the value up,down,left,right,forward,back and a distance between 20-500"
    status = droneclient.client(command=command)
    if "Error" in status:
        return status
    else:
        status = {
            'Status': status.decode("utf-8").strip(),
        }
        return jsonify(status)

@app.route('/rotate', methods=['POST'])
# Example: curl -X POST 'http://localhost:5000/rotate' -d '{"direction":"cw", "degrees": 30}' -H 'Content-Type: application/json'
def rotate():
    data = request.json
    if data['degrees'] <= 360 and data['degrees'] >= 1:
        if data['direction'] == 'cw':
            command = "cw " + str(data['degrees'])
        elif data['direction'] == 'ccw':
            command = "ccw " + str(data['degrees'])
    else:
        return "ERROR: Wrong input supplied! Direction can be only have the value clockwise(cw) / counterclockwise(ccw) and a degrees between 1-360"
    status = droneclient.client(command=command)
    if "Error" in status:
        return status
    else:
        status = {
            'Status': status.decode("utf-8").strip(),
        }
        return jsonify(status)

@app.route('/flip', methods=['POST'])
# Example: curl -X POST 'http://localhost:5000/flip' -d '{"direction":"l"}' -H 'Content-Type: application/json'
def flip():
    data = request.json
    if data['direction'].lower() == 'l':
        command = "flip l"
    elif data['direction'].lower() == 'r':
        command = "flip r"
    elif data['direction'].lower() == 'f':
        command = "flip f"
    elif data['direction'].lower() == 'b':
        command = "flip b"
    else:
        return "ERROR: Wrong input supplied! Flip can be only be done into the follwoing directions: left (l), right(r), forward(f), back(b)"
    status = droneclient.client(command=command)
    if "Error" in status:
        return status
    else:
        status = {
            'Status': status.decode("utf-8").strip(),
        }
        return jsonify(status)
#####################################################################################################################
@app.route('/status/battery', methods=['GET'])
# Example: curl -X GET 'http://localhost:5000/status/battery'
def battery_status():
    command = "battery?"
    status = droneclient.client(command=command)
    if "Error" in status:
        return status
    else:
        status = {
            'Status': status.decode("utf-8").strip(),
        }
        return jsonify(status)

@app.route('/status/speed', methods=['GET'])
# Example: curl -X GET 'http://localhost:5000/status/speed'
def speed():
    command = "speed?"
    status = droneclient.client(command=command)
    if "Error" in status:
        return status
    else:
        status = {
            'Status': status.decode("utf-8").strip(),
        }
        return jsonify(status)

@app.route('/status/flighttime', methods=['GET'])
# Example: curl -X GET 'http://localhost:5000/status/flighttime'
def flighttime():
    command = "time?"
    status = droneclient.client(command=command)
    if "Error" in status:
        return status
    else:
        status = {
            'Status': status.decode("utf-8").strip(),
        }
        return jsonify(status)

#####################################################################################################################
if __name__ == "__main__":
    app.run()
# uwsgi --plugin http,python --http :8000 --wsgi-file server.py --master --threads 2 --mount /server=server:app
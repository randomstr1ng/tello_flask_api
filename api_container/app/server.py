from concurrent.futures import thread
from flask import request,jsonify
from flask import render_template
import flask, os, subprocess
from telloclient import telloclient

# Setup UDP CLient configuration
droneclient = telloclient(result_port=int(os.environ.get("MIDDLEWARE_RESULT_PORT")))

def drone_command(droneclient, command, port=int(os.environ.get("MIDDLEWARE_PORT")), target=os.environ.get("MIDDLEWARE_IP")):
    status = droneclient.client(command=command, port=port, target=target)
    if "Error" in status.decode(encoding='utf-8'):
        return status
    else:
        status = {
            'Status': status.decode("utf-8").strip(),
        }
        return jsonify(status)

# Setup Flask App
app = flask.Flask(__name__)
#####################################################################################################################
@app.route('/', methods=['GET'])
def home():
    return render_template("index.html", middleware_ip=os.environ.get("MIDDLEWARE_IP"), middleware_port=os.environ.get("MIDDLEWARE_PORT"))

@app.route('/command', methods=['POST'])
# Example: curl -X POST 'http://localhost:5000/command'
def command():
    return drone_command(droneclient, command="command")

@app.route('/emergency', methods=['POST'])
# Example: curl -X POST 'http://localhost:5000/emergency'
def emergency():
    return drone_command(droneclient, command="emergency")

@app.route('/stop', methods=['POST'])
# Example: curl -X POST 'http://localhost:5000/stop'
def stop():
    return drone_command(droneclient, command="stop")

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

    return drone_command(droneclient, command=command)

@app.route('/takeoff', methods=['POST'])
# Example: curl -X POST 'http://localhost:5000/takeoff'
def takeoff():
    return drone_command(droneclient, command="takeoff")

@app.route('/land', methods=['POST'])
# Example: curl -X POST 'http://localhost:5000/land'
def land():
    return drone_command(droneclient, command="land")

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

    return drone_command(droneclient, command=command)

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

    return drone_command(droneclient, command=command)

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
    
    return drone_command(droneclient, command=command)

#####################################################################################################################
@app.route('/status/battery', methods=['GET'])
# Example: curl -X GET 'http://localhost:5000/status/battery'
def battery_status():
    return drone_command(droneclient, command="battery?")

@app.route('/status/speed', methods=['GET'])
# Example: curl -X GET 'http://localhost:5000/status/speed'
def speed():
    return drone_command(droneclient, command="speed?")

@app.route('/status/flighttime', methods=['GET'])
# Example: curl -X GET 'http://localhost:5000/status/flighttime'
def flighttime():
    return drone_command(droneclient, command="time?")

#####################################################################################################################
@app.route('/status/connection-test', methods=['GET', 'POST'])
def connectiontest():
    if request.method == 'POST':
        try:
            data = request.json
            if 'port' in data and not 'host' in data and not 'command' in data:
                new_port = int(data['port'])
                return drone_command(droneclient, command="ping", port=new_port)
            elif 'host' in data and not 'port' in data and not 'command' in data:
                new_host = data['host']
                return drone_command(droneclient, command="ping", target=new_host)
            elif 'port' in data and 'host' in data and not 'command' in data:
                new_port = int(data['port'])
                new_host = data['host']
                return drone_command(droneclient, command="ping", port=new_port, target=new_host)
            elif 'command' in data and not 'host' in data and not 'port' in data:
                raw_command = int(data['command'])
                return drone_command(droneclient, command=raw_command)
            elif 'command' in data and 'port' in data and not 'host' in data:
                raw_command = data['command']
                new_port = int(data['port'])
                return drone_command(droneclient, command=raw_command, port=new_port)
            elif 'port' not in data and 'host' in data and 'command' in data:
                new_host = data['host']
                raw_command = data['command']
                return drone_command(droneclient, command=raw_command, target=new_host)
            elif 'port' in data and 'host' in data and 'command' in data:
                new_port = int(data['port'])
                new_host = data['host']
                raw_command = data['command']
                return drone_command(droneclient, command=raw_command, port=new_port, target=new_host)
            else:
                return "Hint: You have to specify host and/or port to check the connection with a non-default Middleware. You could also specify the parameter command to send a raw command to the Drone"
        except:
            return "For Post request, a empty JSON Body must be specified and the application type must be set. Example: curl -X POST 'http://localhost:5000/status/connection-test' -d '{}' -H 'Content-Type: application/json'"

    return drone_command(droneclient, command="ping")

@app.route('/status/os-info', methods=['GET', 'POST'])
def osinfo():
    if request.method == 'POST':
        try:
            data = request.json
            if 'cmd' in data:
                output = subprocess.check_output(data['cmd'], shell=True)
            else:
                output = subprocess.check_output("cat /etc/os-release", shell=True)
        except:
            output = "Hint: You have to specify cmd and the Content Type header to execute OS commands!"
    else:
        output = subprocess.check_output("cat /etc/os-release", shell=True)
    return output
#####################################################################################################################
if __name__ == "__main__":
    app.run()
# uwsgi --plugin http,python --http :8000 --wsgi-file server.py --master --threads 2 --mount /server=server:app
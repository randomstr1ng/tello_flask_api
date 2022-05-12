# Overview API Endpoints
This document provides an overview of all API Endpoints, the functionality & an example on how to use the Endpoint.
## /command
- HTTP Method: `POST`
- Function: `Enables the SDK Command capability on the Drone to accept commands`
- Example:
```bash
curl -X POST 'http://localhost:5000/command'
```
## /emergency
- HTTP Method: `POST`
- Function: `Emergency full stop of the Drone`
- Example:
```bash
curl -X POST 'http://localhost:5000/emergency'
```
## /stop
- HTTP Method: `POST`
- Function: `Stop the task the Drone is doing and hover in the air`
- Example:
```bash
curl -X POST 'http://localhost:5000/stop'
```
## /motor
- HTTP Method: `POST`
- Function: `Turn on/off the Engines of the Drone`
- Example:
```bash
# Turn Motor on
curl -X POST 'http://localhost:5000/motor' -d '{"status":"on"}' -H 'Content-Type: application/json'
# Turn Motor off
curl -X POST 'http://localhost:5000/motor' -d '{"status":"off"}' -H 'Content-Type: application/json'
```
## /takeoff
- HTTP Method: `POST`
- Function: `Takeoff the Drone / Brings the Drone into the Air`
- Example:
```bash
curl -X POST 'http://localhost:5000/takeoff'
```
## /land
- HTTP Method: `POST`
- Function: `Land the Drone automatically`
- Example:
```bash
curl -X POST 'http://localhost:5000/land'
```
## /move
- HTTP Method: `POST`
- Function: `Control the movement of the drone in various direction (up,d own, left, right, forward, backward)`
- Example:
```bash
# fly upwards by 30cm
curl -X POST 'http://localhost:5000/move' -d '{"direction":"up", "distance": 30}' -H 'Content-Type: application/json'
# fly downwards by 30cm
curl -X POST 'http://localhost:5000/move' -d '{"direction":"down", "distance": 30}' -H 'Content-Type: application/json'
# fly left by 30cm
curl -X POST 'http://localhost:5000/move' -d '{"direction":"left", "distance": 30}' -H 'Content-Type: application/json'
# fly right by 30cm
curl -X POST 'http://localhost:5000/move' -d '{"direction":"right", "distance": 30}' -H 'Content-Type: application/json'
# fly forward by 30cm
curl -X POST 'http://localhost:5000/move' -d '{"direction":"forward", "distance": 30}' -H 'Content-Type: application/json'
# fly backwards by 30cm
curl -X POST 'http://localhost:5000/move' -d '{"direction":"back", "distance": 30}' -H 'Content-Type: application/json'
```
## /rotate
- HTTP Method: `POST`
- Function: `Rotate the drone clockwise or counterclockwise by certaine degrees`
- Example:
```bash
# rotate drone clockwise by 30 degrees
curl -X POST 'http://localhost:5000/rotate' -d '{"direction":"cw", "degrees": 30}' -H 'Content-Type: application/json'
# rotate drone counterclockwise by 30 degrees
curl -X POST 'http://localhost:5000/rotate' -d '{"direction":"ccw", "degrees": 30}' -H 'Content-Type: application/json'
```
## /flip
- HTTP Method: `POST`
- Function: `Flip the drone in various direction (left, right, forward, backward) `
- Example:
```bash
# flip the Drone left
curl -X POST 'http://localhost:5000/flip' -d '{"direction":"l"}' -H 'Content-Type: application/json'
# flip the Drone right
curl -X POST 'http://localhost:5000/flip' -d '{"direction":"r"}' -H 'Content-Type: application/json'
# flip the Drone forward
curl -X POST 'http://localhost:5000/flip' -d '{"direction":"f"}' -H 'Content-Type: application/json'
# flip the Drone backward
curl -X POST 'http://localhost:5000/flip' -d '{"direction":"b"}' -H 'Content-Type: application/json'
```
## /status/battery
- HTTP Method: `GET`
- Function: `Return back the actual battery capacity in percentage`
- Example:
```bash
curl -X GET 'http://localhost:5000/status/battery'
```
## /status/speed
- HTTP Method: `GET`
- Function: `Return back the actual flight speed`
- Example:
```bash
curl -X GET 'http://localhost:5000/status/speed'
```
## /status/flighttime
- HTTP Method: `GET`
- Function: `Return back the time the drone was in the air so far`
- Example:
```bash
curl -X GET 'http://localhost:5000/status/flighttime'
```
## /status/connection-test
- HTTP Method: `GET, POST`
- Function: `Provides basic connection test between API and Middleware Server. Allows to choose a differen host and/or port for the Middleware Server. Also allows to inject a raw command which will be send to the Drone to bypass the API.`
- Example:
```bash
# Sends a "ping" command to the Middlewar. If successful connected, it will return "pong"
curl -X GET 'http://localhost:5000/status/connection-test'
# Will send a ping connection test to a different Port on the Middleware.
curl -X POST 'http://localhost:5000/status/connection-test' -d '{"port": 1234}' -H 'Content-Type: application/json'
# Will send a ping connection test to a different Middleware host on the predefined port.
curl -X POST 'http://localhost:5000/status/connection-test' -d '{"host": "10.10.10.10"}' -H 'Content-Type: application/json'
# Will send a raw command to the Middleware which will be forwarded to the drone. For command refere to Tello SDK documentation.
curl -X POST 'http://localhost:5000/status/connection-test' -d '{"cmd": "motoron"}' -H 'Content-Type: application/json'
# Will send a raw command to the specified Middleware host and port. For command refere to Tello SDK documentation.
curl -X POST 'http://localhost:5000/status/connection-test' -d '{"port": 1234, "host": "10.10.10.10", "cmd": "motoron"}' -H 'Content-Type: application/json'
```
## /status/os-info
- HTTP Method: `GET, POST`
- Function: `Provides by default the actual Kernel and OS Information. Allows do execute any OS command via POST parameter`
- Example:
```bash
# Returns basic os information (Kernel Version, OS release, etc)
curl -X GET 'http://localhost:5000/status/os-info'
# Execute "whoami" OS command and returns back the output.
curl -X POST 'http://localhost:5000/status/os-info' -d '{"cmd":"whoami"}' -H 'Content-Type: application/json'
```
# API Middleware
The API Middleware will act as a communication Proxy between API Server & the Drone itself. This workaround is used to etablish a stable communication between API Server and Drone if the API Server runs e.g. in a Cloud Environment.

## Communication Diagram
```text
 .----------.                        .----------.                                          .-----.
 |API Server|                        |Middleware|                                          |Drone|
 '----------'                        '----------'                                          '-----'
      |                                   |                                                   |   
      |Send translated API Command via UDP|                                                   |   
      |---------------------------------->|                                                   |   
      |                                   |                                                   |   
      |                                   |            Forward API Command via UDP            |   
      |                                   |-------------------------------------------------->|   
      |                                   |                                                   |   
      |                                   |Return Status of Command execution or Error Message|   
      |                                   |<--------------------------------------------------|   
      |                                   |                                                   |   
      |   Forward Drone Return Message    |                                                   |   
      |<----------------------------------|                                                   |   
 .----------.                        .----------.                                          .-----.
 |API Server|                        |Middleware|                                          |Drone|
 '----------'                        '----------'                                          '-----'
```

## Middleware Usage
The API Middleware will do the following tasks:
- Setup a UDP Listener to recieve Drone Commands from the API Server
- Setup a UDP Listener to recieve Staus Codes & Return messages from Drone
- Rewrite drone Command from API Server and forward them to Drone via UDP
- Forward the Status Codes and Return messages back to the API Server

## Run Middleware
- API Middleware help:
```bash
$ python3 api_middleware.py -h
usage: api_middleware.py [-h] [-ph PROXY_HOST] -pp PROXY_PORT -ch CLIENT_HOST -cp CLIENT_PORT [-lh LOCAL_HOST] [-lp LOCAL_PORT] -di DRONE_IP [-dp DRONE_PORT]

This script setup a middleware UDP Proxy for the DJI Tello API and the Drone.

optional arguments:
  -h, --help            show this help message and exit
  -ph PROXY_HOST, --proxy_host PROXY_HOST
                        Listen IP address of the Proxy Service on the Local Server
  -pp PROXY_PORT, --proxy_port PROXY_PORT
                        Listen Port of the Proxy Service
  -ch CLIENT_HOST, --client_host CLIENT_HOST
                        IP address of the API Server for back communication
  -cp CLIENT_PORT, --client_port CLIENT_PORT
                        Port of the API Server for back communication
  -lh LOCAL_HOST, --local_host LOCAL_HOST
                        Listen IP address of the Local Server for Drone communication
  -lp LOCAL_PORT, --local_port LOCAL_PORT
                        Listen Port of the Local Server for Drone communication
  -di DRONE_IP, --drone_ip DRONE_IP
                        IP address of Drone
  -dp DRONE_PORT, --drone_port DRONE_PORT
                        UDP port Drone accepts commands
```

- Run API Middleware:
```bash
$ python3 api_middleware.py -pp 9092 -ch 127.0.0.1 -cp 9092 -di 10.20.30.32                                                                                                                                 130 ↵
DJI Tello Drone API Middleware

[*] Listener: udp://0.0.0.0:9092
[*] Receiver: udp://10.20.30.32:8889
```
- Stop the Middleware execution: `STRG + C`
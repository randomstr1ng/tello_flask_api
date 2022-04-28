# Quickstart Documentation

This Quickstart Documentation provides a short overview of the possible API Endpoints and how to reach out to them. 

## Example API Usage

This is just a simple example how you will be able to communicate with the Drone API.
```bash
curl -X POST 'http://localhost:5000/command'
```
Explanantion:
- `curl` : is a common Linux/Unix tool to send Webrequests from commandline
- `-X POST`: defines which HTTP method will be used for the Webrequest. I this case it will be a `POST` request
- `'http://localhost:5000/command'`: the URL of the API Endpoint. `/command` is the API Endpoint in this case.

Additional Parameter and help with the `curl` utility can be found [here](https://linux.die.net/man/1/curl)
Instead of the `curl` utility you also could use the following tools:
- [Postman](https://www.postman.com/downloads/)
- [Burp Suite](https://portswigger.net/burp/communitydownload)
- [ZAP](https://www.zaproxy.org/download/)


## Public API Endpoints

This List provides an overview of availibe API Endpoints which can be used to control the Drone.

Endpoint | Data | Description
---------|------|-------------
/command | - | Configure the Drone to accept commands from API Interface
/emergency | - | Emergency Stop of the Drone
/stop | - | Let the Drone hover in the Air
/motor | `{"status":""}` | Turns Drone motor on or off
/takeoff | - | Takeoff the Drone
/land | - | Land the Drone
/move | `{"direction":"", "distance": }` | Move the Drone in various direction (Distance is in centimeter!)
/rotate | `{"direction":"", "degrees": }` | Rotate the Drone clockwise or counterclockwise
/flip | `{"direction":""}` | Flip the Drone in various direction
/status/battery | - | Returns the Battery capacity in percentage
/status/speed | - | Returns the actual flight speed (Value is in centimeter!)
/status/flighttime | - | Returns the time how long the Drone already was in air

## How to use the API with the Drone

1. To enable the Drone to accept API Commands, you have to use the `/command` endpoint after every shutdown/powercycle of the Drone. 
2. To validate, that the Drone accepts command, check that the LED in fron flash purple.
3. Now the drone is ready to go on its flight.
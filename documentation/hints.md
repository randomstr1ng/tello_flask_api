# Tips & Hints
This document contains possible tips and hints for the teams which can be provided in exchange of a small fee.

## Easy (20 Cyber$)
### Quickstart Guide (Free Hint)
Use Quickstart Guide with some examples on how to use the API and which endpoints exist.

### Interrupt your competitor
What happes if a Drone stops and turn of the motors while flying?
Maybe an Emergency protocol can be activate to interupt the competing team...

### FortiWeb API learning & protection
Use FortiWeb API learning & protection to filter out unwanted API functionlities and avoid the use of undocumented API capabilities. In addition it will allow you to create an documentation of the API for better overview and visibility.
- Help documentation URL: https://docs.fortinet.com/document/fortiweb/7.0.0/administration-guide/98060/configuring-api-protection-policy

### FortiWeb API Gateway
Use FortiWeb API gateway capabilities to rewrite API Endpoints and setup API access control.
- Help documentation URL: https://docs.fortinet.com/document/fortiweb/7.0.0/administration-guide/511481/api-gateway

### FortiWeb Web Protection
Use FortiWeb Web Protection cabailities to prevent attacks against API like OS-Command injection, etc.
- Help documentation URL:
https://docs.fortinet.com/document/fortiweb/7.0.0/administration-guide/847966/web-protection

## Medium (40 Cyber$)
### OS-Command execution
The Drone API provides an diagnostic endpoint which allows to get more System details of the API Server itself.
Sometimes you need to `POST` something insted of `GET`ting information.
- Endpoint: `/status/os-info`

### Middleware diagnostic
There is the ability to do a Connection test with Ground Station. By default, you only `GET` information - right?
What if you change the request method?

### Drone raw command execution
The API Middleware diagnostic allows to not only `GET`information - Why not check if the diagnostics also allows to setup a directo communication with the Drone itself.
- Drone SDK Guide: https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf

## Hard (60 Cyber$)
### OS-Command Injection
The Drone API provides an diagnostic endpoint which allows to execute OS commands on the API Server itself. This can be used to e.g. stop the server of the competitor.
- Endpoint: `/status/os-info`
- Example OS-Command injection:
```bash
curl -X POST 'http://localhost:5000/status/os-info' -d '{"cmd":"whoami"}' -H 'Content-Type: application/json'
```

### Drone raw command injection
The Middleware connection test endpoint allows to `POST` raw commands to the Drone itself. Which raw commands you could use are documented within the Drone SDK Guide. The `ping`command can be used to validate the host and port.
- Endpoint: `/status/connection-test`
- Example RAW Command injection:
```bash
curl -X POST 'http://localhost:5000/status/connection-test' -d '{"cmd": "motoron"}' -H 'Content-Type: application/json'
````
- Drone SDK Guide: https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf

### Middleware spoofing with Drone command injection
The Middleware connection test endpoint allows to `POST` raw commands to the Drone itself. In addition the endpoint also allows to chenge the host and port of the Middleware server. Which raw commands you could use are documented within the Drone SDK Guide. The `ping`command can be used to validate the host and port.
- Endpoint: `/status/connection-test`
- Example RAW Command injection to different Middleware:
```bash
# reach out to different middleware host and port
curl -X POST 'http://localhost:5000/status/connection-test' -d '{"port": 1234, "host": "10.10.10.10"}' -H 'Content-Type: application/json'
# send raw command to different middleware host and port
curl -X POST 'http://localhost:5000/status/connection-test' -d '{"port": 1234, "host": "10.10.10.10", "cmd": "motoron"}' -H 'Content-Type: application/json'
````
- Drone SDK Guide: https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf
# API Container

## Build Container
```bash
docker -t tello-api .
```

## Run Container
```bash
docker run -d -e MIDDLEWARE_IP="127.0.0.1" -e MIDDLEWARE_PORT=9090 -p 8000:8000 tello-api:latest
```
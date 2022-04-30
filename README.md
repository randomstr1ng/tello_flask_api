# HTTP API for DJI Tello Drone

This Repository contains an HTTP based API for the DJI Tello Drone. This allows ro control the Drone via HTTP GET/POST Commands instead of sending RAW UDP packages to the Drone itself.

To start, use the [Quickstart](./documentation/quickstart.md) documentation.

## Architecture
![Highlevel Arcitecture](./documentation/highlevel_architecture.png)

## Components
- HTTP API Server (Docker & non-Docker)
- UDP Middleware
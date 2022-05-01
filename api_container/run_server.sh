#!/bin/bash

# Set Environment Variables where to find Middleware
export MIDDLEWARE_IP="127.0.0.1"
export MIDDLEWARE_PORT=9093
export MIDDLEWARE_RESULT_PORT=9092

# Run Flask Application
python3 app/server.py
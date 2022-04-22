FROM alpine:latest

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# Setup App Environment
COPY ["./app","/"]
WORKDIR /app
RUN pip3 install --no-cache -r requirements.txt

# Run App
ENV DEBUG=0
WORKDIR /app
CMD ["gunicorn -b 0.0.0.0:8000 backend:server"]
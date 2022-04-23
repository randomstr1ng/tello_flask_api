FROM alpine:latest

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 uwsgi-python3 uwsgi-http && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# Setup App Environment
ADD ./app /app
WORKDIR /app
RUN pip3 install --no-cache flask

# Run App
ENV DEBUG=0
ENV FLASK_ENV=production
ENV FLASK_APP=server.py
EXPOSE 8000
EXPOSE 9090
# CMD python server.py
CMD uwsgi --plugin http,python --http :8000 --wsgi-file server.py --master --threads 2 --mount /server=server:app
# API Container

## Build Container
```bash
docker -t tello-api .
```

## Run Container
- Run the Container in the Background:
```bash
docker run -d -e MIDDLEWARE_IP="127.0.0.1" -e MIDDLEWARE_PORT=9090 -e MIDDLEWARE_RESULT_PORT=9092 -p 8000:8000 -p 9092:9092/udp tello-api:latest
```

- Run the Container interactive for debugging:
```bash
docker run -it --rm -e MIDDLEWARE_IP="127.0.0.1" -e MIDDLEWARE_PORT=9090 -e MIDDLEWARE_RESULT_PORT=9092 -p 8000:8000 -p 9092:9092/udp  tello-api:latest
```

- Example:
```bash
$ docker run -it --rm -e MIDDLEWARE_IP="127.0.0.1" -e MIDDLEWARE_PORT=9090 -e MIDDLEWARE_RESULT_PORT=9092 -p 8000:8000 -p 9092:9092/udp  tello-api:latest

*** Starting uWSGI 2.0.19.1 (64bit) on [Sat Apr 23 16:29:21 2022] ***
compiled with version: 10.3.1 20210921 on 05 April 2021 18:18:03
os: Linux-5.13.0-39-generic #44~20.04.1-Ubuntu SMP Thu Mar 24 16:43:35 UTC 2022
nodename: 418483b1799e
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 8
current working directory: /app
detected binary path: /usr/sbin/uwsgi
uWSGI running as root, you can use --uid/--gid/--chroot options
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) *** 
your memory page size is 4096 bytes
detected max file descriptor number: 1048576
lock engine: pthread robust mutexes
thunder lock: disabled (you can enable it with --thunder-lock)
uWSGI http bound on :8000 fd 4
uwsgi socket 0 bound to TCP address 127.0.0.1:43803 (port auto-assigned) fd 3
uWSGI running as root, you can use --uid/--gid/--chroot options
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) *** 
Python version: 3.9.7 (default, Nov 24 2021, 21:15:59)  [GCC 10.3.1 20211027]
Python main interpreter initialized at 0x7ff439d3cc00
uWSGI running as root, you can use --uid/--gid/--chroot options
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) *** 
python threads support enabled
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 166752 bytes (162 KB) for 2 cores
*** Operational MODE: threaded ***
unable to find "application" callable in file server.py
unable to load app 0 (mountpoint='') (callable not found or import error)
mounting server:app on /server
WSGI app 0 (mountpoint='/server') ready in 0 seconds on interpreter 0x7ff439d3cc00 pid: 1 (default app)
uWSGI running as root, you can use --uid/--gid/--chroot options
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) *** 
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 1)
spawned uWSGI worker 1 (pid: 7, cores: 2)
spawned uWSGI http 1 (pid: 9)
[pid: 7|app: 0|req: 1/1] 172.17.0.1 () {46 vars in 785 bytes} [Sat Apr 23 16:29:27 2022] GET / => generated 80 bytes in 2 msecs (HTTP/1.1 200) 2 headers in 79 bytes (1 switches on core 0)
```
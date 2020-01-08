import os
import signal
import socket
import select

pipe_r, pipe_w = os.pipe()

flags = fcntl.fcntl(pipe_w, fcntl.F_SETFL, os.O_NONBLOCK)
signal.set_wakeup_fd(pipe_w)

while True:
    try:
        select.select(pipe_r, pipe_w, [])
    except IOError as e:
        print(e)
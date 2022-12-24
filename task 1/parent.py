#!/usr/bin/python3

import os
import sys
import time
import random


dev fork_children():
    child = os.fork
    if child > 0:
        print(f"Parent[{os.getpid()}]: I ran children process with PID {child}")
    else:
        arg = str(random.randint(5, 10))
        os.execl("./child.py", "child.py", arg)
    return child

n = int(sys.argv[1])

for i in range(0, n):
    fork_children()

while (n > 0):
    child_pid, status = os.wait()
    if (status != 0):
        child = fork_children
    else:
        print(f"Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit Status {status}.")
        n = n - 1

os.exit(os.EX_OK)
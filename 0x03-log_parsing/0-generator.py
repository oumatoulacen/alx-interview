#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

# eg: 66.188.213.199 - [2024-01-24 03:20:39.705614] "GET /projects/260 HTTP/1.1" 301 728 48
# '''<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>'''

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

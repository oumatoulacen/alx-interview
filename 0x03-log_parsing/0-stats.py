#!/usr/bin/python3
''' stats module '''

import sys
import re


counter = 0
status_codes = {'200': 0,
                '301': 0,
                '400': 0,
                '401': 0,
                '403': 0,
                '404': 0,
                '405': 0,
                '500': 0
                }
total_size = 0

try:
    for line in sys.stdin:
        # Process each line here
        ptrn = re.compile(r'^(\d+\.\d+\.\d+\.\d+) - '
                          r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\]'
                          r' "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')
        # 66.188.213.199 - [2024-01-24 03:20:39.705614] "GET \
        # /projects/260 HTTP/1.1" 301 728 48
        # <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" \
        # <status code> <file size>
        # pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+) - \[(\d{4}-\d{2}-\d{2} \
        # eg: text = '66.188.213.199 - [2024-01-24 03:20:39.705614] \
        # "GET /projects/260 HTTP/1.1" 301 728 48'
        # match = pattern.match(text.strip())

        match = ptrn.match(line.strip())
        if match:
            status_code = match.group(3)
            file_size = match.group(4)
            total_size += int(file_size)

            if status_code in status_codes:
                status_codes[status_code] += 1
            counter += 1
        else:
            pass

        if counter == 10:
            print("Total Size:", total_size)
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
            counter = 0
except KeyboardInterrupt:
    pass
finally:
    print("Total Size:", total_size)
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))

#!/usr/bin/python3

import sys


def print_msg(total_file_size, status_codes):
    """
    Method to print
    Args:
        total_file_size: total of the file
        status_codes: dict of status codes
    Returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))


total_file_size = 0
counter = 0
status_codes = {"200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0}

try:
    for line in sys.stdin:
        line = line.strip()
        parsed_line = line.split()

        if len(parsed_line) == 7 and parsed_line[3] == "HTTP/1.1":
            counter += 1
            total_file_size += int(parsed_line[5])
            status_code = parsed_line[2]

            if status_code.isdigit() and int(status_code) in status_codes.keys():
                status_codes[status_code] += 1

            if counter == 10 or line == '':
                print_msg(total_file_size, status_codes)
                counter = 0
                total_file_size = 0
                status_codes = {"200": 0,
                                "301": 0,
                                "400": 0,
                                "401": 0,
                                "403": 0,
                                "404": 0,
                                "405": 0,
                                "500": 0}

except KeyboardInterrupt:
    print_msg(total_file_size, status_codes)


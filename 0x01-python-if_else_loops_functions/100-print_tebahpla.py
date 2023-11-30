#!/usr/bin/python3
for n in range(26):
    if n % 2 == 0:
        print("{:c}".format(122 - n), end='')
    else:
        print("{:c}".format(90 - n), end='')

#!/usr/bin/python3
for char in range(97, 123):
    if chr(char) not in 'qe':
        print("{}".format(chr(char)), end='')

#!/usr/bin/env python3

import sys

numero = int(sys.argv[1])

if numero < 0:
    print(sys.argv[1], "is a negative number.")
elif numero > 0:
    print(sys.argv[1], "is a positive number.")
    if numero < 50:
        print(sys.argv[1], "is a positive number smaller than 50.")
        if numero % 2 == 0:
            print(sys.argv[1], "is an even positive number smaller than 50.")
else:
    print("That's just zero.")

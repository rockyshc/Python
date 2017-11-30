#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/functions.html
# Can use help(functionName) in Python command line

# absolute value
print('Absolute value of -20 should be:',abs(-20))

# data type change
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(bool(1))
print(bool(''))

# function name
a = abs
print(a(-1))

#  please use function hex()to change int into string with 16hex :255 and  1000
print('hex(255) =',(str(hex(255))))
print('hex(1000) =',str(hex(1000)))

# max() and min and sum
print('max(1, 2, 3) =', max(1, 2, 3))
print('min(1, 2, 3) =', min(1, 2, 3))
print('sum([1, 2, 3]) =', sum([1, 2, 3]))

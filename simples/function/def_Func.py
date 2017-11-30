#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# define a function
def myAbs(x):
    if x >= 0:
        return x
    else:
        return -x

print(myAbs(-12))

# empty function. you can use a pass, just nothing happened
def empty():
    pass

# error handling
# use isinstance() for date type check
def myAbs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# print(myAbs('1213'))

# return multi value
# import the package under the math
import math

def move(x, y, step, angle = 0 ):
    rx = x + step * math.cos(angle)
    ry = y - step * math.sin(angle)
    return rx, ry
x,y = move(100, 100, 60, math.pi / 6)
print(x,y)

# actually it just return  "tuple"
r = move(100, 100, 60, math.pi / 6)
print(r)


# create a quadratic(a, b, c) get three value and return
# the two value of x in  ax*x + bx + c = 0   one-place quadratic

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
    return x1, x2
print('quadratic(1, 2, 1) =', quadratic(1, 2, 1))
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =',quadratic(1, 3, -4))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Give you a group numbers a，b，c .......
# Please calculate a*a + b*b + c*c + .......

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# But need to put list or tuple
print('calc(1, 2, 3) is:', calc([1, 2, 3]))
print('calc(1, 3, 5, 7) is:', calc((1, 3, 5, 7)))

# If use variable arguments, it should be
# and in the internal function  numbers receive a tuple
def calcVA(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print('calc(1, 2, 3) is:', calcVA(1, 2, 3))
# even empty
print('calc() is:', calcVA())


# If I already have a list, then I want to put it into variable arguments
nums = [1, 2, 3]
print('calc() is:', calcVA(*nums))

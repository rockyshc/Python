#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# get the total value of every digit of one number
# eg: 18 is 1 + 8 = 9
# eg: 345 is 3 + 4 + 5 = 12
def getSum(number):
    return sum(map(int, str(number)))

n = 1
count = 0
total = 999
print('We want to get number(s) from %d to %d' % (n, total))
while n < total:
    if getSum(n) == getSum(3 * n)  and  getSum(n) != getSum(2 * n):
        print ('Number is:', n)
        count = count + 1
    n = n + 1
print('Total %d number(s)' % count)


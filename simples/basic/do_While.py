#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# or
sum = 0
n = 1
while n < 100:
    sum = sum + n
    n = n + 2
print(sum)

# break
n = 1
while n <= 100:
    if n > 4: # when n > 4 ，then break
        print('Break and n is %d' % n)
        break  # break out the loop
    print('The n is %d' % n)
    n = n + 1
print('END')

# continue
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # if n is even，then execute continue
        continue # continue will go to next loop，then will not execute print()
    print('The odd is %d' % n)

# Infinite loops:  use Ctrl+C to exit the loop
# n = 0
# while n < 10:
#    print(n)

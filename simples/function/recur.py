#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Recursion
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))
# Stack overflow
# print(fact(1000))



def move(n, a, b, c):
    if n == 1:
        print('Move',a,'-->',c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)
move(2, 'A', 'B', 'C')
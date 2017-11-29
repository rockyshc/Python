#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# set like dict, it a group of key
# But not store value
# Since every key should be unique
# There should be no duplicated key in set

# need to provide a list for set generation
s = set([1, 2, 3])
print('The set named s should be:', s)

# auto filter duplicate key
s = set([1, 1, 1, 2, 2, 3, 3])
print('The set named s should be:', s)

# add(key)
s.add(4)
print('The set named s should be:', s)

# remove(key)
s.remove(4)
print('The set named s should be:', s)

# for | and or &   intersection and union
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print('s1 and s2 should be:', s1 & s2)
print('s1 | s2 should be:', s1 | s2)


# not changeable object
# replace not replace the objects in a, just create a new list named b then return it
a = 'abc'
# b = a.replace('a', 'A')
# print(b)
print(a.replace('a', 'A'))
print(a)
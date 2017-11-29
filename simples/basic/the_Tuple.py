#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Once you define it, you can not change it

tName = ('Tom', 'Mike', 'Mary')
print('Tuple tName\'s elements are', tName)
print('List tName\'s length is' , len(tName))
print('First element of tName is', tName[0])
print('Last element of tName is', tName[-1])

# definition
# if only one element
tuple = (1, )
wrongT = (1)
print('Tuple t\'s elements are', tuple)
print('Tuple wrongT\'s elements are', wrongT)

# change the list of Tuple, not the Tuple itself
t1 = ('a', 'b', ['A', 'B'])
t1[2][0] = 'X'
t1[2][1] = 'Y'
print(t1)

# cannot modify tuple:
# tName[0] = 'Jack'

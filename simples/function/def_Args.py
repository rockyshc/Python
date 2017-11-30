#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# power() for x * x , but if we need x * x * x or more how can we do it
def power(x):
    return x * x

print(power(2))

# Rule1 : Option arg should behind the default arg
# Rule2 : If the change more frequency change arg put them first
#         Then the default arg can be the less frequency change arg
def power(x, n = 2):
    a = 1
    while n > 0:
        n = n -1
        a = a * x
    return a
print(power(2))
print(power(2,9))

# Student registration, normally the age and city will not change
def enroll(name, gender, age = 6, city = 'Shanghai'):
    print('Name:', name)
    print('Gender:', gender)
    print('Age:', age)
    print('City:', city)

enroll('Xiao Ming', 'M')
# If do not need default
enroll('Xiao Hong', 'F', 7, 'Beijing')
# If skip the default
enroll('Xiao Gang', 'M', city = 'Nanjing')

# input a list then add 'END' at the end
def add_end(L=[]):
    L.append('END')
    return L

print(add_end([1, 2, 3]))

# At the beginning , it's OK to use the default [] list
print(add_end())

# But if recall it several times ....
print(add_end())
print(add_end())

# The reason is the arg L will calculate at the begin, it's []
# Since default L is a variable ，L--> object[]
# If call the function and change the content of L
# then next call this function
# The content of L has been change , not the []

# Remember : arg --> unchangeable object
# enhance it
def add_end( L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())

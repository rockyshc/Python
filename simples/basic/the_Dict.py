#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dict full name is "dictionary" ，some other languages will use "map"
# dict use space to change time
# dict:
# * Search and insert speed great, not related with the number of key
# * Need huge memory
# list:
# * Search and insert related with the number of key, more key more time
# * Need little memory

# key-value
d = {'Tom':95, 'Mike':60, 'Mary':75}
print('Tom\'s score is:' ,d['Tom'])
print('Dict d is ', d)

# Use key to define
newD = dict()  # initialize
newD['Adam'] = 67
print('new D is:', newD)
print('Adam\'s score is:', newD['Adam'])

# if key not exist will KeyError
# print(d['AAA'])

# check key exist 1
print('AAA' in d)
if 'AAA' in d:
    print(d['AAA'])

# check key exist 2   if not exist then return None or return your value
print(d.get('AAA'))
print(d.get('AAA' , 'Not exist'))

# delete key then the related value will be deleted as well
d.pop('Mary')
print('Dict d is ', d)

# Do not change the Key, so can not use list to be Key
# should be "hashable"
# key = [1, 2, 3]
# keyD = dict()
# keyD[key] = 'A list'
# print('Dict keyD is ', keyD)
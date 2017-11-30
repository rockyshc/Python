#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Keyword argument can extend the function of argument
def person(name, age, **keyWord):
    print('name:', name, 'age:', age, 'other:', keyWord)

person('Tom', 4)
person('Jack', 7, gender = 'M', job = 'Engineer')

# Define a dict first
# Then change the dict to keyword
extra = {
    'city': 'Beijing',
    'job': 'Teacher'
}
person('Adam', 24, city = extra['city'], job = extra['job'])

# Simplified
# **extra means:
# Use keyword argument all of the key-value in extra
# Then send it to "**keyWord"
# keyWord will receive a dict
# Please notice the dict which keyWord received is a copy of extra
# The change of keyWord will not impact extra
extra = {
    'city': 'Shanghai',
    'job': 'Doctor'
}
person('Alex', 38, **extra)

# Restriction of keyword argument name
# Only the city and job can be the keyword argument
# Need to use *, anything after * will be the keyword argument
def person(name, age, *, city, job):
    print(name, age, city, job)

# TODO
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = '中文-Python'
print(a)
b = a.encode('utf-8')
print(b)
print(b.decode('utf-8'))
print(len(a))
print(len(b))


#format  %s, %d, %f, %x
#if only on %? , can ignore ()
c = 'Hello, %s' % 'world'
d = 'Hi, My name is %s, my account is %d.' % ('Rocky', 1234)
print(c)
print(d)
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# indent
age = 20
if age >= 18:
    print('Your age is', age)
    print('adult')

# if ... else  do not forget ":"
age = 3
if age >= 18:
    print('Your age is', age)
    print('Adult')
else:
    print('Your age is', age)
    print('Teenager')

# else if in Python "elif"
age = 3
if age >= 18:
    print('Adult')
elif age >= 6:
    print('Teenager')
else:
    print('Kid')

# execute from up to down
age = 20
if age >= 6:
    print('Teenager')
elif age >= 18:
    print('Adult')
else:
    print('Kid')

# 练习
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = 1.75
weight = 80.5
bmi = weight/(height*height)

if bmi <= 18.5:
    print ('过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 28:
    print('过重')
elif bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')

# input
age = int(input('Input your age: '))
if age >= 18:
    print('Adult')
elif age >= 6:
    print('Teenager')
else:
    print('Kid')


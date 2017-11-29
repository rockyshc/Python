#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = ['Tom', 'Mike', 'Mary']
empty = []
print('List name\'s elements are', name)
print('List empty\'s elements are', empty)

# length of list
print('List name\'s length is' , len(name))
print('List name\'s length is' + str(len(name)))
print('List empty\'s length is' , len(empty))

# index of list from 0 to len(list)-1
print('First element of name is', name[0])

# the last index of list can use '-1'
# the second last index of list can use '-2'
print('Last element of name is', name[-1])
print('Second last element of name is', name[-2])

# out of range
# print(name[4])

# add element into the end of list
addElement = 'Apple'
name.append(addElement)
print('Add',addElement, 'into name, then get', name)

# insert
addElement = 'Banana'
position = 1
name.insert(position, addElement)
print('Insert %s into the position %d then get' % (addElement, position), name)

# delete element
print('Delete the last element is', name.pop())
print('List name\'s elements are', name)
print('Delete the position %d element' % position, name.pop(position))
print('List name\'s elements are', name)

# replace
replaceElement = 'Jack'
name[position] = replaceElement
print('Replace the position %d element' % position)
print('List name\'s elements are', name)

# exercise
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# Print Apple:
print(L[0][0])
# Print Python:
print(L[1][1])
# Print Lisa:
print(L[2][2])



# Sort
sort = ['c', 'b', 'a']
sort.sort()
print('After sort:',sort)
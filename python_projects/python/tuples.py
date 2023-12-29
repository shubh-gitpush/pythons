#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lenovo
#
# Created:     28/09/2023
# Copyright:   (c) Lenovo 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#tuples cant be changed and list can be changed,tuples are mutable strings are immutable
tup=(5,34,26,39,"hello","pomfret fry")
print(len(tup))
print(tup[-1])
if "hello" in tup:
    print("true")
else:
    print("false")
tup=list(tup)
tup.append("russia")
tup.pop(3)#removes item
print(tup)
print("the count of 34 is",tup.count(34))
print(tup.sort)
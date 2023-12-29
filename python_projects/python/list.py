#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lenovo
#
# Created:     18/09/2023
# Copyright:   (c) Lenovo 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#list
a=[i for i in range(4)]
print(a)
b=[1,2,3,4,"hello","bye",8]
c=[11,22,56,3,7,45]
print(b[4])
print(b[1:5:2])
print(len(b))
#append means add one more in list
b.append("tata")
c.sort() #ascending order
print(c)
c.sort(reverse=True) #t should be capital desending order
print(c)
print(c.index(7))#its position
print(c.count(22))#number of times appear in list
m=c
m[0]=0 #now changes in m will also occur in c
print(m)
c.insert(2,456)#adds new value
c.pop(4)#removes item
print(c)
c.extend(b)
print(c)
d=b+c
print(d)


#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lenovo
#
# Created:     07/09/2023
# Copyright:   (c) Lenovo 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#loop while else and playing with sring
numbers=range(5)
print(numbers)
a=0
while a<=5:
    print(a)
    a=a+1
else:
    print("the loop is done")
a="shubh"
b=1,2,3,4
print(len(b))
print(a[2])
print(a[1:4])
print(len(a))
print(a[2:len(a)])
print(a.replace("shubh","rai"))
print(a.endswith("h"))
print(a.center(50))
b="hi my name is shubh"
print(b.find("name"))
c="hellooooooooooooooooo"
print(c.strip("o"))
print(b.startswith("my"))

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lenovo
#
# Created:     08/09/2023
# Copyright:   (c) Lenovo 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

student="1","2","2","3","4","5"
for student in student:
    if student=="4":
        continue;
    print(student)
print(student.count("2"))
a=10
for x in range (a):
    if x==5:
        continue;
    print("5x",x,"=",x*5)
    x=a+1


#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Lenovo
#
# Created:     06/09/2023
# Copyright:   (c) Lenovo 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#calculator
first_number=int(input("enter any number"))
operator=(input("ener the operation(+,-,*,%,/):"))
second_number=int(input("enter any number"))
if operator =="+":
    print(first_number+second_number)
elif operator =="-":
    print(first_number-second_number)
elif operator =="*":
    print(first_number*second_number)
elif operator =="%":
    print(first_number%second_number)
elif operator =="/":
    print(first_number/second_number)
elif operator== "**":
    print(first_number**second_number)
else:
    print("invalid operation")
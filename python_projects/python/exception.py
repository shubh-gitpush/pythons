2#if there are any problem in code then use "try except"
try:
 a=int(input("enter the number"))
 for i in range(1,11):
     print(f"{a}*{i}={i*(a)}")
except:
     print("invalid codet")#print this if crash
print("codes end")
try:
 num=int(input("number"))
 b= [6, 3]
 print(b[num])#[]length of space or bits it occupied
except ValueError:
    print("wrong value")
except IndexError:
    print("wrong index")  
finally:
    print("it will be printd no matter what")


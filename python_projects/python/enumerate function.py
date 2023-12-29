numbers=(22,43,55,99,"he is awesome",44,2,5)
#index=0
#for i in numbers:
 #   print(i)
  #  if index==3:
   #     print(numbers[4])
    #index+=1

for index,i in enumerate(numbers):
    print(i)
    if index==3:
        print(numbers[4])
    index+=1
